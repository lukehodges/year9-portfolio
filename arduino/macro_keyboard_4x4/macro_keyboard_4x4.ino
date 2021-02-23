#include <Keyboard.h>
#include <Keypad.h>

const byte numRows= 4; //number of rows on the keypad
const byte numCols= 4; //number of columns on the keypad

//keymap defines the key pressed according to the row and columns just as appears on the keypad
char keymap[numRows][numCols]=
{
{'1', '2', '3', '4'},
{'5', '6', '7', '8'},
{'9', '0', 'A', 'B'},
{'C', 'D', 'E', 'F'}
};

//Code that shows the the keypad connections to the arduino terminals
byte rowPins[numRows] = {2,3,4,5}; //Rows 0 to 3
byte colPins[numCols]= {6,7,8,9}; //Columns 0 to 3

//initializes an instance of the Keypad class
Keypad myKeypad= Keypad(makeKeymap(keymap), rowPins, colPins, numRows, numCols);

void setup()
{
Serial.begin(9600);
Keyboard.begin();
}
void one(){
  Keyboard.press(KEY_LEFT_CTRL);
  Keyboard.press(KEY_LEFT_SHIFT);
  Keyboard.press('m');
  delay(100);
  Keyboard.releaseAll();
  delay(100);
  }
void two(){
  Keyboard.press(KEY_LEFT_CTRL);
  Keyboard.press(KEY_PRESS_SHIFT);
  Keyboard.press('d');
  delay(100);
  Keyboard.releaseAll();
}
//If key is pressed, this key is stored in 'keypressed' variable
//If key is not equal to 'NO_KEY', then this key is printed out
//if count=17, then count is reset back to 0 (this means no key is pressed during the whole keypad scan process
void loop()
{
char keypressed = myKeypad.getKey();
if (keypressed != NO_KEY)
{
Serial.print(keypressed);
}
delay(100);
}
