# 🎬 VIDEO RECORDING SCRIPT - Complete Guide

**Project**: PlatinumRx Hotel Management Assignment
**Duration**: 5-10 minutes
**Date**: April 8, 2026

---

## 🎯 VIDEO RECORDING OVERVIEW

**Goal**: Demonstrate your complete data analyst portfolio project working end-to-end

**Tools Needed**:

- Screen recording software (Windows Game Bar or OBS Studio)
- Web browser (Chrome/Edge/Firefox)
- MySQL Workbench (for SQL demo)
- Command Prompt/PowerShell (for Python scripts)

**Recording Tips**:

- Speak clearly and explain what you're doing
- Show the actual code/output, don't just talk about it
- Keep energy up - you're excited about your work!
- Use mouse cursor to highlight important parts
- Pause briefly when showing results

---

## 📋 7-SECTION RECORDING SCRIPT

### 🎬 SECTION 1: PROJECT OVERVIEW (1 minute)

**What to Show**: GitHub repository and project structure

**Script**:

```
"Hi! I'm excited to show you my complete data analyst portfolio project - the PlatinumRx Hotel Management Assignment.

Let me start by showing you the GitHub repository where everything is hosted."

[Open browser to: https://github.com/srinivasan-web/Hotel-Management]

"This is my GitHub repository. You can see all the project files are organized into folders:
- SQL folder with database schemas and queries
- Python folder with data analysis scripts
- Spreadsheets folder with Excel files
- Dashboard folder with interactive visualizations
- And comprehensive documentation

The project demonstrates full-stack data analyst skills: SQL databases, Python programming, Excel analysis, and web dashboards."
```

**Visual**: Click through folders, show file structure, mention commit history

---

### 🎬 SECTION 2: SQL DATABASE DEMO (2 minutes)

**What to Show**: MySQL Workbench running queries

**Preparation**:

1. Open MySQL Workbench
2. Connect to your MySQL server
3. Have the SQL files ready

**Script**:

```
"Now let's dive into the SQL component. I built two complete databases: a Hotel Management system and a Clinic Financial system.

Let me show you the database schemas and run some complex queries."
```

**Step-by-Step Demo**:

1. **Show Hotel Schema**:

   ```
   [Open SQL/01_Hotel_Schema_Setup.sql in MySQL Workbench]
   "This is the hotel database schema with 4 tables: users, bookings, items, and booking_commercials."
   [Execute the script]
   "You can see the tables were created successfully."
   ```

2. **Show Clinic Schema**:

   ```
   [Open SQL/03_Clinic_Schema_Setup.sql]
   "Here's the clinic database with sales and expenses tables."
   [Execute the script]
   ```

3. **Run Hotel Queries**:

   ```
   [Open SQL/02_Hotel_Queries.sql]
   "Now let me run some business intelligence queries. This first query shows revenue by guest."
   [Execute Query 1 - highlight the JOIN and GROUP BY]
   "See how it combines data from multiple tables using JOINs and aggregates revenue."

   "This query shows booking summaries with window functions."
   [Execute Query 5 - show the RANK() OVER clause]
   ```

4. **Run Clinic Queries**:
   ```
   [Open SQL/04_Clinic_Queries.sql]
   "Now for the clinic data - this shows profit/loss analysis."
   [Execute one of the financial queries]
   "The query calculates profit margins and identifies profitable channels."
   ```

**Visual**: Show query results, explain what each query does, highlight complex SQL features

---

### 🎬 SECTION 3: EXCEL ANALYSIS (1 minute)

**What to Show**: Google Sheets with formulas

**Script**:

```
"Next, let's look at the Excel component. I created a ticket analysis spreadsheet with advanced formulas."
```

**Step-by-Step Demo**:

1. **Open Google Sheets**:

   ```
   [Open: https://docs.google.com/spreadsheets/d/1oNXMa01uLzADRlXZQ8Hs1waXQNjaIPHh9X-MqSPdfRw/edit?usp=sharing]
   "Here's my Google Sheets version of the Excel file."
   ```

2. **Show Ticket Sheet**:

   ```
   "The ticket sheet contains ticket data with IDs, dates, and status."
   ```

