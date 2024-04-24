import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

# Initialize Firebase Admin SDK
cred = credentials.Certificate('firebaseKey.json')
firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()

# Get a document from Firestore
def getMealDoc(document_id):
    
    print(document_id)
    doc_ref = db.collection("meals").document(document_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None


def getTodaysMeal():
    current_month_year = datetime.datetime.now().strftime("%B%Y")
    document_id = current_month_year.lower()
    meal_doc = getMealDoc(document_id)
    today = datetime.datetime.now().strftime("%d")
    print(today)
    return meal_doc[today]

def setMealDoc(data):
    current_month_year = datetime.datetime.now().strftime("%B%Y")
    document_id = current_month_year.lower()
    doc_ref = db.collection("meals").document(document_id)
    doc_ref.set(data, merge=True)