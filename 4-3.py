import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
p = GPIO.PWM(22, 1000)

p.start(0) 
try:
    while True:
        input_str = input("Enter a duty cycle from 0% to 100% ('q' to skipnyt') >> ")
        if input_str == 'q':
            break
        elif input_str.isdigit() and int(input_str) <= 100:
            value = int(input_str)
            p.ChangeDutyCycle(value)
        else:
            print("Ne to chislo. ot 0 do 100")
            continue
finally:
    p.stop()
    print("\nPWM has stopped")
    GPIO.cleanup()
    print("Everything is cleaned up")
    