3. **Show Feedbacks Sheet**:
   ```
   "The feedbacks sheet demonstrates advanced Excel formulas."
   [Click on cell C2] "This VLOOKUP formula retrieves dates from the ticket sheet."
   [Click on cell E2] "This IF formula checks if tickets were resolved on the same day."
   [Click on cell F2] "Another IF formula checks if they were resolved in the same hour."
   [Click on summary cell] "And this COUNTIFS formula counts how many tickets were resolved same-day AND same-hour."
   ```

**Visual**: Click on formula cells, show the formula bar, explain what each formula does

---

### 🎬 SECTION 4: PYTHON SCRIPTS (2 minutes)

**What to Show**: Command line running Python scripts

**Preparation**:

1. Open Command Prompt or PowerShell
2. Navigate to project directory
3. Have Python installed

**Script**:

```
"Now for the Python programming component. I wrote three production-quality scripts demonstrating different data analysis techniques."
```

**Step-by-Step Demo**:

1. **Navigate to Project**:

   ```
   [Open Command Prompt]
   cd h:\hotel-menagement\PlatinumRx_Assignment
   "Let me navigate to the project directory."
   ```

2. **Run Time Converter**:

   ```
   python Python/01_Time_Converter.py
   "First script: A time converter utility function."
   [Show output] "You can see it converts minutes to hours and minutes format, with 9 test cases all passing."
   ```

3. **Run Remove Duplicates**:

   ```
   python Python/02_Remove_Duplicates.py
   "Second script: Three different algorithms for removing duplicates from strings."
   [Show output] "It demonstrates O(n²) vs O(n) performance - the Dict Order method is fastest."
   ```

4. **Run Data Analysis**:
   ```
   python Python/03_Data_Analysis.py
   "Third script: A complete data analysis class with aggregation, filtering, and export capabilities."
   [Show output] "It processes hotel and clinic data, generates reports, and exports to JSON and CSV files."
   ```

**Visual**: Type commands, show output, explain what each script does and why it's useful

---

### 🎬 SECTION 5: INTERACTIVE DASHBOARDS (2 minutes)

**What to Show**: Web browser with Chart.js visualizations

**Preparation**:

1. Open web browser
2. Have dashboard files ready

**Script**:

```
"Finally, let's see the interactive dashboards I created using Chart.js. These turn the data into beautiful visualizations."
```

**Step-by-Step Demo**:

1. **Open Hotel Dashboard**:

   ```
   [Open Dashboard/Hotel_Dashboard.html in browser]
   "Here's the Hotel Management Dashboard with 4 interactive charts."
   [Hover over charts] "You can see bookings by guest, revenue trends, and key metrics."
   ```

2. **Open Clinic Dashboard**:

   ```
   [Open Dashboard/Clinic_Dashboard.html in browser]
   "And here's the Clinic Financial Dashboard."
   [Hover over charts] "It shows revenue by channel, profit/loss analysis, and financial trends."
   ```

3. **Show Interactivity**:
   ```
   "Both dashboards are fully interactive - hover over data points to see details, and they're responsive for mobile viewing."
   ```

**Visual**: Open both HTML files, click around, show hover effects, mention Chart.js library

---

### 🎬 SECTION 6: DOCUMENTATION (1 minute)

**What to Show**: README and documentation files

**Script**:

```
"The project includes comprehensive documentation for reproducibility and professional presentation."
```

**Step-by-Step Demo**:

1. **Show README**:

   ```
   [Open README.md on GitHub or locally]
   "The README provides complete project overview, setup instructions, and portfolio value."
   ```

2. **Show HOW_TO_RUN**:

   ```
   [Open HOW_TO_RUN.md]
   "This detailed guide shows exactly how to run every component."
   ```

3. **Show Other Docs**:
   ```
   "There are also submission guides, completion summaries, and deployment documentation."
   ```

**Visual**: Scroll through documentation, highlight key sections

---

### 🎬 SECTION 7: DEPLOYMENT & VERSION CONTROL (1 minute)

**What to Show**: Git history and deployment

**Script**:

```
"Finally, let me show you the professional deployment and version control."
```

**Step-by-Step Demo**:

