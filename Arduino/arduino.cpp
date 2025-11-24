const int BATHROOM_LIGHT = 11;
const int BEDROOM_LIGHT = 12;
const int KITCHEN_LIGHT = 13;

bool blinking = false; // Variable para controlar el estado de parpadeo

void menu(){
   Serial.println("[1]. Turn on bathroom_light");
   Serial.println("[2]. Turn off bathroom_light");
   Serial.println("[3]. Turn on bedroom_light");
   Serial.println("[4]. Turn off bedroom_light");
   Serial.println("[5]. Turn on kitchen_light");
   Serial.println("[6]. Turn off kitchen_light");
   Serial.println("[7]. Turn on all lights");
   Serial.println("[8]. Turn off all lights");
   Serial.println("[9]. Blinking lights");
   Serial.println("[0]. Stop blinking");
}

void setup() {
  pinMode(BATHROOM_LIGHT, OUTPUT);
  pinMode(BEDROOM_LIGHT, OUTPUT);
  pinMode(KITCHEN_LIGHT, OUTPUT);
  Serial.begin(9600);
  menu();
}

void loop() {
  if(Serial.available() > 0){
    char opt = Serial.read();
    if (opt == '1'){
      blinking = false;
      digitalWrite(BATHROOM_LIGHT, HIGH);
    }
    if (opt == '2'){
      blinking = false;
      digitalWrite(BATHROOM_LIGHT, LOW);
    }
    
    if (opt == '3'){
      blinking = false;
      digitalWrite(BEDROOM_LIGHT, HIGH);
    }
    if (opt == '4'){
      blinking = false;
      digitalWrite(BEDROOM_LIGHT, LOW);
    }
    if (opt == '5'){
      blinking = false;
      digitalWrite(KITCHEN_LIGHT, HIGH);
    }
    if (opt == '6'){
      blinking = false;
      digitalWrite(KITCHEN_LIGHT, LOW);
    }
  
    
    if (opt == '7'){
      blinking = false;
      digitalWrite(BATHROOM_LIGHT, HIGH);
      digitalWrite(BEDROOM_LIGHT, HIGH);
      digitalWrite(KITCHEN_LIGHT, HIGH);
    }
    if (opt == '8'){
      blinking = false;
      digitalWrite(BATHROOM_LIGHT, LOW);
      digitalWrite(BEDROOM_LIGHT, LOW);
      digitalWrite(KITCHEN_LIGHT, LOW);
    }
    
    if (opt == '9'){
      blinking = true;
    }
    
    if (opt == '0'){
      blinking = false; 
      digitalWrite(BATHROOM_LIGHT, LOW);
      digitalWrite(BEDROOM_LIGHT, LOW);
      digitalWrite(KITCHEN_LIGHT, LOW);
    }
  }
  
  if(blinking){
    digitalWrite(BATHROOM_LIGHT, HIGH);
    digitalWrite(BEDROOM_LIGHT, HIGH);
    digitalWrite(KITCHEN_LIGHT, HIGH);
    delay(500);
    
    digitalWrite(BATHROOM_LIGHT, LOW);
    digitalWrite(BEDROOM_LIGHT, LOW);
    digitalWrite(KITCHEN_LIGHT, LOW);
    delay(500);
  }
}