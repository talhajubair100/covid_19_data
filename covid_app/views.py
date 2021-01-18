from django.shortcuts import render

# Create your views here.

import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "88b8319385msh1013fdd44af27bcp19bc49jsn733943950085",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

#print(response.text)


def home(request):
    noresults = response['results']
    con_list = []
    for i in range(0, noresults):
        con_list.append(response['response'][i]['country'])
    context = {'con_list': con_list}
    return render(request, 'home.html', context)