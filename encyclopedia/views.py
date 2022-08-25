import markdown
from django.urls import reverse,is_valid_path
import random
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.shortcuts import render,redirect
from django import forms
from . import util



class edit_entry():
    title = ''
    content = ''
    

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



instance_entry = edit_entry()
def select_Page(request,name):
    entry = util.get_entry(name)
    if entry is None:
        return render(request,'encyclopedia/not_found.html')
    
    
    instance_entry.title = name
    
    html = markdown.markdown(entry)


    return render(request, 'encyclopedia/View_content.html',{
        "xy":html,
        
    })


def random1(request):
    return HttpResponse(select_Page(request,random.choice(util.list_entries())))



def create_entry(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    if title == None:
        return render(request,"encyclopedia/new_entry.html")

    if util.get_entry(title) == None:
        if description == '':
            return render(request,"encyclopedia/new_entry.html",{
            'state':"Make sure you entered descrption"
        })
        util.save_entry(title,description)
        return render(request,"encyclopedia/new_entry.html",{
            'state':"Page succesfully added"
        })
    else:
        return render(request,"encyclopedia/new_entry.html",{
            'state':"Another page found with same name"
        })
    


def search(request):
    search1 = request.POST.get('q')
    list1 = util.list_entries()
    found = []
    
    for x in list1:
        if search1.upper() in x.upper():
            found.append(x)
    return render(request,"encyclopedia/search_result.html",{
            'found':found
        })




def edit(request):
    
    page_entry = instance_entry.title
    body_of_entry = util.get_entry(page_entry)
    
    
    return render(request,'encyclopedia/edit_content.html',{
        'entry_title':page_entry,
        'body':body_of_entry,
    
    })

    

def save_edit(request):
    instance_entry.content = request.POST.get('change_body')
    util.save_entry(instance_entry.title,instance_entry.content)
    return render(request,'encyclopedia/save_edit.html')