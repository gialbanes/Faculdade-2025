int pot = A5;
int led = 13;
int valmed = 0;

void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Lê o valor do potenciômetro (0-1023) e o mapeia para um novo intervalo (0-100)
  valmed = map(analogRead(pot), 0, 1023, 0, 100);
  digitalWrite(led, HIGH);
  // o tempo para a próxima ação depende do meu potenciometro, diferente dos outros exercícios em que eu declarava o tempo 
  delay(valmed);
  digitalWrite(led, LOW);
  delay(pot);
  Serial.println(valmed);

}
