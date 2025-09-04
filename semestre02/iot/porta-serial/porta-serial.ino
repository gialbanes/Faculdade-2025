// criação de variável 
byte valorDigitado;
int led = 13;

void setup(){
  pinMode(led, OUTPUT);
  //configuração da porta serial
 Serial.begin(9600); // porta padrão 

}

void loop()
{
  // verificação da existência da porta serial (USB)
  if(Serial.available()) {
    // Serial.read() lê o primeiro byte que está no buffer (memória) 
    valorDigitado = Serial.read();

    if(valorDigitado == 'L') {

      digitalWrite(led, HIGH);
      // essa função é o oposto Serial.read() - escreva no Serial, ou seja, envia algo 
      // para computador e se o computador estiver disponível, receberá a informação
      Serial.write(valorDigitado);
    }
  }
}