-- ============================================================================
-- CLINIC MANAGEMENT SYSTEM - SCHEMA SETUP
-- ============================================================================
-- This script creates the clinic database with sales (by channel) 
-- and expenses tables for profit/loss analysis.
-- ============================================================================

-- Create Clinic Sales Table
CREATE TABLE clinic_sales (
    sale_id INT PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL,
    sales_channel VARCHAR(50) NOT NULL,
    sale_date DATE NOT NULL
);

-- Create Expenses Table
CREATE TABLE expenses (
    expense_id INT PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL,
    expense_date DATE NOT NULL
);

-- ============================================================================
-- INSERT SAMPLE DATA
-- ============================================================================

-- Insert Sales Data (November 2021, multiple channels)
INSERT INTO clinic_sales VALUES
(1, 5000.00, 'Online', '2021-11-01'),
(2, 3000.00, 'Offline', '2021-11-02'),
(3, 4500.00, 'Online', '2021-11-05'),
(4, 2000.00, 'Offline', '2021-11-08'),
(5, 6000.00, 'Online', '2021-11-10'),
(6, 3500.00, 'Offline', '2021-11-15'),
(7, 5500.00, 'Online', '2021-11-18'),
(8, 2500.00, 'Offline', '2021-11-22');

-- Insert Expenses Data (November 2021)
INSERT INTO expenses VALUES
(1, 2000.00, '2021-11-01'),
(2, 1000.00, '2021-11-02'),
(3, 1500.00, '2021-11-05'),
(4, 1200.00, '2021-11-08'),
(5, 2500.00, '2021-11-10'),
(6, 800.00, '2021-11-15'),
(7, 1800.00, '2021-11-18'),
(8, 900.00, '2021-11-22');

-- ============================================================================
-- VERIFICATION QUERY
-- ============================================================================
-- Run this to verify the data loaded correctly:

SELECT 'Clinic Sales' AS table_name, COUNT(*) AS row_count FROM clinic_sales
UNION ALL
SELECT 'Expenses', COUNT(*) FROM expenses;
