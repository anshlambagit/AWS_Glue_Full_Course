CREATE TABLE IF NOT EXISTS expensive_orders_managed
  WITH (format='parquet') AS
SELECT
  *
FROM
  orders
WHERE
  item = 'Monitor'