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

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
storage = firebase.storage()

email = input("Enter a Email id : ")
password = input("Enter a Password : ")
login = auth.sign_in_with_email_and_password(email,password)
print("Login Successfully")

storage.child("images/a.jpg").put("imgs/a.jpg")
print("image uploaded")
storage.child("images/a.jpg").download("dimgs/burger.jpg")
print("image downloaded")

imgurl = storage.child("images/a.jpg").get_url(login['idToken'])
print(imgurl)
