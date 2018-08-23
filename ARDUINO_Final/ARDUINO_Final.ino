#include <Servo.h>
Servo camara;
// Pines de entrada para CI L298
#define MOTOR_CTL1  8  // I1 Input 1
#define MOTOR_CTL2  10  // I2 Input 1
#define MOTOR_PWM1  9 // EA Enable A

#define MOTOR_CTR1  5   // I1 Input 2
#define MOTOR_PWM2  6  //  EA Enable B
#define MOTOR_CTR2  7 //    I2 Input 2 

#define MOTOR_DIR_FORWARD  0   // Adelante
#define MOTOR_DIR_BACKWARD  1  // Atras
#define MOTOR_DIR_RIGHT  0   // Adelante
#define MOTOR_DIR_LEFT  1  // Atras

String inputString = "";  // string vacio para recibir mensajes en el serial     
boolean stringComplete = false; //booleano para comprobar si el mensaje fue recibido completamente
String c; // mensaje completo sin caracteres de inicio/final
String d; // primer caracter del mensaje recibido
String msj; //mensaje para ser enviado
int Status = 5; //Estado inicial de motores

int acelx, acely, acelz;  //aceleraciones por eje


void setup(){
   // Configuracion de pines para control del motor   
   // Control de sentido de giro del motor 1
   pinMode(MOTOR_CTL1,OUTPUT);
   pinMode(MOTOR_CTL2,OUTPUT);
   // Control de velocidad
   pinMode(MOTOR_PWM1,OUTPUT);
   // Control de sentido de giro del motor 2
   pinMode(MOTOR_CTR1,OUTPUT);
   pinMode(MOTOR_CTR2,OUTPUT);
   pinMode(MOTOR_PWM2,OUTPUT);
   Serial.begin(115200); // inicializacion serial
   inputString.reserve(200); //reserva de memoria para recibir el mensaje
   setSpeed(255);   // velocidad de movimiento del robot 
   camara.attach(12);   //anclaje del servo de la camara al pin correspondiente
}

// Control de velocidad mediante PWM
// 0 < motor_speed < 255
void setSpeed(byte motor_speed)
{
  analogWrite(MOTOR_PWM1, motor_speed);
  analogWrite(MOTOR_PWM2, motor_speed);
}

//pines a activar para giro derecha/izquierda
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


// pines a activar para movimiento adelante/atras
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
   digitalWrite(MOTOR_CTL1,HIGH);
   digitalWrite(MOTOR_CTL2,HIGH);
   digitalWrite(MOTOR_CTR1,HIGH);
   digitalWrite(MOTOR_CTR2,HIGH);
}

// Motor libre
void motorFree()
{
   digitalWrite(MOTOR_CTL1,LOW);
   digitalWrite(MOTOR_CTL2,LOW);
   digitalWrite(MOTOR_CTR1,LOW);
   digitalWrite(MOTOR_CTR2,LOW);
}

//programa principal: None -> None
// si se ha recibido un string a travez del puerto serial, lo analiza y decide la accion a tomar segun el mensaje correspondiente
// para el movimiento de los motores se liberan los motores durante un tiempo corto, para no forzar el movimiento
void loop(){ 
  if (stringComplete){    
    c = inputString.substring(0,3);  //se toma el string sin el ultimo caracter (strings permitidos solo tienen 4 caracteres)
    d = inputString.substring(0,1);  //se toma la primera letra del string para el caso especial del movimiento del servo de la camara
    
    if (c=="Fwd"){
      motorFree();
      delay(300);
      motorMove(MOTOR_DIR_FORWARD);
      Status = 8;
    }
    else if (c=="Bwd"){
      motorFree();
      delay(300);
      motorMove(MOTOR_DIR_BACKWARD);
      Status = 2;
    }
    else if(c=="Lef"){
      motorFree();
      delay(300);
      turnAngle(MOTOR_DIR_LEFT);
      Status = 4;
    }
    else if(c=="Rit"){
      motorFree();
      delay(300);
      turnAngle(MOTOR_DIR_RIGHT);
      Status = 6;
    }
    else if(c=="Sto"){
      motorStop();
      Status = 5;
    }    
    else if(d=="c"){      
      camara.write(c.substring(1,3).toInt()*10);
    }    
    else if(c == "Ser"){      
      //Acelerometro      
      acelx = analogRead(0);
      acelx = analogRead(0);      
      acely = analogRead(1); 
      acely = analogRead(1);      
      acelz = analogRead(2);      
      acelz = analogRead(2);           
      //temperatura      
      int tempC;
      tempC = analogRead(3);      
      msj = '[' + String(acelx) + ';' + String(acely) + ';' + String(acelz) + '/' + String(Status) + '/' + String(tempC) + ']' ; 
      Serial.print(msj);      
    }
    else { //si el string no es reconocido, se descarta y se espera por el siguiente
      inputString = "";
      c = "";
      stringComplete = false;       
    }
    inputString = ""; //luego de haber actuado en funcion al string, se elimina para recibir uno nuevo
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

