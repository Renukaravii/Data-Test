

object kk{
  def main(args: Array[String]): Unit = {

    val k = List(
      (1,5000),
      (2,4000),
      (3,3000)
    )
    val i =  List(
      (1,"abi","teacher"),
      (2,"ammu","student"),
      (3,"appu","vp"),
      (1,"reyan","hm"))

    val result = (for {
      a <- k

      m <- i.filter(x=>x._1 == a._1)
    } yield ((m._2,a._2)))
    val b = result
    //println(b)
    val u = b.filter(_._2>4500)
    println(u)



  }}
