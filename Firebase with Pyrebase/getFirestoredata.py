import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('firebaseKey.json')

firebase_admin.initialize_app(cred)

database = firestore.client()

class myModel:
      name = ""
      age = 0
      sid = 0

modelLst = []

myref = database.collection('Student1').where("Name", "==", "Ram")

docs = myref.stream()

for doc in docs:
      print(f'{doc.id} : {doc.to_dict()}')
      d = doc.to_dict()
      for a in d:
            print(a, ' : ', d[a])

#//or
data = database.collection('Student1').where("Name", "==", "Ram").get()
for doc in data:
      print('document: ',doc.id)
      print(doc.to_dict())
