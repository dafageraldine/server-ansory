from flask import Flask,request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask_cors import CORS

###initialize git
app = Flask(__name__)
CORS(app)
cred = credentials.Certificate('ansory-8dc38-firebase-adminsdk-2xtx8-de4e743e1b.json')
firebase_admin.initialize_app(cred)
dbq = firestore.client()
doc_ref = dbq.collection('datasiswa')

@app.route('/login',methods=["POST"])
def login():
    data = request.form.to_dict(flat=False)
    val = doc_ref.where("username","==",data['username'][0]).where("pass","==",data['pass'][0]).get()
    if (len(val) == 1):
        return {"data" : "sukses","nama":val[0].to_dict()['nama siswa'],"kelas":val[0].to_dict()['kelas'],"absen" :val[0].to_dict()['absen'],"nilai":val[0].to_dict()['nilai'],"username":val[0].to_dict()['username']}
    else:
        return{"data":"password atau username salah"}

@app.route("/getdatasiswa")
def getdatasiswa():
    data = doc_ref.get()
    djson = []
    for i in range(len(data)):
        nama = data[i].to_dict()['nama siswa']
        kelas = data[i].to_dict()['kelas']
        absen = data[i].to_dict()['absen']
        nilai = data[i].to_dict()['nilai']
        username = data[i].to_dict()['username']
        ids = data[i].id
        djson.append({"nama" : nama,'absen' : absen,'kelas' : kelas,'nilai' : nilai,"id":ids,"username":username})
    return{"data":djson}

@app.route("/register",methods=["POST"])
def register():
    data = request.form.to_dict(flat=False)
    val = doc_ref.where("username","==",data['username'][0]).get()
    # print(len(val))
    if(len(val)==0):
        doc_ref.document().set({
            'absen':data['absen'][0],
            'kelas':data['kelas'][0],
            'nama siswa':data['nama siswa'][0],
            'nilai':data['nilai'][0],
            'pass':data['pass'][0],
            'username':data['username'][0],
        })
        return{"data":"sukses"}
    else:
        return{"data":"username telah diambil"}

@app.route("/insertnilai",methods=["POST"])
def insertnilai():
    return {"data":"sukses"}

if __name__ == "__main__":
    app.run(debug=True,)