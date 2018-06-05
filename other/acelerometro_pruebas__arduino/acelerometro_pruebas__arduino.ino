int x, y, z;

void setup()
{
  Serial.begin(9600);      // sets the serial port to 9600
}

void loop()
{
  x = analogRead(0);       // read analog input pin 0
  y = analogRead(1);       // read analog input pin 1
  z = analogRead(2);       // read analog input pin 1
  String a;
  
  a = '[' + String(x) + ',' + String(y) + ',' + String(z) + ']' ; 
  
  Serial.println(a);
//  Serial.print(x);    // print the acceleration in the X axis
//  Serial.print(",");       // prints a space between the numbers
//  Serial.print(y);    // print the acceleration in the Y axis
//  Serial.print(",");       // prints a space between the numbers
//  Serial.println(z);  // print the acceleration in the Z axis
  delay(100);              // wait 100ms for next reading
}

