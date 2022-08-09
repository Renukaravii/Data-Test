import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._


object bonus {
  def main(args: Array[String]): Unit = {
    val g = SparkSession.builder().appName("json").master("local").getOrCreate()
    val p =g.read.option("header",true).csv("C:/Users/z032359/Desktop/iii/schema/hive.csv")
    val l =g.read.option("header",true).csv("C:/Users/z032359/Desktop/iii/schema/hive.csv")
    l.show()

    p.join(l,p("empid") === l("managerid"),"right").select(l("empid"),l("empname"),p("empname").alias("managername")).show()






  }}
