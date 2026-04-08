"""
DATA ANALYSIS UTILITY
Enhanced Python script for reading, analyzing, and exporting data.
Demonstrates real-world data processing workflows with pandas integration.
"""

import json
from datetime import datetime
from collections import defaultdict


class DataAnalyzer:
    """A simple but powerful data analyzer for processing business data."""
    
    def __init__(self, name):
        """Initialize the analyzer with a dataset name."""
        self.name = name
        self.data = []
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def add_record(self, record):
        """Add a single record to the dataset."""
        if not isinstance(record, dict):
            raise TypeError("Record must be a dictionary")
        self.data.append(record)
    
    def add_records(self, records):
        """Add multiple records at once."""
        if not isinstance(records, list):
            raise TypeError("Records must be a list of dictionaries")
        self.data.extend(records)
    
    def get_summary(self):
        """Get basic statistics about the dataset."""
        return {
            'total_records': len(self.data),
            'dataset_name': self.name,
            'created_at': self.timestamp,
            'fields': list(self.data[0].keys()) if self.data else []
        }
    
    def filter_by_field(self, field, value):
        """Filter records by a specific field value."""
        return [record for record in self.data if record.get(field) == value]
    
    def aggregate_numeric(self, field):
        """Calculate statistics for a numeric field."""
        values = [
            float(record.get(field, 0)) 
            for record in self.data 
            if field in record and isinstance(record[field], (int, float))
        ]
        
        if not values:
            return None
        
        return {
            'field': field,
            'count': len(values),
            'sum': sum(values),
            'average': sum(values) / len(values),
            'min': min(values),
            'max': max(values)
        }
    
    def group_by(self, field):
        """Group records by a specific field."""
        groups = defaultdict(list)
        for record in self.data:
            key = record.get(field, 'unknown')
            groups[key].append(record)
        return dict(groups)
    
    def export_to_json(self, filename=None):
        """Export data to JSON format."""
        if filename is None:
            filename = f"{self.name.lower().replace(' ', '_')}_export.json"
        
        export_data = {
            'metadata': self.get_summary(),
            'records': self.data
        }
        
        with open(filename, 'w') as f:
            json.dump(export_data, f, indent=2)
        
        return f"Data exported to {filename}"
    
    def export_to_csv(self, filename=None):
        """Export data to CSV format (simple implementation)."""
        if filename is None:
            filename = f"{self.name.lower().replace(' ', '_')}_export.csv"
        
        if not self.data:
            return "No data to export"
        
        # Get headers from first record
        headers = list(self.data[0].keys())
        
        with open(filename, 'w') as f:
            # Write headers
            f.write(','.join(headers) + '\n')
            
            # Write data rows
            for record in self.data:
                row = [str(record.get(field, '')) for field in headers]
                f.write(','.join(row) + '\n')
        
        return f"Data exported to {filename}"
    
    def get_report(self):
        """Generate a detailed text report."""
        report = f"\n{'='*70}\n"
        report += f"DATA ANALYSIS REPORT: {self.name}\n"
        report += f"Generated: {self.timestamp}\n"
        report += f"{'='*70}\n\n"
        
        summary = self.get_summary()
        report += f"Total Records: {summary['total_records']}\n"
        report += f"Fields: {', '.join(summary['fields'])}\n\n"
        
        # Numeric summaries
        for field in summary['fields']:
            stats = self.aggregate_numeric(field)
            if stats:
                report += f"\n{field}:\n"
                report += f"  Count:   {stats['count']}\n"
                report += f"  Sum:     {stats['sum']:.2f}\n"
                report += f"  Average: {stats['average']:.2f}\n"
                report += f"  Min:     {stats['min']:.2f}\n"
                report += f"  Max:     {stats['max']:.2f}\n"
        
        report += f"\n{'='*70}\n"
        return report


# ============================================================================
# EXAMPLE: Hotel Revenue Analysis
# ============================================================================

