import threading
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from movement import *
from DH11 import *
from HCSR04 import *
from MQ2 import *


# Use a service account
cred = credentials.Certificate('/home/pi/RTR/PythonModules/FirebaseAdminSDK/rtr2021-1e400-firebase-adminsdk-c3vp6-242cb993da.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
# Create an Event for notifying main thread.
callback_done = threading.Event()

# Create a callback on_snapshot function to capture changes
def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        CallMovement();
    callback_done.set()

def CaptureFiresotreChanges():
    doc_ref = db.collection(u'RTRobot').document(u'Movement')
    # Watch the document
    doc_watch = doc_ref.on_snapshot(on_snapshot)
def ReadFiresotredocument():
    print("Flow Line :  Reading Firesotre document.......")
    doc_ref = db.collection(u'RTRobot').document(u'Movement')
    try:
        doc=doc_ref.get()
        MovementAction=doc.to_dict()
        print(MovementAction)
        return MovementAction;
    except google.cloud.exceptions.NotFound:
        print("Flow Line :  No such document..")
    except:
        print("Flow Line :  error occurred!")
    finally:
        print("Flow Line :  Read Firesotre document Complected..")
def CallMovement():
    Forward_str={'Action': 'Forward'}
    Backward_str={'Action': 'Backwards'}
    TurnLeft_str={'Action': 'Left'}
    TurnRight_str={'Action': 'Right'}
    StopMotor_str={'Action': 'Stop'}
    
    Distance_str = ObjectDistance();
    try:
        Check_str=ReadFiresotredocument();
        if Check_str == Forward_str:
            if Distance_str > 50:
                Forward(20,21,12,16,19,26,6,13,4,17,27,22);
            else:
                print("Flow Line :  Some objects block the path")
        elif Check_str == Backward_str:
            Backward(20,21,12,16,19,26,6,13,4,17,27,22);
        elif Check_str == TurnLeft_str:
            TurnLeft(20,21,12,16,19,26,6,13,4,17,27,22);
        elif Check_str == TurnRight_str:
            TurnRight(20,21,12,16,19,26,6,13,4,17,27,22);
        elif Check_str == StopMotor_str:
            StopMotor(20,21,12,16,19,26,6,13,4,17,27,22);
    except:
        print("Flow Line :  error occurred!")
        
def AddToFiresotreField():
    print("Flow Line :  Add To Firesotre.......")
    doc_ref = db.collection(u'RTRobot').document(u'sensorData')
    try:
        humidity_str,temperature_str=humidity_temperature(18);
        Distance_str=ObjectDistance();
        ToxicGas_str=ToxicGasDectection();
        
        
        data = {
            u'Gas':ToxicGas_str,
            u'Humidity':humidity_str,
            u'Temp':temperature_str,
            u'Distance':Distance_str
            }
        doc_ref.set(data)
    except google.cloud.exceptions.NotFound:
        print("Flow Line :  No such document..")
    except:
        print("Flow Line :  error occurred!")
    finally:
        print("Flow Line :  Add To Firesotre Complected..")
        
#if __name__ == "__main__":
#    AddToFiresotreField();
#    CaptureFiresotreChanges();