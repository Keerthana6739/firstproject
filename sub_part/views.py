from django.shortcuts import render
# import request

# Create your views here.
def index(request):
    return render(request,'index.html')

def first(request):
    return render(request,'first.html')