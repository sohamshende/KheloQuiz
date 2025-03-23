from django.shortcuts import render

# Create your views here.

def about_view(request, *args, **kwargs):
    item_list = {
        "item1": "item1",
        "item2": "item2",
        "item3": [10,20,30],
    }
    return render(request, "pages/about.html",item_list)