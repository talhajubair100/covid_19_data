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
    noresults = int(response['results'])
    con_list = []
    for i in range(0, noresults):
        con_list.append(response['response'][i]['country'])

    if request.method == "POST":
        selectedcountry = request.POST['selectedcountry']
        noresults = int(response['results'])

        for i in range(0, noresults):
            if selectedcountry == response['response'][i]['country']:
                print('country', selectedcountry)
                new = response['response'][i]['cases']['new']
                active = response['response'][i]['cases']['active']
                critical = response['response'][i]['cases']['critical']
                recovered = response['response'][i]['cases']['recovered']
                M_pop = response['response'][i]['cases']['1M_pop']
                total = response['response'][i]['cases']['total']
                deaths = int(total) - int(active)-int(recovered)
        context = {'selectedcountry': selectedcountry, 'con_list': con_list, 'new': new, 'active': active, 'critical': critical, 'recovered': recovered, 'M_pop': M_pop, 'total': total, 'deaths': deaths}
        return render(request, 'home.html', context)

    
    context = {'con_list': con_list}
    
    return render(request, 'home.html', context)