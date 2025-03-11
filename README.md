//Arduino TRIG, ECHO SENSOR Test code
#define TRIG 13
#define ECHO 12 

int led_r = 7;
int led_g = 8;
void setup()
{
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(led_r, OUTPUT);
  pinMode(led_g, OUTPUT);
  pinMode(TRIG, INPUT);
  pinMode(ECHO,OUTPUT);

}

void loop()
{
  long duration, distance;
  
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  
  duration = pulseIn(ECHO, HIGH);
  
  distance = duration * 17 / 1000;
  Serial.println(duration);
  Serial.print("\nDIstance : ");
  Serial.print(distance);
  Serial.println(" Cm");
  
  digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(led_r, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(LED_BUILTIN, LOW);
  digitalWrite(led_r, LOW);
  delay(1000); // Wait for 1000 millisecond(s)
   digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(led_g, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(LED_BUILTIN, LOW);
  digitalWrite(led_g, LOW);
  delay(1000); // Wait for 1000 millisecond(s)
}
