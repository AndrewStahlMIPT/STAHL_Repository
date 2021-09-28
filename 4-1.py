import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3

def decimal2binary(value):
    return [int(elem) for elem in bin(value)[2:].zfill(bits)]

def bin2dac(value): 
     signal = decimal2binary(value)
     GPIO.output(dac, signal)
     return signal   

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)



try:
    while True:
        inputstr = input("Enter a value between 0 and 255 (press 'q' to exit the program)")
        
        if inputstr .isdigit():
            value = int(inputstr)
            if value >= levels:
                print("The chislo ne podhodit. Vvedi ot 0 do 255")
                continue

            signal = bin2dac(value)
            voltage = value / levels * maxVoltage
            print("Ti vvel {:^3} -> {}, vihodnoe napryazenie = {:.2f}".format(value, signal, voltage))

        elif inputstr == 'q':
            break
        else:
            print("The chislo ne podhodit. Vvedi ot 0 do 255")
            continue

except KeyboardInterrupt:
    print("programma ostanovlena klavoy")
else:
    print("Nikakix isklucheniy")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")