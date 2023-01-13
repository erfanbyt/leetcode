SELECT s.name 
FROM SalesPerson as s
WHERE s.name not in (
    SELECT s.name
    FROM Orders AS o
    INNER JOIN Company c ON c.com_id = o.com_id
    LEFT JOIN SalesPerson s on s.sales_id = o.sales_id
    WHERE c.name LIKE 'RED')
