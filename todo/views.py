from django.shortcuts import render,redirect,get_object_or_404
from todo.forms import TodoForm
from todo.forms import ContactForm
from todo.models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    contactform=ContactForm(request.POST or None)
    if contactform.is_valid():
        contactform.save()
        return redirect("home")
    return render(request,'contact.html',{'form': contactform})
  
    
#creation of reviews
def todoadd(request):
    todoform=TodoForm(request.POST or None)
    if todoform.is_valid():
        todoform.save()
        return redirect("todolist")
    return render(request,'todoadd.html',{'form':todoform})

#displaying the reviews/reading

def todolist(request):
    allfeedback=Todo.objects.all()#reading the data from databse
    return render(request,'todolist.html',{'todos':allfeedback})
#updation
def todoedit(request,pk):
    todo=get_object_or_404(Todo,pk=pk)
    todoform=TodoForm(request.POST or None,instance=todo)
    if todoform.is_valid():
        todoform.save()
        return redirect('todolist')
    return render(request,'todoadd.html',{'form':todoform})

#deletion
def tododelete(request,pk):
    todo=get_object_or_404(Todo,pk=pk)
    if request.method=="POST":
        todo.delete()
        return render('todolist')
    return render(request,'tododelete.html',{'todo':todo})
