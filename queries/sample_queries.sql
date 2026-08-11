-- Sample SQL queries for the US Accidents dataset

-- 1. Count accidents by state
SELECT State, COUNT(*) AS accident_count
FROM accidents
GROUP BY State
ORDER BY accident_count DESC;

-- 2. Top 10 cities by number of accidents
SELECT City, State, COUNT(*) AS accident_count
FROM accidents
GROUP BY City, State
ORDER BY accident_count DESC
LIMIT 10;

-- 3. Accident severity distribution
SELECT Severity, COUNT(*) AS count
FROM accidents
GROUP BY Severity
ORDER BY Severity;

-- 4. Monthly accidents for 2019
SELECT strftime('%Y-%m', Start_Time) AS month, COUNT(*) AS accident_count
FROM accidents
WHERE Start_Time >= '2019-01-01' AND Start_Time < '2020-01-01'
GROUP BY month
ORDER BY month;

-- 5. Accidents during bad weather conditions
SELECT Weather_Condition, COUNT(*) AS accident_count
FROM accidents
WHERE Weather_Condition IS NOT NULL
GROUP BY Weather_Condition
ORDER BY accident_count DESC
LIMIT 20;
