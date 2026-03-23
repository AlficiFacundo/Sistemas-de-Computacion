void setup() {
  Serial.begin(115200);

  // Configurar la frecuencia
  setCpuFrequencyMhz(160);
  Serial.print("Frecuencia de CPU configurada: ");
  Serial.print(getCpuFrequencyMhz());
  Serial.println(" MHz");

  unsigned long inicio = millis();

  // Bucle
  volatile unsigned long resultado = 0;
  for (unsigned long i = 1; i <= 53000000; i++) {
    resultado += i ^ (i % 123);
  }

  unsigned long fin = millis();
  unsigned long tiempo = fin - inicio;

  Serial.print("Resultado final: ");
  Serial.println(resultado);
  Serial.print("Tiempo de ejecución: ");
  Serial.print(tiempo / 1000.0);
  Serial.println(" segundos");
}

void loop() {
  // No se usa
}