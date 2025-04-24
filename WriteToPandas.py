import serial
import csv
import re
import time

# Have this be the same as the port you are connected to the Arduino Uno with
SERIAL_PORT = 'COM6'
BAUD_RATE = 9600

# Create a CSV file and ensure there are headers
with open('temperature_log.csv', 'w', newline='') as file:
    # Connect to serial so you i can get the input stream
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Give Arduino time to reset and actually log
    #Start off the messages
    print("Logging data... Press Ctrl+C to stop.")
    #Try catch so it doesnt break if something goes wrong and so we know when to stop it
    try:
        # Establish the writer
        writer = csv.writer(file)
        writer.writerow(['Time (ms)', 'Sensor Value', 'Volts', 'Degrees C'])

        while True:
            line = ser.readline().decode('utf-8').strip()

            # Match format like: Time: 1299, Sensor Value: 123, Volts: 0.71, degrees c: 21.03
            match = re.match(r'Time: (\d+), Sensor Value: (\d+), Volts: ([\d.]+), degrees c: ([\d.]+)', line)
            if match:
                row = [int(match.group(1)), int(match.group(2)), float(match.group(3)), float(match.group(4))]
                print(row)
                writer.writerow(row)

    except KeyboardInterrupt:
        print("\nStopped logging.")
        ser.close()
