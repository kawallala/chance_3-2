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

int v=255; //velocidad

String inputString = "";       
boolean stringComplete = false;
String c;
String msj; //mensaje pi
int Status = 5; //Estado de motores

int acelx, acely, acelz;  //aceleraciones por eje

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
   Serial.begin(115200);
   
   //
   inputString.reserve(200);
   
   
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
      //Serial.println("Fd");
      Status = 8;
    }
    else if (c=="Bd"){
      motorFree();
      delay(100);
      motorMove(MOTOR_DIR_BACKWARD);
      //Serial.println("Bd");
      Status = 2;
    }
    else if(c=="Lf"){
      motorFree();
      delay(100);
      turnAngle(MOTOR_DIR_LEFT);
      //Serial.println("Lf");
      Status = 4;
    }
    else if(c=="Rt"){
      motorFree();
      delay(100);
      turnAngle(MOTOR_DIR_RIGHT);
      //Serial.println("Rt");
      Status = 6;
    }
    else if(c=="St"){
      motorStop();  
      //Serial.println("St");
      Status = 5;
    }
    else if(c == "Se"){
      
       //Acelerometro
      
      acelx = analogRead(0);
      acelx = analogRead(0);      
      acely = analogRead(1); 
      acely = analogRead(1);      
      acelz = analogRead(2);      
      acelz = analogRead(2);           
      //temperatura      
      int tempC; String temp;
      tempC = analogRead(3);
      
      msj = '[' + String(acelx) + ';' + String(acely) + ';' + String(acelz) + '/' + String(Status) + '/' + String(tempC) + ']' ; 
      Serial.print(msj); 
      
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

