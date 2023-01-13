SELECT name 
FROM Customer
WHERE IFNULL(Customer.referee_id, 1) <> 2
