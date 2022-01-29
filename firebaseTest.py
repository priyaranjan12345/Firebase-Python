from firebase import firebase

database = firebase.FirebaseApplication("https://pythondb-69265.firebaseio.com/")

#                       databasename/table
result = database.get("pythondb-69265/Saller", '')

print(result,"\n")
print("\ntype of data :",type(result))

print("----Name----")
for data in result:
      print(result[data]['Name'])


for datas in result:
      print(result[datas])


