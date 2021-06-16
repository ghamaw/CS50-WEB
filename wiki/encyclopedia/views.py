from markdown2 import Markdown
from django.shortcuts import render
from django.http import HttpResponse

from . import util


def index(request):
    # Search Function here
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, entry):
    # if entry not in util.list_entries():
    #     return render(request, "encyclopedia/empty_entry.html", {
    #         "empty_title": entry
    #     })
    # content = util.list_entries(entry)
    # Get all entry
    list_entry = util.get_entry(entry)
    
    # Check if the input entry does exist
    if list_entry == None:
        return render(request, "encyclopedia/empty_entry.html", {
             "empty_title": entry
         })
    return render(request, "encyclopedia/entry.html", {
        "entry_title": entry,
        "content" : Markdown().convert(list_entry)
    })

def search (request):
    if request == "GET":
        return 