String serial_in;
const uint8_t led_pin = 8;

// Global temp variables
static uint8_t temp_sensors[] = {A0, A1};
static double prev_temps[] = {0.0, 0.0};
static double temps[] = {0.0, 0.0};
static uint8_t num_temp_sensors = 2;

static unsigned long TELEMETRY_PERIOD = 1000; // 1000 ms default between telemetry grabs

double updateTempData(uint8_t sensor_id);
void sendTelemetry();
void runCommand(String serial);
void refreshTelemetryData();

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

  refreshTelemetryData();
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
  static double temp = 0;
  for(int i = 0; i < num_temp_sensors; i++){
    String serial_data = "1," + String(i) + "," + String(temps[i], 2);
    Serial.println(serial_data);
  }
}

void refreshTelemetryData(){
  // TODO: Include other data updates here
  updateTempData();
}

double updateTempData()
{
  for(int i = 0; i < num_temp_sensors; i++){
    temps[i] = (analogRead(temp_sensors[i])*(5000/1024.0) + prev_temps[i])/2; // Averaging filter
    temps[i] = (temps[i]-110)/10;     // 110 is magic offset for TMP35
    prev_temps[i] = temps[i];
  }
}
