import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('firebaseKey.json')

firebase_admin.initialize_app(cred)

database = firestore.client()

myref = database.collection('Student1').document('stu_doc2')
#or//
#myref = database.collection('Student1').add({'name:Rama', 'Id':04, 'age':21})

myref.set({
            'Name' : 'Hari',
            'Id' : 3,
            'age' : 23
      })
print("Data Inserted Successfully")


# add attribute
