import pyrebase

firebaseConfig = {
  "apiKey" : "AIzaSyB-5CuBmlL-e80c0wFTgH7qFJZkokdMNdQ",
  "authDomain" : "pythondb-69265.firebaseapp.com",
  "databaseURL" : "https://pythondb-69265.firebaseio.com",
  "projectId" : "pythondb-69265",
  "storageBucket" : "pythondb-69265.appspot.com",
  "messagingSenderId" : "1014739720861",
  "appId" : "1:1014739720861:web:7c6610995ac9f4ff965274",
  "measurementId" : "G-TY0RDFQETP"
}

firebaseDb = pyrebase.initialize_app(firebaseConfig)

auth = firebaseDb.auth()

database = firebaseDb.database()
'''
email = input("Enter a Email id : ")
password = input("Enter a Password : ")

login = auth.sign_in_with_email_and_password(email,password)
print("Login Successfully")

uid = login['localId']
'''
# Or
'''
token = login['idToken']
uid = auth.refresh(login['refreshToken'])
print("uid : ",uid['userId'])
'''

data = {
      "name" : "Deba",
      "Rollno" : 23,
      "age" : 22,
      "address" : "Sarang-igit"
      }

database.child("Saller").child('Student_Data').set(data)
print("Data Inserted Successfully")
