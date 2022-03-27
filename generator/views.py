from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):
 

    characters = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()_+}{":][?><'))

    if request.GET.get('number'):
        characters.extend(list('1236547890'))


    length = int(request.GET.get('length',12))

    thepassword = ''
    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html',{'password':thepassword} )

def discription(request):
    return render(request, 'generator/discription.html')


