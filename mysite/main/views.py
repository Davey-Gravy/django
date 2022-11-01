from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def index(response, id):
    lst = ToDoList.objects.get(id=id)
    if response.method == "POST":
        print(response.POST)
        # if using the save button, update checkbox status
        if response.POST.get('save'):
            for item in lst.item_set.all():
                if response.POST.get(f'c{item.id}') == 'clicked':
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        # if using add item button, create new item, set text as input
        elif response.POST.get('newItem'):
            txt = response.POST.get('new')
            if len(txt) > 2:
                lst.item_set.create(text=txt, complete=False)
            else:
                print('invalid')
    
    return render(response, 'main/list.html', {'lst':lst})

def home(response):
    return render(response, 'main/home.html', {})

def create(response):
    # response.user     # grants access to user properties (name, pass, is_authenticated, etc.)
    if response.method == "POST":       
        form = CreateNewList(response.POST)

        # if form string is valid,
        # clean name, create todo list
        if form.is_valid():
            n = form.cleaned_data['name']
            response.user.todolist_set.create(name=n)

        # if form is post request,
        # redirect to newly created list
        return HttpResponseRedirect(f'/{t.id}')

    else:
        form = CreateNewList()
    
    return render(response, 'main/create.html', {'form':form})

def view(response):
    return render(response, 'main/view.html')