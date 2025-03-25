from influxdb_client import InfluxDBClient
import time
import serial
influxdb_url ="http://localhost:8086"
influxdb_token ="MDuMYtD6M9miZFBlapuN9OlkDDATv2xC-_yEa8SWVLBVOqJY-lAg0cbhXJNJidzij4ci-X_MStSclY7dwOw_NQ=="
influxdb_org = "test"
influxdb_bucket = "dust"

serial_port = "COM10"
baudrate = 9600
timeout = 2

client = InfluxDBClient(url=influxdb_url, token = influxdb_token, org = influxdb_org)

client = InfluxDBClient(url=influxdb_url, token = influxdb_token, org = influxdb_org)
write_api = client.write_api()

try:
    ser = serial.Serial(serial_port, baudrate, timeout = timeout)
    print(f"Connected to {serial_port} at {baudrate} baud")
except serial.SerialException:
    print("Failed to connect to serial port.")
    exit()

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print(f"Received: {line}")

            if "=" in line:
                key, value = line.split("=")
                try:
                    value = float(value)
                    data = f"sensor_data,device=arduino {key}={value}"
                    write_api.write(bucket=influxdb_bucket, record=data)
                    print(f"Data written to InfluxDB: {key}={value}")

                except ValueError:
                    print("Invalid data format")

            time.sleep(1)

except KeyboardInterrupt:
    print("Stopping data collection")

finally:
    ser.close()
