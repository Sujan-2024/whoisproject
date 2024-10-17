from django.shortcuts import render
import whois11
# Create your views here.
def index(request):
    return render(request, 'whoisapp/index.html')

def details(request):
    # get domain from form
    domain = request.GET.get('domain')
    info = whois11.whois(domain)
    return render(request, 'whoisapp/details.html', {'domain': domain, 'info': info})