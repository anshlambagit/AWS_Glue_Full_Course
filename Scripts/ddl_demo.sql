CREATE EXTERNAL TABLE IF NOT EXISTS `demodb`.`newtable`
LOCATION 's3://anshbucket2026/processed/'
TBLPROPERTIES ('table_type' = 'DELTA');