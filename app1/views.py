from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse, JsonResponse
from app1.models import ToDo
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def home(request):
    return render(request, "login.html")

def login(request):
    if request.method == "POST":
        crdntls = {
            "usr": request.POST['usr'],
            "pwd": request.POST['pwd']
        }
        user = auth.authenticate(username = crdntls['usr'], password=crdntls['pwd'])
        if user:
            auth.login(request, user)
            return redirect("dashboard")
        else:
            messages.info(request, "Invalid credentials")
            return redirect("home")
    else:
        return render(request, 'login.html')
 

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, "dashboard.html")
    else:
        messages.info(request, "Access Denied")
        return redirect("home")

# todo list
def getlist(request):
    dt = {'message' : []}
    todos = ToDo.objects.raw("select a.*, b.username from app1_todo as a join auth_user as b on a.user_id = b.id")
    for todo in todos: 
        t = todo.__dict__
        dt['message'].append([
            '<a href="view?id={}">{}</a>'.format(t['id'],t['todo']), 
            "Yes" if t['is_done'] == 1 else "No", 
            t['username'],
        ])
    return JsonResponse(dt)

# create todo
def add_todo(request):
    if request.method == "POST":
        data = request.POST
        try:
            ToDo(
                todo = data['todo'],
                is_done = data['is_done'],
                user = request.user
            ).save()

            return getlist(request)
        except Exception as e:
            raise Exception(str(e))


# redirect details
def view_details(request):
    if request.method == "GET":
        todo_details = ToDo.objects.filter(id=request.GET['id'])[0].__dict__
        return render(request, "details.html", todo_details)


# create todo
def edit_todo(request):
    if request.method == "POST":
        data = request.POST
        todo = ToDo.objects.get(id=data['id'])
        try:
            todo.todo = data['todo']
            todo.is_done = data['is_done']
            todo.save()
            return JsonResponse({"message": True})
        except Exception as e:
            raise Exception(str(e))
        

def delete_todo(request):
    if request.method == "GET":
        try:
            ToDo.objects.get(id=request.GET['id']).delete()
            return JsonResponse({"message": True})
        except Exception as e:
            raise Exception(str(e))



def logout(request):
    auth.logout(request)
    return redirect('home')
