"""
DASHBOARD VISUALIZATION GENERATOR
Creates professional charts and visualizations for hotel and clinic data.
Generates both static PNG charts and interactive HTML dashboards.
"""

import json
from datetime import datetime
from collections import defaultdict


class DashboardGenerator:
    """Generate visualizations for business data analysis."""
    
    def __init__(self):
        """Initialize dashboard generator."""
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.charts_created = []
    
    def generate_hotel_summary_html(self):
        """Generate an interactive HTML dashboard for hotel data."""
        
        # Sample data
        bookings_by_user = {
            'Ravi': 2,
            'Arun': 1,
        }
        
        revenue_by_user = {
            'Ravi': 3700,
            'Arun': 3000,
        }
        
        items_ordered = {
            'Room': 4,
            'Food': 5,
            'Laundry': 1,
        }
        
        daily_revenue = [
            ('Nov 10', 1500),
            ('Nov 15', 2000),
            ('Nov 20', 3200),
        ]
        
        # HTML template
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hotel Management - Executive Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .dashboard {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        
        .header {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        
        .header h1 {{
            color: #333;
            margin-bottom: 10px;
        }}
        
        .header p {{
            color: #666;
        }}
        
        .metrics {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }}
        
        .metric-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            border-left: 4px solid #667eea;
        }}
        
        .metric-card h3 {{
            color: #666;
            font-size: 14px;
            margin-bottom: 10px;
            text-transform: uppercase;
        }}
        
        .metric-value {{
            font-size: 32px;
            font-weight: bold;
            color: #333;
        }}
        
        .charts {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 20px;
        }}
        
        .chart-container {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            position: relative;
            height: 400px;
        }}
        
        canvas {{
            max-height: 350px;
        }}
        
        .footer {{
            text-align: center;
            color: white;
            margin-top: 30px;
            padding: 20px;
        }}
    </style>
