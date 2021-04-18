import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
 
def motor(MotorPin1,MotorPin2,motion):
    # GPIO Numbering
    GPIO.setup(MotorPin1,GPIO.OUT)  # All pins as Outputs
    GPIO.setup(MotorPin2,GPIO.OUT)
    if motion=="Clockwise":
        GPIO.output(MotorPin1,GPIO.HIGH)
        GPIO.output(MotorPin2,GPIO.LOW)
    elif motion=="AntiClockwise":
        GPIO.output(MotorPin1,GPIO.LOW)
        GPIO.output(MotorPin2,GPIO.HIGH)
    elif motion=="Stop":
        GPIO.output(MotorPin1,GPIO.LOW)
        GPIO.output(MotorPin2,GPIO.LOW)
        
       
def Forward(M1P1,M1P2,M2P1,M2P2,M3P1,M3P2,M4P1,M4P2,M5P1,M5P2,M6P1,M6P2):
    print("Flow Line :  Forward......")
    try:
        motor(M1P1,M1P2,"Clockwise");#motor1
        motor(M2P1,M2P2,"Clockwise");#motor2
        motor(M3P1,M3P2,"Clockwise");#motor3
        motor(M4P1,M4P2,"Clockwise");#motor4
        motor(M5P1,M5P2,"Clockwise");#motor5
        motor(M6P1,M6P2,"Clockwise");#motor6
    except KeyboardInterrupt:
        print("Flow Line :  Keyboard exception occurred!")
    except:
        print("Flow Line :  Other error or exception occurred!")
    finally:
        print("Flow Line :  Move Forward")
        
def Backward(M1P1,M1P2,M2P1,M2P2,M3P1,M3P2,M4P1,M4P2,M5P1,M5P2,M6P1,M6P2):
    print("Flow Line :  Backward......")
    try:
        motor(M1P1,M1P2,"AntiClockwise");#motor1
        motor(M2P1,M2P2,"AntiClockwise");#motor2
        motor(M3P1,M3P2,"AntiClockwise");#motor3
        motor(M4P1,M4P2,"AntiClockwise");#motor4
        motor(M5P1,M5P2,"AntiClockwise");#motor5
        motor(M6P1,M6P2,"AntiClockwise");#motor6
    except KeyboardInterrupt:
        print("Flow Line :  Keyboard exception occurred!")
    except:
        print("Flow Line :  Other error or exception occurred!")
    finally:
        print("Flow Line :  Move Backward")
        
def TurnLeft(M1P1,M1P2,M2P1,M2P2,M3P1,M3P2,M4P1,M4P2,M5P1,M5P2,M6P1,M6P2):
    print("Flow Line :  TurnLeft......")
    try:
        motor(M1P1,M1P2,"AntiClockwise");#motor1
        motor(M2P1,M2P2,"AntiClockwise");#motor2
        motor(M3P1,M3P2,"AntiClockwise");#motor3
        motor(M4P1,M4P2,"Clockwise");#motor4
        motor(M5P1,M5P2,"Clockwise");#motor5
        motor(M6P1,M6P2,"Clockwise");#motor6
    except KeyboardInterrupt:
        print("Flow Line :  Keyboard exception occurred!")
    except:
        print("Flow Line :  Other error or exception occurred!")
    finally:
        print("Flow Line :  TurnLeft")
        
def TurnRight(M1P1,M1P2,M2P1,M2P2,M3P1,M3P2,M4P1,M4P2,M5P1,M5P2,M6P1,M6P2):
    print("Flow Line :  TurnRight......")
    try:
        motor(M1P1,M1P2,"Clockwise");#motor1
        motor(M2P1,M2P2,"Clockwise");#motor2
        motor(M3P1,M3P2,"Clockwise");#motor3
        motor(M4P1,M4P2,"AntiClockwise");#motor4
        motor(M5P1,M5P2,"AntiClockwise");#motor5
        motor(M6P1,M6P2,"AntiClockwise");#motor6
    except KeyboardInterrupt:
        print("Flow Line :  Keyboard exception occurred!")
    except:
        print("Flow Line :  Other error or exception occurred!")
    finally:
        print("Flow Line :  TurnRight")
        
def StopMotor(M1P1,M1P2,M2P1,M2P2,M3P1,M3P2,M4P1,M4P2,M5P1,M5P2,M6P1,M6P2):
    print("Flow Line :  Stop......")
    try:
        motor(M1P1,M1P2,"Stop");#motor1
        motor(M2P1,M2P2,"Stop");#motor2
        motor(M3P1,M3P2,"Stop");#motor3
        motor(M4P1,M4P2,"Stop");#motor4
        motor(M5P1,M5P2,"Stop");#motor5
        motor(M6P1,M6P2,"Stop");#motor6
    except KeyboardInterrupt:
        print("Flow Line :  Keyboard exception occurred!")
    except:
        print("Flow Line :  Other error or exception occurred!")
    finally:
        print("Flow Line :  Stop")
                
#if __name__ == "__main__":
#    try:
#        TurnRight(20,21,12,16,19,26,6,13,4,17,27,22);
#    except KeyboardInterrupt:
#        GPIO.cleanup()
#        print("stopped by User")
#    except:
#        print("Other error or exception occurred!")
#    finally:
#        print("User")
#        sleep(5) 
#        GPIO.cleanup()
        
    
