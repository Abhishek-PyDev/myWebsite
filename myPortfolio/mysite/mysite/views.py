# This all things are coding by Abhishek
from django.http import HttpResponse


def home(request):
    ind_path = "C:\\Users\\ASHWANI\\OneDrive\\Desktop\\Django\\myPortfolio\\mysite\\mysite\\repository\\home.txt"
    with open(ind_path) as f:
        home_page = f.read()
    return HttpResponse(home_page)


def about(request):
    return HttpResponse("<h1>This is my about page</h1>")


def contact(request):
    return HttpResponse("<h1>This is my Contact page. Where you can contact me.</h1>")
