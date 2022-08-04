package newn


import scala.io.Source._
object newe {
  def main(args: Array[String]): Unit = {



    val lines = fromFile("C:/Users/z032359/Desktop/iii/schema/input.txt").mkString
   // println(lines)


    val k =lines.split ("\n").map (_.trim).mkString("\n")
    //println(k)
    val j = k.replaceAll(" ",",")
    val p = j.replaceAll(",,",",")

    println(p)








  }


}
