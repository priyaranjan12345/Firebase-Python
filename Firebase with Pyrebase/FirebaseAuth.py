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

#print(dir(auth.requests.delete))

email = input("Enter a Email id : ")
password = input("Enter a Password : ")

'''
#signUp firebase auth
try:
      user = auth.create_user_with_email_and_password(email, password)
      print("User created Successfully")
except:
      print("User Already Exist")
'''
'''
auth.send_email_verification(user['idToken'])
print("Check Your Email")
'''

# signIn firebase Auth
try:
      login = auth.sign_in_with_email_and_password(email,password)
      print("Login Successfully")
except:
      print("Error in Login")

# signOut firebase auth
try:
      #auth.logout(auth.request)
      #del login['localId']

      #print(auth.current_user['localId'])
      #auth.api_key
      
      print("SignOut Successfully")
except Exception as e:
      print("----Error in signout----")
      print("Error : ",e.args[0])
   
try:
      print("uid : ",login['localId'])
except Exception as e:
      print("Error : ",e.args[0])
# Or
try:
      token = login['idToken']
      uid = auth.refresh(login['refreshToken'])
      print("uid : ",uid['userId'])
except Exception as e:
      print("Error : ",e.args[0])


