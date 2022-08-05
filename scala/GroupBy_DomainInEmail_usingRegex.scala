object ghj {

  def main(args: Array[String]): Unit = {
    val out = new java.io.FileWriter("C:/y/output1.csv")
    val email = List("abc@gmail.com",
      "123@gmail.com",
      "abcde@yahoo.com",
      "abcde@live.com",
      "abcde@yahoo.com",
      "abcde@rediff.com")

    val regex = """(?<=@)[^.]*.[^.]*(?=\.)""".r
    val y = for {
      o <- email
      matches <- regex.findAllIn(o)
    } yield (matches)
    println(y)
    println(y.groupBy(l => l).map(t => (t._1, t._2.length + " ")))


  }
