-- ============================================================================
-- HOTEL MANAGEMENT SYSTEM - SCHEMA SETUP
-- ============================================================================
-- This script creates the hotel database schema with users, bookings, 
-- items (services/products), and the relationship table for booking commercials.
-- ============================================================================

-- Create Users Table
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Create Bookings Table
CREATE TABLE bookings (
    booking_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    booking_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create Items Table (Products/Services offered)
CREATE TABLE items (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    rate DECIMAL(10, 2) NOT NULL
);

-- Create Booking Commercials Table (Junction: links bookings to items with quantity)
CREATE TABLE booking_commercials (
    booking_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (booking_id, item_id),
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);

-- ============================================================================
-- INSERT SAMPLE DATA
-- ============================================================================

-- Insert Users
INSERT INTO users VALUES 
(1, 'Ravi'), 
(2, 'Arun');

-- Insert Bookings (November 2021)
INSERT INTO bookings VALUES
(1, 1, '2021-11-10'),
(2, 2, '2021-11-15'),
(3, 1, '2021-11-20');

-- Insert Items (Services with rates)
INSERT INTO items VALUES
(1, 'Room', 500.00),
(2, 'Food', 200.00),
(3, 'Laundry', 100.00);

-- Insert Booking Commercials (Quantities of items booked)
INSERT INTO booking_commercials VALUES
(1, 1, 2),  -- Booking 1: 2 Rooms
(1, 2, 3),  -- Booking 1: 3 Foods
(2, 1, 1),  -- Booking 2: 1 Room
(3, 1, 1),  -- Booking 3: 1 Room
(3, 2, 2),  -- Booking 3: 2 Foods
(3, 3, 1);  -- Booking 3: 1 Laundry

-- ============================================================================
-- VERIFICATION QUERY
-- ============================================================================
-- Run this to verify the data loaded correctly:

SELECT 'Users' AS table_name, COUNT(*) AS row_count FROM users
UNION ALL
SELECT 'Bookings', COUNT(*) FROM bookings
UNION ALL
SELECT 'Items', COUNT(*) FROM items
UNION ALL
SELECT 'Booking Commercials', COUNT(*) FROM booking_commercials;
