-- ============================================================================
-- HOTEL MANAGEMENT SYSTEM - QUERIES
-- ============================================================================
-- Five key business queries for hotel analytics
-- ============================================================================

-- ============================================================================
-- Q1: LAST BOOKED ROOM (Most Recent Booking)
-- ============================================================================
-- Scenario: Show the most recent booking made
-- Result should show: booking_id, user_id, user_name, booking_date

SELECT 
    b.booking_id,
    b.user_id,
    u.name AS user_name,
    b.booking_date
FROM bookings b
JOIN users u ON b.user_id = u.user_id
ORDER BY b.booking_date DESC
LIMIT 1;

-- ============================================================================
-- Q2: BILLING IN NOVEMBER
-- ============================================================================
-- Scenario: Calculate total bill for each booking in November 2021
-- Logic: For each booking, sum(quantity * rate) for all items in that booking
-- Filter by: bookings in November only

SELECT 
    b.booking_id,
    u.name AS user_name,
    b.booking_date,
    SUM(bc.quantity * i.rate) AS total_bill
FROM bookings b
JOIN users u ON b.user_id = u.user_id
JOIN booking_commercials bc ON b.booking_id = bc.booking_id
JOIN items i ON bc.item_id = i.item_id
WHERE MONTH(b.booking_date) = 11 AND YEAR(b.booking_date) = 2021
GROUP BY b.booking_id, u.name, b.booking_date
ORDER BY b.booking_date;

-- ============================================================================
-- Q3: BILLS GREATER THAN 1000
-- ============================================================================
-- Scenario: Find all bookings with total bill amount exceeding 1000
-- Logic: GROUP & aggregate, then HAVING to filter aggregated results

SELECT 
    b.booking_id,
    u.name AS user_name,
    b.booking_date,
    SUM(bc.quantity * i.rate) AS total_bill
FROM bookings b
JOIN users u ON b.user_id = u.user_id
JOIN booking_commercials bc ON b.booking_id = bc.booking_id
JOIN items i ON bc.item_id = i.item_id
GROUP BY b.booking_id, u.name, b.booking_date
HAVING SUM(bc.quantity * i.rate) > 1000
ORDER BY total_bill DESC;

-- ============================================================================
-- Q4: MOST ORDERED ITEM
-- ============================================================================
-- Scenario: Which item has been ordered most (by total quantity across all bookings)
-- Logic: Group by item, sum quantities, rank by total quantity

SELECT 
    i.item_id,
    i.item_name,
    i.rate,
    SUM(bc.quantity) AS total_quantity_ordered
FROM items i
JOIN booking_commercials bc ON i.item_id = bc.item_id
GROUP BY i.item_id, i.item_name, i.rate
ORDER BY total_quantity_ordered DESC;

-- ============================================================================
-- Q5: 2ND HIGHEST BILL (Using Window Functions)
-- ============================================================================
-- Scenario: Find the booking with the 2nd highest total bill amount
-- Logic: Use RANK() window function to rank bookings by total bill,
--        then filter for rank = 2

SELECT 
    b.booking_id,
    u.name AS user_name,
    b.booking_date,
    total_bill,
    bill_rank
FROM (
    SELECT 
        b.booking_id,
        b.user_id,
        b.booking_date,
        SUM(bc.quantity * i.rate) AS total_bill,
        RANK() OVER (ORDER BY SUM(bc.quantity * i.rate) DESC) AS bill_rank
    FROM bookings b
    JOIN booking_commercials bc ON b.booking_id = bc.booking_id
    JOIN items i ON bc.item_id = i.item_id
    GROUP BY b.booking_id, b.user_id, b.booking_date
) ranked_bills
JOIN users u ON ranked_bills.user_id = u.user_id
WHERE bill_rank = 2;

-- ============================================================================
-- BONUS: BOOKING SUMMARY (All bookings with full details)
-- ============================================================================
-- Shows each booking with user, date, total bill, and item breakdown

SELECT 
    b.booking_id,
    u.name AS user_name,
    b.booking_date,
    i.item_name,
    bc.quantity,
    i.rate,
    (bc.quantity * i.rate) AS item_total,
    SUM(bc.quantity * i.rate) OVER (PARTITION BY b.booking_id) AS booking_total
FROM bookings b
JOIN users u ON b.user_id = u.user_id
JOIN booking_commercials bc ON b.booking_id = bc.booking_id
JOIN items i ON bc.item_id = i.item_id
ORDER BY b.booking_id, i.item_name;
