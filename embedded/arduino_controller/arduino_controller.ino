String serial_in;
const uint8_t led_pin = 8;
const uint8_t temp_in_1 = A0;
static const unsigned long TELEMETRY_PERIOD = 1000; // 1000 ms between telemetry uploads

double getTempData(uint8_t sensor_id);
void sendTelemetry();
void runCommand(String serial);

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(led_pin, OUTPUT);
}

void loop() {
  static unsigned long last_refresh_time = 0;

  // Check if commands are available and run them
  if(Serial.available())
  {
    serial_in = Serial.readString();
    runCommand(serial_in);
  }

  // Check if 1 second has passed, and if so send telemetry data
  if(millis() - last_refresh_time >= TELEMETRY_PERIOD)
  {
    last_refresh_time += TELEMETRY_PERIOD;
    sendTelemetry();
  }
  
}

void runCommand(String serial)
{
  static uint8_t cmd = serial.substring(0,1).toInt(); // Grabs just the first character
  static String args = serial.substring(2); // Grabs everything past the first comma

  if(cmd == 1)  // SetServoPosition
  {
    // TODO: IMPLEMENT ME
    digitalWrite(led_pin, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(1000);                       // wait for a second
    digitalWrite(led_pin, LOW);    // turn the LED off by making the voltage LOW
    delay(1000);
  }
  if(cmd == 2)  // SetFanSpeed
  {
    // TODO: IMPLEMENT ME
  }
  if(cmd == 3)  // SetFanState
  {
    // TODO: IMPLEMENT ME
  }
}

void sendTelemetry()
{
  // TODO: Implement me
  static double temp = 0;
  temp = getTempData(1);
  String serial_data = "1,1," + String(temp, 2);
  Serial.println(serial_data);
}

double getTempData(uint8_t sensor_id)
{
  // TODO: Implement me
  static double val;
  val = analogRead(temp_in_1)*(5000/1024.0);
  val = (val-110)/10; // 110 is about right for TMP35
  return val;
}
