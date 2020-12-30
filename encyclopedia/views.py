from django.shortcuts import redirect, render
from django.contrib import messages
import markdown2
from random import choice
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_page(request, title):
    try:
        html_content = markdown2.markdown(util.get_entry(title))
        return render(request, "encyclopedia/page.html", {'entry': (title, html_content)})
    except:
        return render(request, 'encyclopedia/404.html')

def create(request):
    if request.method == 'GET':
        return render(request, 'encyclopedia/create.html')
    title = request.POST.get('title')
    content = request.POST.get('content')
    if title in util.list_entries():
        messages.error(request, 'Entry with the given title already exists!')
        return render(request, 'encyclopedia/create.html')
    util.save_entry(title, content)
    return redirect(f'/wiki/{title}')

def get_random(request):
    title = choice(util.list_entries())
    return redirect(f'/wiki/{title}')

def edit(request, title):
    print(title+'ejeje')
    if request.method == "POST":
        content = request.POST.get('content')
        util.save_entry(title, content)
        return redirect(f'/wiki/{title}')

    return render(request, 'encyclopedia/edit.html', {'entry': (title, util.get_entry(title))})

def search(request):
    title = request.POST.get('q')
    entries = util.list_entries()
    if title in entries:
        return redirect(f'/wiki/{title}')

    entries_to_be_displayed = []
    for entry in entries:
        if util.get_entry(entry).find(title) != -1:
            entries_to_be_displayed.append(entry)
    print(entries_to_be_displayed)
    return render(request, "encyclopedia/searchresults.html", {
        "entries": entries_to_be_displayed
    })