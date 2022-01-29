from firebase import firebase

firebase = firebase.FirebaseApplication("https://pythondb-69265.firebaseio.com/", None)


data = {
      'Name':'Sita',
      'Email':'sita@gmail.com',
      'phone':90456656540
      }

result = firebase.post("pythondb-69265/Student", data)


print(result)
