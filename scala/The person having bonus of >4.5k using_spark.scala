import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

object hh {
  def main(args : Array[String]): Unit = {
    val g = SparkSession.builder().appName("json").master("local").getOrCreate()
    val j=g.read.option("header",true).csv("C:/Users/z032359/Desktop/iii/schema/11.csv")
    val k =g.read.option("header",true).csv("C:/Users/z032359/Desktop/iii/schema/22.csv")
   j.show()
    k.show()
    j.join(k,j("id") ===  k("id"),"inner").select(j("id"),j("name"),j("position"),k("salary")).filter("salary > 4500")
      .show(false)





  }
}
