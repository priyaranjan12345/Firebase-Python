from firebase import firebase

database = firebase.FirebaseApplication("https://pythondb-69265.firebaseio.com/")

print(database)

result1 = database.get("pythondb-69265/Student", '')
#                       databaseloacation/table/id
result = database.get("pythondb-69265/Student/-M-QbxVm1e9zv3VNM2y2", '')

print(result,"\n")
print("\ntype of data :",type(result))

print("\nEmail: ",result['Email'])
print("Name:",result['Name'])
print("Phone no: ",result['phone'],"\n")

print(result1)

##for data in result:
##      print(data)
##
