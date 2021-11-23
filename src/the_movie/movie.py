from pyspark.sql import SparkSession, DataFrame
import pyspark.sql.functions as f


def get_spark(app_name="The Movie"):
	return SparkSession.builder.appName(app_name).enableHiveSupport().getOrCreate()


def read_data(spark: SparkSession):
	path = "./data/name.basics.csv"
	return spark.read.csv(path, sep=r';', header=True)


def find_the_oldest_soundtrack(dataframe: DataFrame):
	df_soundtrack = dataframe.filter(dataframe.primaryProfession.contains("soundtrack"))
	print(df_soundtrack.show(1))
	return df_soundtrack.select(f.min(f.col("birthYear")).alias("MAX")).limit(1).collect()[0].MAX