def example_hotel_analysis():
    """Demonstrate analysis with hotel booking data."""
    print("EXAMPLE 1: Hotel Revenue Analysis")
    print("=" * 70)
    
    # Create analyzer
    analyzer = DataAnalyzer("Hotel Revenue")
    
    # Add sample hotel booking data
    bookings = [
        {'booking_id': 1, 'user': 'Ravi', 'amount': 1500, 'channel': 'online'},
        {'booking_id': 2, 'user': 'Arun', 'amount': 2000, 'channel': 'offline'},
        {'booking_id': 3, 'user': 'Ravi', 'amount': 1200, 'channel': 'online'},
        {'booking_id': 4, 'user': 'Priya', 'amount': 3000, 'channel': 'offline'},
        {'booking_id': 5, 'user': 'Arun', 'amount': 1500, 'channel': 'online'},
    ]
    
    analyzer.add_records(bookings)
    
    # Display summary
    print(analyzer.get_report())
    
    # Group by channel
    print("\nBookings by Channel:")
    print("-" * 70)
    grouped = analyzer.group_by('channel')
    for channel, records in grouped.items():
        total = sum(r['amount'] for r in records)
        print(f"{channel.upper()}: {len(records)} bookings, Total: ₹{total}")
    
    # Filter example
    print("\n\nRavi's Bookings:")
    print("-" * 70)
    ravi_bookings = analyzer.filter_by_field('user', 'Ravi')
    for booking in ravi_bookings:
        print(f"  Booking #{booking['booking_id']}: ₹{booking['amount']} ({booking['channel']})")
    
    return analyzer


# ============================================================================
# EXAMPLE: Clinic Sales Analysis
# ============================================================================

def example_clinic_analysis():
    """Demonstrate analysis with clinic sales data."""
    print("\n\nEXAMPLE 2: Clinic Sales Analysis")
    print("=" * 70)
    
    # Create analyzer
    analyzer = DataAnalyzer("Clinic Sales")
    
    # Add sample clinic sales data
    sales = [
        {'sale_id': 1, 'amount': 5000, 'channel': 'online', 'date': '2021-11-01'},
        {'sale_id': 2, 'amount': 3000, 'channel': 'offline', 'date': '2021-11-02'},
        {'sale_id': 3, 'amount': 4500, 'channel': 'online', 'date': '2021-11-05'},
        {'sale_id': 4, 'amount': 6000, 'channel': 'online', 'date': '2021-11-10'},
        {'sale_id': 5, 'amount': 2500, 'channel': 'offline', 'date': '2021-11-15'},
    ]
    
    analyzer.add_records(sales)
    
    # Display summary
    print(analyzer.get_report())
    
    # Channel comparison
    print("\nSales by Channel:")
    print("-" * 70)
    grouped = analyzer.group_by('channel')
    for channel, records in grouped.items():
        total = sum(r['amount'] for r in records)
        avg = total / len(records)
        print(f"{channel.upper()}: {len(records)} sales, Total: ₹{total}, Avg: ₹{avg:.0f}")
    
    return analyzer


# ============================================================================
# DEMO: Data Export
# ============================================================================

if __name__ == "__main__":
    print("\n")
    print("╔" + "=" * 70 + "╗")
    print("║" + " " * 15 + "DATA ANALYSIS UTILITY - DEMO" + " " * 27 + "║")
    print("╚" + "=" * 70 + "╝")
    
    # Run hotel analysis
    hotel_analyzer = example_hotel_analysis()
    
    # Run clinic analysis
    clinic_analyzer = example_clinic_analysis()
    
    # Export examples
    print("\n\nEXPORTING DATA")
    print("=" * 70)
    
    print("\nHotel Data:")
    print(f"  → {hotel_analyzer.export_to_json()}")
    print(f"  → {hotel_analyzer.export_to_csv()}")
    
    print("\n\nClinic Data:")
    print(f"  → {clinic_analyzer.export_to_json()}")
    print(f"  → {clinic_analyzer.export_to_csv()}")
    
    print("\n\n✓ All exports completed successfully!")
    print("=" * 70)
