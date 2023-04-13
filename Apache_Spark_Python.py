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
    
   
# To collect or show? 
    # collect vs. show
    # show methods is a utility function that prints the dataframe to the console
    # count_df.show()
    # collect returns the data as a python list
    # logger.info will also show the data in the logs file??? CHeck this later
    # logger.info(count_df.collect())
