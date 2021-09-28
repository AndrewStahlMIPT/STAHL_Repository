import RPi.GPIO as GPIO
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3

def decimal2binary(i):
    return [int(elem) for elem in bin(i)[2:].zfill(bits)]

def bin2dac(i): 
     signal = decimal2binary(i)
     GPIO.output(dac, signal)
     return signal   

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)



try:
    while True:
        for i in range(0,255):
            bin2dac(i)
            time.sleep(0.005)
            signal = bicn2dac(i)
            voltage = i / levels * maxVoltage
            print("Ti vvel {:^3} -> {}, vihodnoe napryazenie = {:.2f}".format(i, signal, voltage))
        for i in range(255,0,-1):
            bin2dac(i)
            time.sleep(0.005)
            signal = bin2dac(i)
            voltage = i / levels * maxVoltage
            print("Ti vvel {:^3} -> {}, vihodnoe napryazenie = {:.2f}".format(i, signal, voltage))

              

except KeyboardInterrupt:
    print("programma ostanovlena klavoy")
else:
    print("Nikakix isklucheniy")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")