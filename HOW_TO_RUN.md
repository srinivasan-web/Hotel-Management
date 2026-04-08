# 🚀 HOW TO RUN - Complete Guide

**A step-by-step guide to run every component of the PlatinumRx Hotel Management Assignment**

---

## 📋 TABLE OF CONTENTS

1. [Prerequisites](#prerequisites)
2. [Setup](#setup)
3. [Run SQL Database](#run-sql-database)
4. [Run Python Scripts](#run-python-scripts)
5. [Generate Excel](#generate-excel)
6. [View Dashboards](#view-dashboards)
7. [Troubleshooting](#troubleshooting)
8. [Full Workflow](#full-workflow)

---

## 🔧 PREREQUISITES

Before running anything, ensure you have installed:

### Windows Installation

#### 1. Python (Required for Python scripts & Excel generation)
```bash
# Download: https://www.python.org/downloads/
# Install: Accept all defaults, especially "Add Python to PATH"

# Verify installation
python --version
pip --version
```

#### 2. MySQL (Required for SQL database)
```bash
# Download Community Server: https://dev.mysql.com/downloads/mysql/
# Windows Edition: https://dev.mysql.com/downloads/windows/installer/

# Install MySQL Community Server 8.0+
# Download MySQL Workbench (GUI client) - RECOMMENDED for beginners
```

#### 3. Git (Required for version control)
```bash
# Download: https://git-scm.com/download/win
# Install with all defaults
```

#### 4. Excel or LibreOffice Calc (For viewing spreadsheet)
- Excel: Usually pre-installed on Windows
- LibreOffice Calc: Free alternative (https://www.libreoffice.org/)

---

## ⚙️ SETUP

### Clone from GitHub
```bash
# Open PowerShell/Command Prompt
cd C:\YourFolder  (or any location)

# Clone the repository
git clone https://github.com/srinivasan-web/Hotel-Management.git

# Navigate to project
cd Hotel-Management
```

### Install Python Dependencies
```bash
pip install openpyxl  # For Excel generation
```

**Note**: All other functionality uses Python standard library (no additional packages needed)

---

## 🗄️ RUN SQL DATABASE

### Option A: MySQL Workbench (RECOMMENDED - GUI)

1. **Open MySQL Workbench**
   - Search for "MySQL Workbench" on Windows
   - Click to open

2. **Create Database**
   - File → Open SQL Script
   - Select: `SQL/01_Hotel_Schema_Setup.sql`
   - Click ⚡ Execute (or Ctrl+Shift+Enter)
   - Wait for completion

3. **Run Remaining Setup**
   - File → Open SQL Script
   - Select: `SQL/03_Clinic_Schema_Setup.sql`
   - Click ⚡ Execute

4. **Run Queries**
   - File → Open SQL Script
   - Select: `SQL/02_Hotel_Queries.sql`
   - Click ⚡ Execute to see results
   - Repeat with: `SQL/04_Clinic_Queries.sql`

### Option B: MySQL Command Line

```bash
# Connect to MySQL (enter password when prompted)
mysql -u root -p

# Inside MySQL prompt (you'll see "mysql> "):

# Create and select database
CREATE DATABASE platinum_rx;
USE platinum_rx;

# Run setup scripts
SOURCE C:\path\to\SQL\01_Hotel_Schema_Setup.sql;
SOURCE C:\path\to\SQL\03_Clinic_Schema_Setup.sql;

# Verify data loaded
SHOW TABLES;
SELECT COUNT(*) FROM users;
SELECT COUNT(*) FROM bookings;

# Run queries to see results
SOURCE C:\path\to\SQL\02_Hotel_Queries.sql;
SOURCE C:\path\to\SQL\04_Clinic_Queries.sql;
```

### Verify SQL Success

You should see results for all tables:
```
✓ users table: 2 records (Ravi, Arun)
✓ bookings table: 3 records
✓ items table: 3 records
✓ booking_commercials table: 6 records
✓ clinic_sales table: 8 records
✓ expenses table: 8 records
```

---

## 🐍 RUN PYTHON SCRIPTS

### Quick Start (Run All 3 Scripts)

```powershell
# Navigate to project
cd C:\path\to\Hotel-Management

# Run Script 1: Time Converter
python Python/01_Time_Converter.py

# Output should show:
# - convert_minutes(130) → "2 hrs 10 minutes" ✓
# - 9 test cases all passing ✓

# Run Script 2: Remove Duplicates
python Python/02_Remove_Duplicates.py

# Output should show:
# - 3 implementations (Simple, Set Tracking, Dict Order)
# - Performance benchmarking comparing O(n²) vs O(n)
# - Example: "programming" → "progamin" ✓

# Run Script 3: Data Analysis
python Python/03_Data_Analysis.py

# Output should show:
# - Hotel Revenue Analysis report
# - Clinic Sales Analysis report
# - Exports to hotel_revenue_export.json/csv
# - Exports to clinic_sales_export.json/csv
```

### Individual Script Details

#### Script 1: Time Converter (01_Time_Converter.py)
```bash
python Python/01_Time_Converter.py

# Expected Output:
# ============================================================
# TIME CONVERTER - TEST CASES
# ============================================================
# ✓ convert_minutes(  0) = '0 minutes'
# ✓ convert_minutes( 45) = '45 minutes'
# ✓ convert_minutes( 60) = '1 hr'
# ✓ convert_minutes(130) = '2 hrs 10 minutes'
# ...
```

#### Script 2: Remove Duplicates (02_Remove_Duplicates.py)
```bash
python Python/02_Remove_Duplicates.py

# Expected Output:
# ============================================================
# DUPLICATE REMOVAL UTILITY - TEST CASES
# ============================================================
# Testing all three implementations:
# - Simple (O(n²))
# - Set Tracking (O(n))
# - Dict Order (O(n)) - FASTEST
#
# Performance Results: Dict Order is fastest
```

#### Script 3: Data Analysis (03_Data_Analysis.py)
```bash
python Python/03_Data_Analysis.py

# Expected Output:
# ============================================================
# DATA ANALYSIS UTILITY - DEMO
# ============================================================
#
# EXAMPLE 1: Hotel Revenue Analysis
# ============================================================
# Data exported to hotel_revenue_export.json
# Data exported to hotel_revenue_export.csv
#
# EXAMPLE 2: Clinic Sales Analysis
# ============================================================
# Data exported to clinic_sales_export.json
# Data exported to clinic_sales_export.csv
```

---

## 📊 GENERATE EXCEL

The Excel file is already created (`Spreadsheets/Ticket_Analysis.xlsx`), but you can regenerate it:

```bash
# Navigate to Spreadsheets folder
cd Spreadsheets

# Generate/Regenerate Excel file
python create_excel.py

# Output:
# ============================================================
# CREATING EXCEL SPREADSHEET
# ============================================================
# ✓ Excel file created successfully!
#   Location: ...\Ticket_Analysis.xlsx
#
#   Sheets created:
#     • ticket: Contains ticket_id, created_at, updated_at, status
#     • feedbacks: Contains feedback data with formulas
#
#   Formulas included:
#     • VLOOKUP: Fetches created_at from ticket sheet
#     • IF: Checks if same day (compares dates)
#     • IF: Checks if same hour (compares hours)
#     • COUNTIFS: Counts resolved same-day AND same-hour tickets
```

### View Excel File

```bash
# Open in Excel
start Spreadsheets/Ticket_Analysis.xlsx

# Or navigate directly to file and double-click
```

### Verify Excel Formulas

In `feedbacks` sheet:
- **Column C**: `=VLOOKUP(B2,ticket!A:B,2,FALSE)` - Retrieves dates from ticket sheet
- **Column E**: `=IF(INT(C2)=INT(D2),"Yes","No")` - Checks same day
- **Column F**: `=IF(HOUR(C2)=HOUR(D2),"Yes","No")` - Checks same hour
- **Summary Row**: `=COUNTIFS(E2:E6,"Yes",F2:F6,"Yes")` - Counts matches

---

## 📈 VIEW DASHBOARDS

### Generate HTML Dashboards

```bash
# Navigate to Dashboard folder
cd Dashboard

# Generate dashboards
python generate_dashboards.py

# Output:
# ============================================================
# GENERATING INTERACTIVE DASHBOARDS
# ============================================================
# ✓ Dashboards created successfully!
#   ✓ Hotel_Dashboard.html
#   ✓ Clinic_Dashboard.html
#
#   Features:
#     • Interactive Chart.js visualizations
#     • Responsive design (mobile-friendly)
#     • Real-time data display
#     • Professional styling and layouts
#     • Open in any web browser
```

### Open Dashboards in Browser

```bash
# Open Hotel Dashboard
start Dashboard/Hotel_Dashboard.html

# Open Clinic Dashboard
start Dashboard/Clinic_Dashboard.html
```

### What You'll See

**Hotel Dashboard**:
- 4 interactive charts
- Bookings by Guest (Doughnut chart)
- Revenue by Guest (Bar chart)
- Items Ordered (Bar chart)
- Revenue Trend (Line chart)
- Key metrics (Total bookings, revenue, guests, average)

**Clinic Dashboard**:
- 4 interactive charts
- Revenue by Channel (Pie chart: Online vs Offline)
- Financial Summary (Revenue, Expenses, Profit)
- Daily Revenue vs Expenses (Dual line chart)
- Daily Profit Margins (Bar chart)
- Key metrics (Revenue, expenses, profit, profit margin %)

---

## 🔍 TROUBLESHOOTING

### Python Issues

#### "python: command not found"
```bash
# Python not in PATH; install from https://www.python.org/downloads/
# Make sure to check "Add Python to PATH" during installation
# Restart PowerShell after installation
```

#### "openpyxl module not found"
```bash
pip install openpyxl
```

#### Script runs but shows errors
```bash
# Check Python version (must be 3.8+)
python --version

# Run script with verbose output
python -u Python/01_Time_Converter.py
```

### SQL Issues

#### "MySQL: command not found"
```bash
# Use MySQL Workbench GUI instead (recommended)
# Or install MySQL from: https://dev.mysql.com/downloads/mysql/
```

#### "Access denied" error
```bash
# Make sure MySQL is running:
# Windows Services → Search "Services" → Find "MySQL80" → Start it

# Or use MySQL Workbench with correct credentials
```

#### "No such file or directory"
```bash
# Make sure you're in the correct folder
cd C:\path\to\Hotel-Management
dir  # Should see SQL, Python, Spreadsheets, Dashboard folders
```

### Dashboard Issues

#### "Chart.js not loading"
```bash
# Dashboards need internet to load Chart.js from CDN
# Ensure you have internet connection
# JavaScript console may show warnings (normal if offline)
```

#### "Tooltip not showing"
```bash
# Hover over chart elements to see tooltips
# If not working, check:
# 1. Browser is supported (Chrome, Firefox, Safari, Edge)
# 2. JavaScript is enabled (usually default)
# 3. Try different browser if issues persist
```

---

## 🔄 FULL WORKFLOW

### Complete End-to-End Execution (10-15 minutes)

```bash
# ==================== STEP 1: SQL ====================
echo "Step 1: Setting up SQL Database..."

# Open MySQL Workbench and run:
# File → Open SQL Script → SQL/01_Hotel_Schema_Setup.sql → Execute
# File → Open SQL Script → SQL/03_Clinic_Schema_Setup.sql → Execute

echo "✓ SQL setup complete"

# ==================== STEP 2: PYTHON ====================
echo "Step 2: Running Python scripts..."

cd C:\path\to\Hotel-Management

python Python/01_Time_Converter.py
python Python/02_Remove_Duplicates.py
python Python/03_Data_Analysis.py

echo "✓ Python scripts complete"

# ==================== STEP 3: EXCEL ====================
echo "Step 3: Generating Excel spreadsheet..."

cd Spreadsheets
python create_excel.py
start Ticket_Analysis.xlsx

echo "✓ Excel generated and opened"

# ==================== STEP 4: DASHBOARDS ====================
echo "Step 4: Generating dashboards..."

cd ..\Dashboard
python generate_dashboards.py

start Hotel_Dashboard.html
start Clinic_Dashboard.html

echo "✓ Dashboards generated and opened"

# ==================== VERIFICATION ====================
echo "✓ ALL COMPONENTS RUNNING SUCCESSFULLY!"
```

---

## ✅ VERIFICATION CHECKLIST

After running everything, verify:

- [ ] **SQL Database**
  - [ ] MySQL running and database created
  - [ ] 6 tables populated with data
  - [ ] Queries execute and return results

- [ ] **Python Scripts**
  - [ ] 01_Time_Converter runs: converts 130 min → "2 hrs 10 minutes"
  - [ ] 02_Remove_Duplicates runs: "programming" → "progamin"
  - [ ] 03_Data_Analysis runs: generates reports and exports

- [ ] **Excel**
  - [ ] Ticket_Analysis.xlsx opens in Excel
  - [ ] VLOOKUP fetches data (Column C populated)
  - [ ] IF formulas show Yes/No (Columns E & F)
  - [ ] COUNTIFS shows count in summary row

- [ ] **Dashboards**
  - [ ] Hotel_Dashboard.html opens in browser
  - [ ] Shows 4 interactive charts with data
  - [ ] Hovering shows tooltips
  - [ ] Responsive on different screen sizes
  - [ ] Clinic_Dashboard.html opens in browser
  - [ ] Shows 4 financial charts
  - [ ] All metrics display correctly

---

## 📊 SAMPLE EXPECTED OUTPUTS

### SQL Query Results
```
Q1: Last Booked Room
booking_id | user_id | booking_date
-----------|---------|----------------------------------------
    3      |    1    | 2021-11-20

Q2: November Billing
booking_id | total_bill
-----------|----------
    1      | 1500.00
    2      | 2000.00
    3      | 3200.00
```

### Python Output
```
convert_minutes(130) = "2 hrs 10 minutes" ✓
remove_duplicates("programming") = "progamin" ✓
DataAnalyzer: 5 records analyzed, exported to JSON & CSV ✓
```

### Excel Summary
```
Feedback Summary:
- Total Records: 5
- Resolved Same Day: Yes, Yes, No, Yes, Yes
- Resolved Same Hour: No, No, No, Yes, Yes
- Count (Same Day AND Hour): 1
```

### Dashboard Metrics
```
Hotel:
- Total Bookings: 3
- Total Revenue: ₹6,700
- Unique Guests: 2
- Average Value: ₹2,234

Clinic:
- Total Revenue: ₹27,500
- Total Expenses: ₹14,700
- Net Profit: ₹12,800
- Profit Margin: 46.5%
```

---

## 🎯 QUICK REFERENCE

### Most Used Commands

```bash
# Run all Python scripts at once
cd C:\path\to\Hotel-Management
python Python/*.py

# Generate Excel
python Spreadsheets/create_excel.py

# Generate Dashboards
python Dashboard/generate_dashboards.py

# Open all dashboards
start Dashboard/Hotel_Dashboard.html
start Dashboard/Clinic_Dashboard.html
start Spreadsheets/Ticket_Analysis.xlsx

# View Git history
git log --oneline

# Check project status
git status
```

---

## 📞 NEED HELP?

1. **Python not working?** → Install from python.org, check PATH
2. **MySQL not working?** → Use MySQL Workbench GUI, ensure service is running
3. **Dashboards blank?** → Check internet, open browser console (F12)
4. **Git push issues?** → Verify credentials, check repository URL
5. **Excel formulas not working?** → Make sure both sheets exist and data is present

---

## 🚀 NEXT STEPS

After everything is running:

1. ✅ Verify all components work
2. ✅ Review the README.md for project details
3. ✅ Share GitHub repository link
4. ✅ Record a 5-10 min walkthrough (bonus for portfolio)
5. ✅ Add to portfolio/resume

---

**Created**: April 8, 2026  
**Version**: 1.0  
**Status**: ✅ Complete

**Happy coding! 🎉**
