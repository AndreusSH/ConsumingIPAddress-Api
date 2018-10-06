from django.shortcuts import render 
import requests

def home(request):
    response = requests.get('http://api.ipstack.com/check?access_key=2cf547973c9f834bbb2032dbddd4a926')
    geodata = response.json() 
    return render(request, 'geo/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })
 
    
