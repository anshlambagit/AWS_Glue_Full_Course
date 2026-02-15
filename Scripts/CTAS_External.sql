CREATE TABLE IF NOT EXISTS expensive_orders
  WITH (format='parquet', external_location='s3://buckettutorialansh/expensive_orders/') AS
SELECT
  *
FROM
  orders
WHERE
  item = 'Monitor'