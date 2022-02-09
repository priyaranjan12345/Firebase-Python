import urllib.request

def download_file(url, image_name):
    full_path = image_name + ".jpg"
    urllib.request.urlretrieve(url, full_path)

url = input("Enter image url : ")
image_name = input("Enter image name : ")

download_file(url, image_name)


"""
https://firebasestorage.googleapis.com/v0/b/database-1d34d.appspot.com/o/Images%2Ffood_items%2Fburger.png?alt=media&token=a41aafd4-3d8e-45b0-9f32-d5433bb7b7b4
"""
"""
https://firebasestorage.googleapis.com/v0/b/pythondb-69265.appspot.com/o/images%2Fa.jpg?alt=media&token=eyJhbGciOiJSUzFvHv5Hw6IpNW3tt7K2CZQ9wXD5KdFj6gswQ
"""
"""
https://firebasestorage.googleapis.com/v0/b/pythondb-69265.appspot.com/o/images%2Fa.jpg?alt=media&token=14cbe065-4067-4c74-9f8a-aca21631c683
"""
