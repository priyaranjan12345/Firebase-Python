import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('firebaseKey.json')

firebase_admin.initialize_app(cred)

database = firestore.client()

mydata = database.collection("restaurants").get()

print('__'*60)
for i in mydata:
    print(i.to_dict())
    print('__'*60)

print('__'*60)
for i in mydata:
    d = i.to_dict()['uid']
    print(d)
    '''md = database.collection("restaurants").doc(d).get()
    for k in md:
        print(k.to_dict())
    print('__'*60)'''
