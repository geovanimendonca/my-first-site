from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import storage
import os, itertools

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./pythondbtest-a8bdf-firebase-adminsdk-daafs-7052e44485.json"

firebaseConfig = {
    'apiKey': "AIzaSyDuYp1S1udPe47Idq2zM9FCAg-X3QDUgpw",
    'authDomain': "pythondbtest-a8bdf.firebaseapp.com",
    'databaseURL': "https://pythondbtest-a8bdf.firebaseio.com",
    'projectId': "pythondbtest-a8bdf",
    'storageBucket': "pythondbtest-a8bdf.appspot.com",
    'messagingSenderId': "418377876568",
    'appId': "1:418377876568:web:8c563caf3c401c2b7e762d",
    'measurementId': "G-4V1VH879R1"
}
cred = credentials.Certificate('./pythondbtest-a8bdf-firebase-adminsdk-daafs-7052e44485.json')

db = firestore.client() # Database
client = storage.Client() # Storage
bucket = client.get_bucket('pythondbtest-a8bdf.appspot.com')

# Exemplo de botão que upa coisas pra nuvem
def button(request):
    return render(request,'lab/base.html')
# Exemplo de botão que upa coisas pra nuvem
def output(request,pk):
    post_to_delete=Post.objects.get(id=pk)
    try:
        #sprint("done")
        users_ref = db.collection(u'Exame_site')
        docs = users_ref.stream()
        for doc in docs:
            CPF = str(post_to_delete.Cpf_pacient)
            #print(CPF)
            #print(u'{} => {}'.format(doc.id, doc.to_dict()))
            exp = doc.to_dict()
            data = exp.get(CPF+"result","")
            print(data)
        if data != None:
            Exame_result = data[0]
            return render(request,'lab/result.html',{'data':data,'exame':Exame_result})
    except:

        return render(request, 'lab/result.html')
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'lab/post_list.html',{'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'lab/post_detail.html', {'post': post})

def post_new(request):

     if request.method == "POST":
         form = PostForm(request.POST)
         
         if form.is_valid():

             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             Equipamento = 'Exame_site' 
             CPF = str(post.Cpf_pacient)
             doc_ref = db.collection(Equipamento).document(u'Exames')#.document(CPF+' '+date_time_txt)
             doc_ref.set({
                 CPF:[str(post.Exam),str(post.Pacient),str(post.Observations),str(post.author),str(post.published_date)]
             },merge=True)
             return redirect('post_detail', pk=post.pk)

     else:
         form = PostForm()
     return render(request, 'lab/post_edit.html', {'form': form}) 
    
def post_edit(request, pk):
     post = get_object_or_404(Post, pk=pk)
     if request.method == "POST":
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             #post.author = request.user
             post.published_date = timezone.now()
             post.save()
             Equipamento = 'Exame_site' 
             CPF = str(post.Cpf_pacient)
             doc_ref = db.collection(Equipamento).document(u'Exames')#.document(CPF+' '+date_time_txt)
             doc_ref.set({
                 CPF:[str(post.Exam),str(post.Pacient),str(post.Observations),str(post.author),str(post.published_date)]
             },merge=True)
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm(instance=post)
     return render(request, 'lab/post_edit.html', {'form': form})

def delete_post(request,pk):
    
    post_to_delete=Post.objects.get(id=pk)
    Equipamento = 'Exame_site' 
    CPF = str(post_to_delete.Cpf_pacient)
    print(str(post_to_delete.Cpf_pacient))
    doc_ref = db.collection(Equipamento).document(u'Exames')
    doc_ref.update({str(CPF):firestore.DELETE_FIELD})

    post_to_delete.delete()
    return redirect('/')

def register(response):
    return render()
