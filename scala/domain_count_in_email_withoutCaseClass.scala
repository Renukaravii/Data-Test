import scala.collection.JavaConversions._



object ghj {

  def main(args: Array[String]): Unit = {
    val email = List("abc@gmail.com",
    "123@gmail.com",
    "abcde@yahoo.com")
    val j = email.map(x => x.slice(x.indexOf("@")+1,x.indexOf(".")))

    println(j)

    println(j.groupBy(l => l).map(t => (t._1, t._2.length+" ")))

      }










}
