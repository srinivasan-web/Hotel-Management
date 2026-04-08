# 🚀 QUICK START GUIDE

**One-click commands to run everything**

---

## 1️⃣ SETUP SQL DATABASE

### MySQL Command Line

```bash
# Connect to MySQL
mysql -u root -p

# Inside MySQL prompt:
CREATE DATABASE platinum_rx;
USE platinum_rx;
SOURCE C:\path\to\SQL\01_Hotel_Schema_Setup.sql;
SOURCE C:\path\to\SQL\03_Clinic_Schema_Setup.sql;
```

### MySQL Workbench (GUI)

1. Open MySQL Workbench
2. File → Open SQL Script → `01_Hotel_Schema_Setup.sql`
3. Click ⚡ Execute
4. Repeat for all 4 SQL files

---

## 2️⃣ RUN PYTHON SCRIPTS

```powershell
# Navigate to project
cd h:\hotel-menagement\PlatinumRx_Assignment

# Time Converter
python Python/01_Time_Converter.py

# Remove Duplicates (with performance benchmarking)
python Python/02_Remove_Duplicates.py

# Data Analysis
python Python/03_Data_Analysis.py

# Create / Regenerate Excel
python Spreadsheets/create_excel.py

# Generate Dashboards
python Dashboard/generate_dashboards.py
```

---

## 3️⃣ VIEW DASHBOARDS

```powershell
# Open in default browser
start Dashboard/Hotel_Dashboard.html
start Dashboard/Clinic_Dashboard.html
```

---

## 4️⃣ VIEW EXCEL ANALYSIS

```powershell
# Open in Excel
start Spreadsheets/Ticket_Analysis.xlsx
```

---

## 5️⃣ PUSH TO GITHUB

```bash
# Create repo on GitHub: https://github.com/new
# Then:

cd h:\hotel-menagement\PlatinumRx_Assignment
git remote add origin https://github.com/YOUR_USERNAME/PlatinumRx_Assignment.git
git branch -M main
git push -u origin main
```

---

## 📋 QUICK VERIFICATION

### ✅ SQL Test

```sql
-- In MySQL:
SELECT COUNT(*) as users FROM users;               -- Should be: 2
SELECT COUNT(*) as bookings FROM bookings;         -- Should be: 3
SELECT COUNT(*) as items FROM items;               -- Should be: 3
```

### ✅ Excel Test

- Open `Spreadsheets/Ticket_Analysis.xlsx`
- Check: VLOOKUP formula in column C (should show dates)
- Check: IF formulas in columns E & F (should show Yes/No)
- Check: Summary row shows count of resolved tickets

### ✅ Python Test

```bash
python Python/01_Time_Converter.py     # Should output: "2 hrs 10 minutes"
python Python/02_Remove_Duplicates.py  # Should output: "progamin"
python Python/03_Data_Analysis.py      # Should show reports and exports
```

### ✅ Dashboard Test

- Open `Hotel_Dashboard.html` → Should show 4 interactive charts
- Open `Clinic_Dashboard.html` → Should show 4 interactive charts
- Both should display metrics and be responsive

---

## 📁 FILE LOCATIONS

```
PlatinumRx_Assignment/
├── SQL/
│   ├── 01_Hotel_Schema_Setup.sql
│   ├── 02_Hotel_Queries.sql
│   ├── 03_Clinic_Schema_Setup.sql
│   └── 04_Clinic_Queries.sql
├── Spreadsheets/
│   ├── Ticket_Analysis.xlsx
│   └── create_excel.py
├── Python/
│   ├── 01_Time_Converter.py
│   ├── 02_Remove_Duplicates.py
│   └── 03_Data_Analysis.py
├── Dashboard/
│   ├── Hotel_Dashboard.html
│   ├── Clinic_Dashboard.html
│   └── generate_dashboards.py
├── README.md
└── COMPLETION_SUMMARY.md
```

---

## 🛠 TROUBLESHOOTING

| Issue           | Solution                                                      |
| --------------- | ------------------------------------------------------------- |
| No Python       | Install from: https://www.python.org/downloads/               |
| No MySQL        | Install from: https://dev.mysql.com/downloads/mysql/          |
| openpyxl error  | Run: `pip install openpyxl`                                   |
| Dashboard blank | Check browser console (F12), verify internet for Chart.js CDN |
| Git not found   | Install from: https://git-scm.com/download/win                |
| SQL errors      | Ensure MySQL is running: `net start MySQL80`                  |

---

## 💡 KEY TAKEAWAYS

✅ **SQL**: Complex queries with JOINs, GROUP BY, window functions  
✅ **Excel**: VLOOKUP, IF, COUNTIFS formulas  
✅ **Python**: OOP, algorithms, data processing  
✅ **Dashboards**: Interactive Chart.js visualizations  
✅ **Portfolio**: Professional GitHub repository

**You have everything needed for a junior data analyst role!** 🚀

---

## 📞 NEED HELP?

1. **Review README.md** - Comprehensive guide with all details
2. **Check COMPLETION_SUMMARY.md** - Project overview and stats
3. **Inspect Python files** - All code has docstrings and examples
4. **View SQL files** - Comments explain each query
5. **Open HTML dashboards** - Visual examples of data

---

**Created**: April 8, 2026  
**Status**: ✅ Production Ready  
**Next**: Push to GitHub! 🚀
