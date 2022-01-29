from firebase import firebase

firebase = firebase.FirebaseApplication("https://pythondb-69265.firebaseio.com/", None)

firebase.put("pythondb-69265/Student/-M-QbxVm1e9zv3VNM2y2", 'Name', 'Rina')

print("Update successfull...")
