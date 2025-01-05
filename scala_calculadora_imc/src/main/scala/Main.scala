import scala.io.StdIn.readLine

object IMCCalculator {
  def main(args: Array[String]): Unit = {
    println("=== Calculadora de IMC ===")

    // Leer peso del usuario
    print("Introduce tu peso (kg): ")
    val peso = try {
      readLine().toDouble
    } catch {
      case _: NumberFormatException =>
        println("Por favor, introduce un número válido para el peso.")
        return
    }

    // Leer altura del usuario
    print("Introduce tu altura (m): ")
    val altura = try {
      readLine().toDouble
    } catch {
      case _: NumberFormatException =>
        println("Por favor, introduce un número válido para la altura.")
        return
    }

    if (altura <= 0 || peso <= 0) {
      println("El peso y la altura deben ser números positivos.")
      return
    }

    // Calcular el IMC
    val imc = peso / (altura * altura)
    println(f"Tu IMC es: $imc%.2f")

    // Clasificar el IMC
    val categoria = if (imc < 18.5) {
      "Bajo peso"
    } else if (imc < 24.9) {
      "Peso normal"
    } else if (imc < 29.9) {
      "Sobrepeso"
    } else {
      "Obesidad"
    }

    println(s"Clasificación: $categoria")
  }
}