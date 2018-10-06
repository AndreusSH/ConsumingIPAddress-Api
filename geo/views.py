from django.shortcuts import render 
import requests

def home(request):
    response = requests.get('http://api.ipstack.com/check?access_key=YourOwnKey')
    data = response.json() 
    return render(request, 'geo/home.html', {
        'ip': data['ip'],
        'country': data['country_name'],
        'continent': data['continent_name'],
        'zip': data['zip'],
        'capital':data['location']['capital'],
        'flag': data['location']['country_flag']
    })
 
    
