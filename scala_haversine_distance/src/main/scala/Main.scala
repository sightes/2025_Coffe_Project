object Haversine {
  val EarthRadiusKm = 6371.0 // Radio promedio de la Tierra en kilómetros

  def haversine(lat1: Double, lon1: Double, lat2: Double, lon2: Double): Double = {
    val lat1Rad = Math.toRadians(lat1)
    val lon1Rad = Math.toRadians(lon1)
    val lat2Rad = Math.toRadians(lat2)
    val lon2Rad = Math.toRadians(lon2)

    val dLat = lat2Rad - lat1Rad
    val dLon = lon2Rad - lon1Rad

    val a = Math.pow(Math.sin(dLat / 2), 2) +
      Math.cos(lat1Rad) * Math.cos(lat2Rad) * Math.pow(Math.sin(dLon / 2), 2)

    val c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a))

    EarthRadiusKm * c
  }

  def main(args: Array[String]): Unit = {
    // Ejemplo: Coordenadas de Nueva York y Londres
    val lat1 = 40.7128 // Latitud de Nueva York
    val lon1 = -74.0060 // Longitud de Nueva York
    val lat2 = 51.5074 // Latitud de Londres
    val lon2 = -0.1278 // Longitud de Londres

    val distancia = haversine(lat1, lon1, lat2, lon2)
    println(f"La distancia entre Nueva York y Londres es: $distancia%.2f km")
  }
}