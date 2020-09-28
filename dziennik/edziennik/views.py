from django.shortcuts import render ,get_object_or_404 ,get_list_or_404
from django.http import HttpResponse
from django.shortcuts import render
from  django.utils.datastructures import MultiValueDictKeyError
from  django.contrib.auth.models import Group ,User
from  django.contrib.auth import authenticate ,get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.views import generic
from django.views.generic.edit   import UpdateView
# funkcja zwracajacca grupe nr 0 brak lub bez log
# 1 uczen 2 nauczyciel
def check_grupa(request):
    nr_grupy = 0
    if request.user.is_authenticated:
        nr_grupy=1
        if request.user.has_perm('edziennik.nauczyciel'):
            nr_grupy=2
    return nr_grupy

def index(request) :
    return render(request,'index.html')

def login(request):
    return render(request,'index.html')

def abc(request):
    print("PRZED AUTORYZ  ")

    nr=check_grupa(request)
    if nr == 1:
        quest = get_object_or_404(Osoba, user_id=request.user.id)
        return render(request, 'glowna_u.html', {'quest': quest})
    elif nr == 2:
        quest = get_object_or_404(Osoba, user_id=request.user.id)
        quest2=get_list_or_404(Plan,id_n_id=quest.id)
        return render(request, 'glowna_n.html',{'quest': quest ,'quest2':quest2})
    else: return render(request, 'index.html')

def szczegoly(request,idp):

        nr=check_grupa(request)
        if nr==2:

            quest=get_object_or_404(Plan,id=idp)
            idk=quest.id_k_id

            idu=[]

            quest2=get_list_or_404(Listaklasy,id_k_id=idk)
            for i in range(len(quest2)):
                idu.append(quest2[i].id_u_id)
                print(quest2[i].id_u_id)
            quest3=get_list_or_404(Osoba, id__in=idu)
            return render(request,'szczegoly.html',{'quest2':quest2 , 'quest3':quest3 ,'idp':idp } )

        else: return render(request, 'index.html')

def edytuj(request,idp) :
    nr = check_grupa(request)
    if nr == 2:
        try:
            idu= request.POST['wybor']
        except MultiValueDictKeyError:
            quest = get_object_or_404(Plan, id=idp)
            idk = quest.id_k_id
            idu = []
            quest2 = get_list_or_404(Listaklasy, id_k_id=idk)
            for i in range(len(quest2)):
                idu.append(quest2[i].id_u_id)
            quest3 = get_list_or_404(Osoba, id__in=idu)
            return render(request, 'szczegoly.html', {'quest2': quest2, 'quest3': quest3, 'idp': idp})
        quest = get_object_or_404(Osoba, id=idu)
        quest2=get_list_or_404(Ocena,id_n_id=idp ,id_u_id=idu)
        return render(request,'edytuj.html',{'idp':idp ,'quest2':quest2 , 'quest':quest })
    else:
        return render(request, 'index.html')

def zatwierdze(request,idp):
        nr = check_grupa(request)
        if nr == 2:
            ido = request.POST['wybor']
            updatee=request.POST['new_ocena']
            if updatee=='0':
                Ocena.objects.filter(id=ido).delete()
            else :
                #zamien ocene
                Ocena.objects.filter(id=ido).update(ocena=updatee)
            quest = get_object_or_404(Osoba, user_id=request.user.id)
            quest2 = get_list_or_404(Plan, id_n_id=quest.id)
            return render(request, 'glowna_n.html', {'quest': quest, 'quest2': quest2})
        else:
                return render(request, 'index.html')






def dodajo(request,idp):
    nr = check_grupa(request)
    if nr == 2:
        quest=get_object_or_404(Plan, id=idp)
        quest2=get_list_or_404(Listaklasy,id_k_id=quest.id_k_id)
        idu=[]
        for i in range(len(quest2)):
            idu.append(quest2[i].id_u_id)
            print(quest2[i].id_u_id)
        quest3=get_list_or_404(Osoba,id__in=idu)
        return render(request,'dodajo.html',{'idp':idp ,'quest2':quest2 , 'quest':quest ,'quest3':quest3 })
    else:
        return render(request, 'index.html')

def zatwierdzo(request,idp):
    nr = check_grupa(request)
    if nr == 2:
        ile =0
        ile=int (request.POST['ile'])
        quest=get_object_or_404(Plan,id=idp)
        for n in range(ile):
            numer=str(n+1)
            ocenai ='new_ocena'+numer

            ocena = request.POST[ocenai]
            if ocena!='0':
                waga=request.POST['waga']
                opis=request.POST['opis']
                idui = 'idu' + numer
                idu = request.POST[idui]
                statment=Ocena(id_u_id=idu ,ocena=ocena,waga=waga , przedmiot=quest.przedmiot ,id_n_id=idp,opis=opis )
                statment.save()

        quest = get_object_or_404(Osoba, user_id=request.user.id)
        quest2 = get_list_or_404(Plan, id_n_id=quest.id)
        return render(request, 'glowna_n.html', {'quest': quest, 'quest2': quest2})
    else:
        return render(request, 'index.html')
