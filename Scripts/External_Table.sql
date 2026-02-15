CREATE EXTERNAL TABLE IF NOT EXISTS `database_tutorial`.`orders` (
  `orderid` string,
  `customer` string,
  `item` string,
  `quantity` string,
  `price` string,
  `orderdate` string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES ('field.delim' = ',')
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://buckettutorialansh/raw/'
TBLPROPERTIES ('classification' = 'csv');