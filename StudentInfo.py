from firebase import firebase

database = firebase.FirebaseApplication("https://mydata-6b138.firebaseio.com/")

print(database)
try:
      result1 = database.get("mydata-6b138/StudentInfo", '')
      print(result1,"\n")
      print("\ntype of data :",type(result))

except:
      print("Error in authentication")
