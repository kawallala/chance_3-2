
String inputString = "";         // a String to hold incoming data
String a, b, c;

boolean stringComplete = false;  // whether the string is complete

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}

void loop() {
  // print the string when a newline arrives:
  
  if (stringComplete) {
    
   Serial.println(inputString.substring(0,2));
   Serial.println(inputString.substring(3,5));
   Serial.println(inputString.substring(6,8));
    
    // clear the string:
    inputString = "";
    stringComplete = false;
    
  }
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    
    char inChar = (char)Serial.read();
    inputString += inChar;
    
    if (inChar == '.'){
      
      stringComplete = true;
      
    }
  }
}

