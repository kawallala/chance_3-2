/*
Control de motores de CC con CI L298



*/
// Pines de entrada para CI L298
#define MOTOR_CTL1  8  // I1 Input 1
#define MOTOR_CTL2  10  // I2 Input 1
#define MOTOR_PWM  9 // EA Enable A

#define MOTOR_CTR1  5   // I1 Input 2
#define MOTOR_PWM1  6  //  
#define MOTOR_CTR2  7 //    I2 Input 2

 

#define MOTOR_DIR_FORWARD  0   // Adelante
#define MOTOR_DIR_BACKWARD  1  // Atras

#define MOTOR_DIR_RIGHT  0   // Adelante
#define MOTOR_DIR_LEFT  1  // Atras
int v=255;

String inputString = "";       
boolean stringComplete = false;
String c;

int x, y, z;

void setup(){
   // Configuracion de pines para control del motor
   
   // Control de sentido de giro
   pinMode(MOTOR_CTL1,OUTPUT);
   pinMode(MOTOR_CTL2,OUTPUT);
   // Control de velocidad
   pinMode(MOTOR_PWM,OUTPUT);

   // Control de sentido de giro del motor 2
   pinMode(MOTOR_CTR1,OUTPUT);
   pinMode(MOTOR_CTR2,OUTPUT);
   pinMode(MOTOR_PWM1,OUTPUT);
   Serial.begin(9600);
   
   //
   inputString.reserve(200);
   Serial.println('xx,yy,zz');
   
   
}

// Control de velocidad mediante PWM
// 0 < motor_speed < 255
void setSpeed(byte motor_speed)
{
  analogWrite(MOTOR_PWM, motor_speed);
  analogWrite(MOTOR_PWM1, motor_speed);

}

void turnAngle(boolean direction)
{
   switch (direction)
   {
     case MOTOR_DIR_RIGHT:
     {
       digitalWrite(MOTOR_CTL1,HIGH);
       digitalWrite(MOTOR_CTR1,HIGH);
       
       digitalWrite(MOTOR_CTL2,LOW);  
       digitalWrite(MOTOR_CTR2,LOW);  
              
     }
     break; 
          
     case MOTOR_DIR_LEFT:
     {
        digitalWrite(MOTOR_CTL1,LOW);
        digitalWrite(MOTOR_CTR1,LOW);
        
        digitalWrite(MOTOR_CTL2,HIGH); 
        digitalWrite(MOTOR_CTR2,HIGH);         
     }
     break;         
   }
}


// Cambiar el sentido de giro
void motorMove(boolean direction)
{
   switch (direction)
   {
     case MOTOR_DIR_FORWARD:
     {
       digitalWrite(MOTOR_CTL1,LOW);
       digitalWrite(MOTOR_CTR1,HIGH);
       
       digitalWrite(MOTOR_CTL2,HIGH);  
       digitalWrite(MOTOR_CTR2,LOW);  
              
     }
     break; 
          
     case MOTOR_DIR_BACKWARD:
     {
        digitalWrite(MOTOR_CTL1,HIGH);
        digitalWrite(MOTOR_CTR1,LOW);
        
        digitalWrite(MOTOR_CTL2,LOW); 
        digitalWrite(MOTOR_CTR2,HIGH);         
     }
     break;         
   }
}

// Frenar el motor
void motorStop()
{
   setSpeed(255); // Habilitar
   digitalWrite(MOTOR_CTL1,HIGH); // Frenar
   digitalWrite(MOTOR_CTL2,HIGH);
   digitalWrite(MOTOR_CTR1,HIGH);
   digitalWrite(MOTOR_CTR2,HIGH);
}

// Motor libre
void motorFree()
{
   setSpeed(255); // Habilitar
   digitalWrite(MOTOR_CTL1,LOW); // Liberar
   digitalWrite(MOTOR_CTL2,LOW);
   digitalWrite(MOTOR_CTR1,LOW);
   digitalWrite(MOTOR_CTR2,LOW);
}

void loop(){ 
  
  setSpeed(v);
  
  if (stringComplete){
    
    
    c = inputString.substring(0,2);
    
    if (c=="Fd"){
      motorFree();
      delay(100);
      motorMove(MOTOR_DIR_FORWARD);
      Serial.println("Fd");
    }
    else if (c=="Bd"){
      motorFree();
      delay(100);
      motorMove(MOTOR_DIR_BACKWARD);;
      Serial.println("Bd");
    }
    else if(c=="Lf"){
      motorFree();
      delay(100);
      turnAngle(MOTOR_DIR_LEFT);
      Serial.println("Lf");
    }
    else if(c=="Rt"){
      motorFree();
      delay(100);
      turnAngle(MOTOR_DIR_RIGHT);
      Serial.println("Rt");
    }
    else if(c=="St"){
      motorStop();  
      Serial.println("St");
    }
    else if(c == "AC"){
      x = analogRead(0);       // read analog input pin 0
      y = analogRead(1);       // read analog input pin 1
      z = analogRead(2);      // read analog input pin 1
      float xx= map(x,0,1023,45.0,-45.0);
      float yy= map(y,0,1023,45.0,-45.0);
      float zz= map(z,0,1023,45.0,-45.0);
      String a;
      a = '[' + String(int(xx*100)) + 'X' + ',' + String(int(yy*100)) + 'Y' + ',' + String(int(zz*100)) + 'Z' +']' ; 
      Serial.println(a);
      
    }
    else if(c == "TP"){
      int tempC; String temp;
      tempC = analogRead(A3);   
      tempC = (5.0 * tempC * 100.0)/1024.0;
      temp = '[' + String(tempC) + ']' ;
      Serial.println(temp);
    }
    
    inputString = "";
    c = "";
    stringComplete = false;
  }
  
}


void serialEvent() {
  while (Serial.available()) {
    
    char inChar = (char)Serial.read();
    inputString += inChar;
    
    if (inChar == '.'){
      
      stringComplete = true;
      
    }
  }
}

