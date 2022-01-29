import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db=firestore.client()

# Read data
# Get a document with known id
result = db.collection('persons').document("HP").get()
if result.exists:
    print(result.to_dict())

print("*"*40)
# Get all documents
docs = db.collection('persons').get()
for doc in docs:
    print(doc.to_dict())

print("*"*40)
# Query
# Equal
docs = db.collection('persons').where("age", "==", 40).get()
for doc in docs:
    print(doc.to_dict())

print("*"*40)
# Greater than
docs = db.collection('persons').where("age", ">", 22).get()
for doc in docs:
    print(doc.to_dict())

print("*"*40)
# Array contains
docs = db.collection('persons').where("accounts", "array_contains", "twiter").get()
for doc in docs:
    print(doc.to_dict())

print("*"*40)
# In
docs = db.collection('persons').where("address", "in", ["New York", "London"]).get()
for doc in docs:
    print(doc.to_dict())

print("*"*40)
# In
docs = db.collection('heroes').where("accounts", "array_contains", "youtube").get()
for doc in docs:
    print(doc.to_dict())