1. **Show Git Commits**:

   ```
   [On GitHub, click Commits tab]
   "You can see the 7 commits showing the development process."
   ```

2. **Show Project Structure**:

   ```
   "Everything is properly organized and publicly accessible."
   ```

3. **Final Summary**:

   ```
   "This project demonstrates end-to-end data analyst capabilities: from database design to web visualization, with clean code and comprehensive documentation.

   Thank you for watching!"
   ```

**Visual**: Show commit history, file structure, final project stats

---

## 🎥 RECORDING TECHNICAL SETUP

### Option 1: Windows Game Bar (Easiest)

1. **Start Recording**:
   - Press `Windows Key + G`
   - Click record button (or use Xbox app)
   - Record full screen or specific window

2. **Stop Recording**:
   - Press `Windows Key + G` again
   - Save video to Videos/Captures folder

### Option 2: OBS Studio (More Control)

1. **Download**: https://obsproject.com/
2. **Setup**: Select "Display Capture" for full screen
3. **Record**: Start/stop with hotkeys
4. **Export**: Save as MP4

### Audio Setup

- Use computer microphone
- Test audio levels before recording
- Speak clearly, explain as you go

---

## 📤 UPLOAD TO GOOGLE DRIVE

1. **Go to Google Drive**: https://drive.google.com/
2. **Upload Video**: Click "New" → "File upload"
3. **Wait for Upload**: Large files may take time
4. **Share Settings**:
   - Right-click video → "Share"
   - Change to: "Anyone with the link"
   - Set permission: "Viewer"
   - Copy the link

**Your link format**:

```
https://drive.google.com/file/d/[YOUR_VIDEO_ID]/view?usp=sharing
```

---

## ✅ FINAL CHECKLIST

**Before Recording**:

- [ ] Test all components work (SQL, Python, Dashboards)
- [ ] Have MySQL Workbench ready
- [ ] Have browser windows prepared
- [ ] Test microphone audio
- [ ] Clear desk/background

**During Recording**:

- [ ] Speak clearly and explain what you're doing
- [ ] Show actual code and results
- [ ] Highlight important parts with mouse
- [ ] Keep energy up and smile!

**After Recording**:

- [ ] Review video for quality
- [ ] Upload to Google Drive
- [ ] Test sharing link works
- [ ] Get the shareable link

---

## 💡 RECORDING TIPS

**Do's**:

- ✅ Explain what you're showing as you go
- ✅ Show real results and outputs
- ✅ Highlight complex parts (SQL joins, Python algorithms)
- ✅ Demonstrate interactivity (dashboard hovers, formula clicks)
- ✅ Mention why you chose certain approaches

**Don'ts**:

- ❌ Don't read directly from screen
- ❌ Don't rush through sections
- ❌ Don't show error messages
- ❌ Don't have background noise

**Timing**:

- Keep total under 10 minutes
- Practice once before recording
- Have water ready (dry mouth!)

---

## 🎯 WHAT TO EMPHASIZE

**Technical Skills**:

- SQL: Complex queries, JOINs, window functions
- Python: OOP, algorithms, data processing
- Excel: Advanced formulas, cross-sheet references
- Web: Chart.js, responsive design, interactivity

**Professional Skills**:

- Clean code organization
- Comprehensive documentation
- Version control (Git)
- Project structure and deployment

**Business Value**:

- Real-world business problems
- Data-driven insights
- Professional presentation
- Reproducible results

---

## 🚀 FINAL SUBMISSION

Once recorded and uploaded, your complete submission will be:

```
========================================
SUBMISSION - PlatinumRx Assignment
========================================

GitHub Repository:
https://github.com/srinivasan-web/Hotel-Management

Google Sheets (Spreadsheet):
https://docs.google.com/spreadsheets/d/1oNXMa01uLzADRlXZQ8Hs1waXQNjaIPHh9X-MqSPdfRw/edit?usp=sharing

Screen Recording (GitHub Drive):
[Your video link here]

========================================
```

---

## 💪 YOU'VE GOT THIS!

**Remember**: This is your chance to shine! Show your technical skills, explain your thought process, and demonstrate why you're a great data analyst candidate.

**Good luck! 🎬✨**
