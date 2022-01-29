import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

# Using add to add documents with auto generated keys
db.collection('persons').add({'name':'John', 'age':42, 'address': "New York"})
db.collection('persons').add({'name':'Jane', 'age':50, 'address': "Los Angeles"})
db.collection('persons').add({'name':'Mark', 'age':30, 'address': "Paris"})
db.collection('persons').add({'name':'Harry', 'age':40, 'address': "London"})
db.collection('persons').add({'name':'Ron', 'age':40, 'address': "Milan"})
db.collection('mycoll').document("mydoc1").collection("mycoll2").add({'name':'Ron', 'age':40, 'address': "Milan"})
db.collection('mycoll').document("mydoc2").collection("mycoll2").add({'name':'jhon', 'age':43, 'address': "Milan"})
db.collection('mycoll').document("mydoc3").collection("mycoll2").add({'name':'jhon', 'age':43, 'address': "Milan"})

# Create a reference for the document before setting
data = {
    'name': 'Harry Potter',
    'address': 'USA',
    'accounts':['twiter', 'microsoft']
}

# Add a new doc in collection 'persons' with ID 'HP'
db.collection('persons').document('HP').set(data)

# Merge or add new data with existing data for 'HP'
#also update like this
data = {'employed':True}
db.collection('persons').document('HP').set(data, merge=True)

# Using document() to get an auto generated ID with set()
data = {
    'name': 'Iron Man',
    'address': 'USA',
    'accounts':['youtube', 'twiter', 'google', 'microsoft']
}
document_reference=db.collection('heroes').document()
document_reference.set(data)

# Adding subcollections
document_reference.collection('movies').add({'name':'Avengers'})
