#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 24
GPIO_ECHO = 23
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def ObjectDistance():
    print("Flow Line :  Checking Object Distance ........")
    try:
        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
        StartTime = time.time()
        StopTime = time.time()
        
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()
     
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()
     
        TimeElapsed = StopTime - StartTime
        distance = (TimeElapsed * 34300) / 2
        ObjDistance=distance 
        print("Flow Line :  HC-SR04 Value get")
        return ObjDistance;
    except KeyboardInterrupt:
        print("Flow Line :  HC-SR04 Measurement stopped by User...")
    except:
        print("Flow Line :  error occurred!")
    finally:
        print("Flow Line :  Checking Object Distance Complected..")

#if __name__ == "__main__":
#    var1 = ObjectDistance();
#    print(var1)