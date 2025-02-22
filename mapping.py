import serial
import csv
from pynput.keyboard import Controller

#serial port
ser = serial.Serial('COM3', 115200)  # do Replace 'COM3' with your Arduino port
keyboard = Controller()

fire = False
spent = False

#file to track
output_file = r"C:\Users\takoy\Documents\data123.csv"
#open file
with open(output_file, mode='w', newline='') as file:
    elapsed = 0
    writer = csv.writer(file)
    writer.writerow(["Timestamp (ms)", "State", "Reading", "Click"])  #csv headers
    try:
        while True:
            #read a line from serial
            line = ser.readline().decode('utf-8', errors='replace').strip().split(",")
            print(line)
            #format example: 10,ACTIVE,580
            if (line[1] == "ACTIVE"):
                fire = True
                #map keystroke - we choose
                if (fire and not spent):
                    keyboard.press('q')
                    keyboard.release('q')
                    writer.writerow([elapsed, line[0], line[1], 1])
                    print("pressed")
                    spent = True
                else:
                    writer.writerow([elapsed, line[0], line[1], 0])
            else:
                fire = False
                spent = True
                writer.writerow([elapsed, line[0], line[1], 0])
            file.flush()
            elapsed += 10
    except KeyboardInterrupt:
        print("File sent to: " + output_file)
        ser.close()
