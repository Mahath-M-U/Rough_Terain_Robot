print("""\
   _______________________________________________________________________________________________________________________________________________________________
  |                                                                                                                                                               |                         
  | ██████╗  ██████╗ ██╗   ██╗ ██████╗ ██╗  ██╗        ████████╗███████╗██████╗ ██████╗  █████╗ ██╗███╗   ██╗        ██████╗  ██████╗ ██████╗  ██████╗ ████████╗  |
  | ██╔══██╗██╔═══██╗██║   ██║██╔════╝ ██║  ██║        ╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║        ██╔══██╗██╔═══██╗██╔══██╗██╔═══██╗╚══██╔══╝  |
  | ██████╔╝██║   ██║██║   ██║██║  ███╗███████║           ██║   █████╗  ██████╔╝██████╔╝███████║██║██╔██╗ ██║        ██████╔╝██║   ██║██████╔╝██║   ██║   ██║     |
  | ██╔══██╗██║   ██║██║   ██║██║   ██║██╔══██║           ██║   ██╔══╝  ██╔══██╗██╔══██╗██╔══██║██║██║╚██╗██║        ██╔══██╗██║   ██║██╔══██╗██║   ██║   ██║     |
  | ██║  ██║╚██████╔╝╚██████╔╝╚██████╔╝██║  ██║           ██║   ███████╗██║  ██║██║  ██║██║  ██║██║██║ ╚████║        ██║  ██║╚██████╔╝██████╔╝╚██████╔╝   ██║     |
  | ╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝           ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝        ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝     |
  |_______________________________________________________________________________________________________________________________________________________________|                                                                                                                                                            
                                                                                                                                      
 """)
import threading
from FirebaseFunction import *
import time
print("Flow Line :  Getting Ready.........................................")
# pip install pyfiglet



def DataReadFromFirebase():
    CaptureFiresotreChanges();
def DataWriteFromFirebase():
    while True:
        AddToFiresotreField();

if __name__ == "__main__":
    try:
        print("Flow Line :  Loading Program.....")
        DataReadthread = threading.Thread(target=DataReadFromFirebase)
        DataWritethread  = threading.Thread(target=DataWriteFromFirebase)
        # starting thread 1
        DataReadthread.start()
        # starting thread 2
        DataWritethread.start()
        # wait until thread 1 is completely executed
        DataReadthread.join()
        # wait until thread 2 is completely executed
        DataWritethread.join()
        # both threads completely executed
        print("Flow Line :  Sucessfully Load Program.")
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Flow Line :  stopped by User")
    except:
        print("Flow Line :  Other error or exception occurred!")
    finally:
        print("Flow Line :  Exiting from Code.....")
        GPIO.cleanup()
        print("Flow Line :  Sucessfully Exit from Code")