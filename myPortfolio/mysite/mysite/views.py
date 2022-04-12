# This all things are coding by Abhishek
from django.http import HttpResponse

# Path formate : "C:\\Users\\ASHWANI\\OneDrive\\Desktop\\myWebsite\\myPortfolio\\mysite\\mysite\\repository"


def home(request):
    ind_path = "C:\\Users\\ASHWANI\\OneDrive\\Desktop\\myWebsite\\myPortfolio\\mysite\\mysite\\repository\\home.txt"
    with open(ind_path) as f:
        home_page = f.read()
    return HttpResponse(home_page)


def about(request):
    return HttpResponse("<h1>This is my about page</h1>")


def contact(request):
    return HttpResponse("<h1>This is my Contact page. Where you can contact me.</h1>")


def poem(request):
    poem_path = "C:\\Users\\ASHWANI\\OneDrive\\Desktop\\myWebsite\\myPortfolio\\mysite\\mysite\\repository\\poem.txt"
    with open(poem_path) as f:
        poems = f.read()
    return HttpResponse(poems)