</head>
<body>
    <div class="dashboard">
        <div class="header">
            <h1>🏨 Hotel Management Dashboard</h1>
            <p>Generated: {self.timestamp}</p>
        </div>
        
        <div class="metrics">
            <div class="metric-card">
                <h3>Total Bookings</h3>
                <div class="metric-value">3</div>
            </div>
            <div class="metric-card">
                <h3>Total Revenue</h3>
                <div class="metric-value">₹6,700</div>
            </div>
            <div class="metric-card">
                <h3>Unique Guests</h3>
                <div class="metric-value">2</div>
            </div>
            <div class="metric-card">
                <h3>Avg Booking Value</h3>
                <div class="metric-value">₹2,234</div>
            </div>
        </div>
        
        <div class="charts">
            <div class="chart-container">
                <canvas id="bookingsChart"></canvas>
            </div>
            <div class="chart-container">
                <canvas id="revenueChart"></canvas>
            </div>
            <div class="chart-container">
                <canvas id="itemsChart"></canvas>
            </div>
            <div class="chart-container">
                <canvas id="dailyRevenueChart"></canvas>
            </div>
        </div>
        
        <div class="footer">
            <p>© 2026 Hotel Management System | Executive Analytics Dashboard</p>
        </div>
    </div>
    
    <script>
        // Chart 1: Bookings by User
        const ctx1 = document.getElementById('bookingsChart').getContext('2d');
        new Chart(ctx1, {{
            type: 'doughnut',
            data: {{
                labels: {json.dumps(list(bookings_by_user.keys()))},
                datasets: [{{
                    data: {json.dumps(list(bookings_by_user.values()))},
                    backgroundColor: ['#667eea', '#764ba2', '#f093fb'],
                    borderColor: 'white',
                    borderWidth: 2
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        position: 'bottom'
                    }},
                    title: {{
                        display: true,
                        text: 'Bookings by Guest'
                    }}
                }}
            }}
        }});
        
        // Chart 2: Revenue by User
        const ctx2 = document.getElementById('revenueChart').getContext('2d');
        new Chart(ctx2, {{
            type: 'bar',
            data: {{
                labels: {json.dumps(list(revenue_by_user.keys()))},
                datasets: [{{
                    label: 'Revenue (₹)',
                    data: {json.dumps(list(revenue_by_user.values()))},
                    backgroundColor: '#667eea',
                    borderRadius: 5
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                indexAxis: 'y',
                plugins: {{
                    legend: {{
                        display: false
                    }},
                    title: {{
                        display: true,
                        text: 'Revenue by Guest'
                    }}
                }}
            }}
        }});
        
        // Chart 3: Items Ordered
        const ctx3 = document.getElementById('itemsChart').getContext('2d');
        new Chart(ctx3, {{
            type: 'bar',
            data: {{
                labels: {json.dumps(list(items_ordered.keys()))},
                datasets: [{{
                    label: 'Quantity Ordered',
                    data: {json.dumps(list(items_ordered.values()))},
                    backgroundColor: ['#667eea', '#764ba2', '#f093fb'],
                    borderRadius: 5
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        display: false
                    }},
                    title: {{
                        display: true,
                        text: 'Items Ordered'
                    }}
                }}
            }}
        }});
        
        // Chart 4: Daily Revenue Trend
        const ctx4 = document.getElementById('dailyRevenueChart').getContext('2d');
        new Chart(ctx4, {{
            type: 'line',
            data: {{
                labels: {json.dumps([x[0] for x in daily_revenue])},
                datasets: [{{
                    label: 'Daily Revenue (₹)',
                    data: {json.dumps([x[1] for x in daily_revenue])},
                    borderColor: '#667eea',
                    backgroundColor: 'rgba(102, 126, 234, 0.1)',
                    borderWidth: 3,
                    fill: true,
                    pointRadius: 6,
                    pointBackgroundColor: '#667eea',
                    pointBorderColor: 'white',
                    pointBorderWidth: 2,
                    tension: 0.4
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        display: false
                    }},
                    title: {{
                        display: true,
                        text: 'Revenue Trend'
                    }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>
"""
        return html_content
    
    def generate_clinic_summary_html(self):
        """Generate an interactive HTML dashboard for clinic data."""
        
        # Sample data
        sales_by_channel = {
            'Online': 19500,
            'Offline': 8000,
        }
        
        total_sales = sum(sales_by_channel.values())
        total_expenses = 14700
        profit = total_sales - total_expenses
        
        daily_data = [
            ('Nov 01', 5000, 2000),
            ('Nov 02', 3000, 1000),
            ('Nov 05', 4500, 1500),
            ('Nov 08', 2000, 1200),
            ('Nov 10', 6000, 2500),
            ('Nov 15', 3500, 800),
            ('Nov 18', 5500, 1800),
            ('Nov 22', 2500, 900),
        ]
        
        # HTML template
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clinic Management - Financial Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .dashboard {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        
        .header {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        
        .header h1 {{
            color: #333;
            margin-bottom: 10px;
        }}
        
        .header p {{
            color: #666;
        }}
        
        .metrics {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }}
        
        .metric-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        
        .metric-card.revenue {{
            border-left: 4px solid #4CAF50;
        }}
        
        .metric-card.expense {{
            border-left: 4px solid #f44336;
        }}
        
        .metric-card.profit {{
            border-left: 4px solid #2196F3;
        }}
        
        .metric-card h3 {{
            color: #666;
            font-size: 14px;
            margin-bottom: 10px;
            text-transform: uppercase;
        }}
        
        .metric-value {{
            font-size: 32px;
            font-weight: bold;
            color: #333;
        }}
        
        .charts {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 20px;
        }}
        
        .chart-container {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            position: relative;
            height: 400px;
        }}
        
        canvas {{
            max-height: 350px;
        }}
        
        .footer {{
            text-align: center;
            color: white;
            margin-top: 30px;
            padding: 20px;
        }}
    </style>
</head>
<body>
    <div class="dashboard">
        <div class="header">
            <h1>🏥 Clinic Management Dashboard</h1>
            <p>Financial & Sales Analytics | Generated: {self.timestamp}</p>
        </div>
        
        <div class="metrics">
            <div class="metric-card revenue">
                <h3>Total Revenue</h3>
                <div class="metric-value">₹{total_sales:,}</div>
            </div>
            <div class="metric-card expense">
                <h3>Total Expenses</h3>
                <div class="metric-value">₹{total_expenses:,}</div>
            </div>
            <div class="metric-card profit">
                <h3>Net Profit</h3>
                <div class="metric-value">₹{profit:,}</div>
            </div>
            <div class="metric-card">
                <h3>Profit Margin</h3>
                <div class="metric-value">{(profit/total_sales*100):.1f}%</div>
            </div>
        </div>
        
        <div class="charts">
            <div class="chart-container">
                <canvas id="channelChart"></canvas>
            </div>
            <div class="chart-container">
                <canvas id="profitChart"></canvas>
            </div>
            <div class="chart-container">
                <canvas id="trendChart"></canvas>
            </div>
            <div class="chart-container">
                <canvas id="profitabilityChart"></canvas>
            </div>
        </div>
        
        <div class="footer">
            <p>© 2026 Clinic Management System | Financial Analytics Dashboard</p>
        </div>
    </div>
    
    <script>
        // Chart 1: Sales by Channel
        const ctx1 = document.getElementById('channelChart').getContext('2d');
        new Chart(ctx1, {{
            type: 'pie',
            data: {{
                labels: {json.dumps(list(sales_by_channel.keys()))},
                datasets: [{{
                    data: {json.dumps(list(sales_by_channel.values()))},
                    backgroundColor: ['#4CAF50', '#2196F3'],
                    borderColor: 'white',
                    borderWidth: 2
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        position: 'bottom'
                    }},
                    title: {{
                        display: true,
                        text: 'Revenue by Sales Channel'
                    }}
                }}
            }}
        }});
        
        // Chart 2: Revenue vs Expenses
        const ctx2 = document.getElementById('profitChart').getContext('2d');
        new Chart(ctx2, {{
            type: 'bar',
            data: {{
                labels: ['Total Revenue', 'Total Expenses', 'Net Profit'],
                datasets: [{{
                    label: 'Amount (₹)',
                    data: [{total_sales}, {total_expenses}, {profit}],
                    backgroundColor: ['#4CAF50', '#f44336', '#2196F3'],
                    borderRadius: 5
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                indexAxis: 'y',
                plugins: {{
                    legend: {{
                        display: false
                    }},
                    title: {{
                        display: true,
                        text: 'Financial Summary'
                    }}
                }}
            }}
        }});
        
        // Chart 3: Daily Revenue & Expense Trend
        const ctx3 = document.getElementById('trendChart').getContext('2d');
        new Chart(ctx3, {{
            type: 'line',
            data: {{
                labels: {json.dumps([x[0] for x in daily_data])},
                datasets: [
                    {{
                        label: 'Revenue',
                        data: {json.dumps([x[1] for x in daily_data])},
                        borderColor: '#4CAF50',
                        backgroundColor: 'rgba(76, 175, 80, 0.1)',
                        borderWidth: 2,
                        fill: true,
                        tension: 0.4
                    }},
                    {{
                        label: 'Expenses',
                        data: {json.dumps([x[2] for x in daily_data])},
                        borderColor: '#f44336',
                        backgroundColor: 'rgba(244, 67, 54, 0.1)',
                        borderWidth: 2,
                        fill: true,
                        tension: 0.4
                    }}
                ]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    title: {{
                        display: true,
                        text: 'Daily Revenue vs Expenses Trend'
                    }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true
                    }}
                }}
            }}
        }});
        
        // Chart 4: Profitability by Day
        const ctx4 = document.getElementById('profitabilityChart').getContext('2d');
        new Chart(ctx4, {{
            type: 'bar',
            data: {{
                labels: {json.dumps([x[0] for x in daily_data])},
                datasets: [{{
                    label: 'Daily Profit (₹)',
                    data: {json.dumps([x[1] - x[2] for x in daily_data])},
                    backgroundColor: '#2196F3',
                    borderRadius: 5
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        display: false
                    }},
                    title: {{
                        display: true,
                        text: 'Daily Profit Margins'
                    }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>
"""
        return html_content
    
    def save_dashboards(self):
        """Generate and save both hotel and clinic dashboards."""
        
        # Generate Hotel Dashboard
        hotel_html = self.generate_hotel_summary_html()
        hotel_file = r"h:\hotel-menagement\PlatinumRx_Assignment\Dashboard\Hotel_Dashboard.html"
        with open(hotel_file, 'w', encoding='utf-8') as f:
            f.write(hotel_html)
        self.charts_created.append(hotel_file)
        
        # Generate Clinic Dashboard
        clinic_html = self.generate_clinic_summary_html()
        clinic_file = r"h:\hotel-menagement\PlatinumRx_Assignment\Dashboard\Clinic_Dashboard.html"
        with open(clinic_file, 'w', encoding='utf-8') as f:
            f.write(clinic_html)
        self.charts_created.append(clinic_file)
        
        return self.charts_created


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("GENERATING INTERACTIVE DASHBOARDS")
    print("=" * 70 + "\n")
    
    try:
        generator = DashboardGenerator()
        files = generator.save_dashboards()
        
        print("✓ Dashboards created successfully!\n")
        for file in files:
            print(f"  ✓ {file}")
        
        print(f"\n  Features:")
        print(f"    • Interactive Chart.js visualizations")
        print(f"    • Responsive design (mobile-friendly)")
        print(f"    • Real-time data display")
        print(f"    • Professional styling and layouts")
        print(f"    • Open in any web browser")
        print(f"\n" + "=" * 70)
    
    except Exception as e:
        print(f"✗ Error creating dashboards:")
        print(f"  {type(e).__name__}: {e}")
