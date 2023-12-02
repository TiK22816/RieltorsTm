from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.shortcuts import render
from .models import Registration




def person_create(request):
    if request.method == 'POST':
        Registration.objects.create(name=request.POST.get('Name_user'), password=request.POST.get('Password_user'))
    if request.POST.get('Name_user')=='Timur' and  request.POST.get('Password_user')=='123':
        return HttpResponseRedirect('http://127.0.0.1:8000/admin/')


    return render(request, 'index.html')

def about(request):
        return HttpResponse('<h1>Сайт был создан для курсовой по Python Django</h1>')

def person(request):
    res_str = ''
    for p in Registration.objects.all():
        res_str+=str(p)+'<br>'
    return HttpResponse('Все зарегестрированные люди....<br>'+res_str)

def persons_delete(request,id):
    try:
        id = int(id)
        person = Registration.objects.get(id=id)
        if person is not None:
            person.delete()
    except Exception as e:
        print(e)
    return HttpResponsePermanentRedirect('/persons/')

def person_update(request,id,name,password):
    try:
        person = Registration.objects.get(id=id)
        if person is not None:
            person.name = name
            person.password = password
            person.save()
    except:
        pass
    return HttpResponsePermanentRedirect('/persons/')