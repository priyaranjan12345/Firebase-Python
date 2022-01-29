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


email = input("Enter a Email id : ")
password = input("Enter a Password : ")


# signIn firebase Auth
try:
      login = auth.sign_in_with_email_and_password(email,password)
      print("Login Successfully")
except:
      print("Error in Login")

# signOut firebase auth
try:
      auth.current_user['localId'].islower
      
      print("SignOut Successfully")
except Exception as e:
      print("Error In signOut : ",e.args[0])
#  get current user uid    
try:
      print("uid : ",login['localId'])
except Exception as e:
      print("Error login uid : ",e.args[0])
# Or
try:
      token = login['idToken']
      uid = auth.refresh(login['refreshToken'])
      print("uid : ",uid['userId'])
except Exception as e:
      print("Error current uid : ",e.args[0])

