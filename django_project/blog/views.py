from django.shortcuts import render

posts = [
    {
        "title":"My First Blog Post",
        "author":"Dhananjay Rout",
        "content":"This is a blog about python course.",
        "date_posted":"14-04-2020"
    },
    {
        "title":"My Second Blog Post",
        "author":"Tanmay Kar",
        "content":"This is a blog about Java course.",
        "date_posted":"14-03-2020"
    }
]

def home(request):
    context = {
        "posts":posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {"title":"About"})
