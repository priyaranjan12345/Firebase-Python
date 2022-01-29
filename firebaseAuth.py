from firebase import Firebase

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

firebase = Firebase(firebaseConfig)

auth = firebase.auth()

def signUp():
      email = input("Enter a Email id : ")
      password = input("Enter a Password : ")

      user = auth.create_user_with_email_and_password(email, password)
      print("User created Sucessfully")

def signIn():
      email = input("Enter a Email id : ")
      password = input("Enter a Password : ")

      user = auth.sign_in_with_email_and_password(email, password)
      print("SignIn Sucessfully")


opt = input("Are you a new user?[y/n] : ")

if(opt.lower() == 'y'):
      signUp()
else:
      signIn();


"""

# signout firebase Auth
try:
      token = login['idToken']
      uid = auth.refresh(login['refreshToken'])
      print("uid : ",uid['userId'])
      print("SignOut Successfully")
except Exception as e:
      print("Error SignOut : ",e.args[0])
"""
