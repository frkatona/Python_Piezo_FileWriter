import serial
import time

arduino = serial.Serial('COM6', 9600)  # replace 'COM6' with the port to which your Arduino is connected
time.sleep(2)  # wait for the serial connection to initialize

arduino.flushInput()

start_time = time.time()  # save the current time
with open("output.txt", "w") as file:
    while True:
        if time.time() - start_time > 5:  # if more than 5 seconds have passed
            print("5 seconds have passed. Exiting.")
            break
        try:
            line = arduino.readline().decode('utf-8').strip()  # read a line from the Arduino's serial output
            file.write(line + "\n")  # write the line to a file
        except KeyboardInterrupt:
            print("Exiting")
            break

arduino.close()
