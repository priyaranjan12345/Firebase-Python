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
https://firebasestorage.googleapis.com/v0/b/pythondb-69265.appspot.com/o/images%2Fa.jpg?alt=media&token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjUzNmRhZWFiZjhkZDY1ZDRkZTIxZTgyNGI4OTlhMWYzZGEyZjg5NTgiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcHl0aG9uZGItNjkyNjUiLCJhdWQiOiJweXRob25kYi02OTI2NSIsImF1dGhfdGltZSI6MTYyMDg4MjAwMCwidXNlcl9pZCI6IjRlejJCUUxsd1BQTDdDZUQxVXBDUmFTZnRsWDIiLCJzdWIiOiI0ZXoyQlFMbHdQUEw3Q2VEMVVwQ1JhU2Z0bFgyIiwiaWF0IjoxNjIwODgyMDAwLCJleHAiOjE2MjA4ODU2MDAsImVtYWlsIjoic2l0YUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsic2l0YUBnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.mgf3UQbOzQnlDsrsBIAdnfT_ySN4FqLQB9b1rAI1lY8mRRH8f6m4C6zUQub2ABmFkQ1hsJyZMCQSuhRzfS-vgqhFCdbW4Tjs82iRw6Sqb-c-VTCyG0QnKMUwx0i6lbMMV3BDz5B2SLcfvkLNgfEX1PAiN9Riy3pAT731OPm8FrlUC2ps0D4CkN-928aFvHv5Hw6IpNW3tt7K2CZQ9wXD5KdFj0DCI2j1lv2Oyi_K37j4NotMUp02QRlgmiYhJkYxRyrHmGPF7fRilRygkbL-oIXqBvecJjZ_Tlnb5ISVXJ86s2iHeRu9Jn50QaMhH8ND0SoB6aljMA5PmhOFW6gswQ
"""
"""
https://firebasestorage.googleapis.com/v0/b/pythondb-69265.appspot.com/o/images%2Fa.jpg?alt=media&token=14cbe065-4067-4c74-9f8a-aca21631c683
"""