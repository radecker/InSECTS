#include <Servo.h>
Servo myservo;  // create servo object to control a servo

String serial_in;
const uint8_t led_pin = 8;
static uint8_t temp_sensors[] = {A0, A1};
static uint8_t num_temp_sensors = 2;
static unsigned long TELEMETRY_PERIOD = 1000; // 1000 ms default between telemetry grabs
int fullposition = 0; // servo position angles
int halfposition = 90;
int closeposition = 180;
int currentservopostion = 180;

double getTempData(uint8_t sensor_id);
void sendTelemetry();
void runCommand(String serial);

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(led_pin, OUTPUT);
  myservo.attach(9); // attaches the servo on pin 9 to the servo object
  myservo.write(closeposition); // initial servo position
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

  if(cmd == 0)  // Config Parameters
  {
//    Serial.println(args.substring(0,4));
    double freq = args.substring(0,4).toDouble();
    TELEMETRY_PERIOD = (1.0/freq)*1000; // convert freq to period in millis
  }
  if(cmd == 1)  // SetServoPosition
  {
    String pos = args.substring(0,4);
    if (pos == "full")
    {
      myservo.write(fullposition);
      currentservopostion = 0;
    }
    else if (pos == "half")
    {
      myservo.write(halfposition);
      currentservopostion = 90;
    }
    else if (pos == "clse")
    {
      myservo.write(closeposition);
      currentservopostion = 180;
    }
    
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
  // TODO: Finish implementation
  static double temp = 0;
  for(int i = 0; i < num_temp_sensors; i++){
    temp = getTempData(temp_sensors[i]);
    String serial_data = "1," + String(i) + "," + String(temp, 2);
    // serial_data = serial_data + ""
    // serial_data = serial_data + ;
    Serial.println(serial_data);
  }
}

double getTempData(uint8_t sensor_id)
{
  // TODO: Implement me
  static double val;
  val = analogRead(sensor_id)*(5000/1024.0);
  val = (val-110)/10; // 110 is about right for TMP35
  return val;
}
