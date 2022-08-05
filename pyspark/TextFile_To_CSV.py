import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._
object hh {
  def main(args : Array[String]): Unit = {
    val g = SparkSession.builder().appName("json").master("local").getOrCreate()
    val df_in=g.read.option("multiLine","true").text("C:/Users/z032359/Desktop/iii/schema/input.txt")

    val newDF = df_in.withColumn("value", trim(col("value")))
    newDF.show(truncate=false)
    val comma = (s:String) => {
       s.replaceAll(" ",",")
    }
    val f = udf(comma)

    val df = newDF.withColumn("newCol", f(newDF("value"))).drop("value")
    df.show(truncate=false)
    val c2 = (s:String) => {
       s.replaceAll(",,",",")
    }
    val comma2 = udf(c2)

    val df1 = df.withColumn("newCol1", comma2(df("newCol"))).drop("newCol")
    df1.show(truncate=false)
    df1.write.csv("C:/Users/z032359/Desktop/iii/schema/in1.csv")


  }
}
