import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','INPUT_PATH','OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


# Fetching the Job Parameters
input_path_url = args['INPUT_PATH']
output_path_url = args['OUTPUT_PATH']


# Data Reading From S3
df = spark.read.format("csv")\
        .option("header",True)\
        .option("inferSchema",True)\
        .load(input_path_url)
        
# Data Writing To S3
df.write.format("parquet")\
            .mode("overwrite")\
            .option("path",output_path_url)\
            .save()


job.commit()