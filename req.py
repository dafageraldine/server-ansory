import requests

data = {"username": "joni11","pass":"12345","kelas":"12 IPA 4","absen":"20","nilai":"0","nama siswa":"joni"}
url = "http://127.0.0.1:5000/register"
response = requests.post(url,data=data)
print(response.content)