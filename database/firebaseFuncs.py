import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
import pytz

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
    timezone = pytz.timezone('America/La_Paz')
    current_month_year = datetime.datetime.now(timezone).strftime("%B%Y")
    document_id = current_month_year.lower()
    meal_doc = getMealDoc(document_id)
    today = datetime.datetime.now().strftime("%d")
    print(today)
    return meal_doc[today]

def setMealDoc(data, month=None):
    if(month==None):
        timezone = pytz.timezone('America/La_Paz')
        current_month_year = datetime.datetime.now(timezone).strftime("%B%Y")
        document_id = current_month_year.lower()
    else:
        timezone = pytz.timezone('America/La_Paz')
        document_id = month.lower()+datetime.datetime.now(timezone).strftime("%Y").lower()
    print(document_id)
    doc_ref = db.collection("meals").document(document_id)
    doc_ref.set(data, merge=True)

def getAllMealDocs():
    meal_docs = []
    collection_ref = db.collection("meals")
    docs = collection_ref.get()
    for doc in docs:
        meal_docs.append(doc.to_dict())
    return meal_docs