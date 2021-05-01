from django.shortcuts import render

import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate('cred.json')
firebase_admin.initialize_app(cred)

def home(request):
    return render(request,'home.html')
def donar(request):
    return render(request,'donar.html')
def taker(request):
    l=[]
    db = firestore.client()
    doc_ref = db.collection(u'donar')

    doc = doc_ref.get()
    for i in doc:
        print(i)
        print(f'Document data: {i.to_dict()}')
        l.append(i.to_dict())
    # if doc.exists:
    #     print(f'Document data: {doc.to_dict()}')
    # else:
    #     print(u'No such document!')
    

    return render(request,"taker.html",{"donars":l})
def dregister(request):
    if(request.method=="POST"):
        name=request.POST['name']
        age=request.POST['age']
        sex=request.POST['sex']
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pincode']
    db = firestore.client()
    doc_ref = db.collection(u'donar')
    doc_ref.add({"name":name,
    "age":age,
    "sex":sex,
    "address":address,
    "city":city,
    "state":state,
    "pincode":pincode})

    return render(request,'thanku.html')