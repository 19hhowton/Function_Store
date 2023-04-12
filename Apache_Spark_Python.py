### This is how you can check your configurations worked as described in local spark.conf file ###
# create a lib.utils and spark.conf to set up non-hard coded SparkConf
# no need for from pyspark import SparkConf

from pyspark.sql import *
from lib.logger import Log4J
from lib.utils import get_spark_app_config

if __name__ == "__main__":

    # conf is SparkConf object
    conf = get_spark_app_config()
    
    # pass SparkConf object to .config method for your SparkSession object
    spark = SparkSession.builder \
        .config(conf=conf) \
        .getOrCreate()

    # logging errors
    logger = Log4J(spark)

    # push message
    logger.info("Starting HelloSpark")

    ### This is how you can check your configurations worked as described in local spark.conf file ###
    # read all spark configs using the below
    conf_out = spark.sparkContext.getConf()
    # print a debug string
    logger.info(conf_out.toDebugString())

    logger.info("Ending HelloSpark")
    # spark.stop()
