from django.shortcuts import render,redirect
import requests

def home(request):
    response = requests.get('http://api.ipstack.com/134.201.250.155?access_key=2cf547973c9f834bbb2032dbddd4a926')
    geodata = response.json() 
    return render(request, 'geo/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })

def search(request):
    if request.method == 'POST':
        
        return render(request,'geo/search.html')