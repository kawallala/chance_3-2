
String inputString = "";         // a String to hold incoming data
String a, b, c;

boolean stringComplete1 = false;  // whether the string is complete
boolean stringComplete2 = false;
boolean stringComplete3 = false;

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}

void loop() {
  // print the string when a newline arrives:
  
  if (stringComplete1 && stringComplete2 && stringComplete3 ) {
    
   Serial.println(a.substring(0,2));
   Serial.println(b.substring(0,2));
   Serial.println(c.substring(0,2));
    
    // clear the string:
    inputString = "";
    stringComplete1 = false;
    stringComplete2 = false;
    stringComplete3 = false; 
    
    
  }
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    inputString += inChar;
    // add it to the inputString:
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == ',' && stringComplete1 == false) {
      stringComplete1 = true;
      a = inputString;
      inputString = "";
      Serial.println("1");
    }
    else if (inChar == ',' && stringComplete2 == false) {
      stringComplete2 = true;
      b = inputString;
      inputString = "";
      Serial.println("2");
    }
    else if (inChar == ',' && stringComplete3 == false) {
      stringComplete3 = true;
      c = inputString;
      inputString = "";
      Serial.println("3");
    }
  }
}

