



import scala.io.Source
import scala.util.parsing.json._

object mm {
  def main(args: Array[String]): Unit = {
    


    val fname = "C:/Users/z032359/Desktop/iii/schema/task.json"
    val fSource = Source.fromFile(fname)

   
    var l = 0
    var m = 0
    var n = 0
    for(line<-fSource.getLines)
    {
      if  (line.contains("Bigdata"))
        l += 1
      if  (line.contains("Development"))
        m += 1
      if  (line.contains("Testing"))
        n += 1

    }
    println("[Bigadata "+l+" ]")
    println("[Development "+m+" ]")
    println("[Testing "+n+" ]")
    fSource.close()
  }



}
