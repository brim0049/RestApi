from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from .models import Chambre, Reservation, Profile
from django.db.models import Sum
from django.utils.timezone import get_current_timezone, now
from datetime import datetime
from .forms import UserForm, ProfileForm
from django.db import transaction
# Create your views here.



def home(request):
    return render(request, "ui_app/home.html",)


def utilisateurs(request):
    if request.method == "GET":
        # filter
        filterProfil = request.GET.get("filterProfil")
        users = User.objects.all()
        if filterProfil == 'Locataire':
            users = User.objects.filter(profile__profil='Locataire')

        elif filterProfil == 'Locateur':
            users = User.objects.filter(profile__profil='Locateur')
        # delete
        id_delete = request.GET.get("delete_id")
        User.objects.filter(id=id_delete).delete()
        return render(request, "ui_app/utilisateurs.html", {"users": users})

    elif request.method == "POST":
        filterProfil = request.GET.get("filterProfil")
        # users
        users = User.objects.all()
        # delete
        id_delete = request.GET.get("delete_id")
        User.objects.filter(id=id_delete).delete()
        # add
        return render(request, "ui_app/utilisateurs.html", {"users": users})
       
           

def addUser(request):
    if request.method == "GET":
        return redirect("utilisateurs")
    elif request.method == "POST":
        users = User.objects.all()
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            mdp = user_form.cleaned_data['password']
            mdpConfirm = profile_form.cleaned_data['passwordConfirm']
            email = user_form.cleaned_data['email']
            if User.objects.filter(email=email) :
                return render(request, "ui_app/addUser.html", {'mailstatus':True})  
            else:
                if mdp == mdpConfirm:
                    sign_up = user_form.save(commit = False)
                    sign_up.password = make_password(user_form.cleaned_data['password'])
                    sign_up.last_login = datetime.now(tz=get_current_timezone())
                    sign_up.save()
                    user = sign_up
                    profile = profile_form.save(commit=False)
                    profile.passwordConfirm = make_password(profile_form.cleaned_data['passwordConfirm'])
                    profile.user = user
                    profile.save()
                    return render(request, "ui_app/utilisateurs.html", {"users": users, 'status': True})
                else:
                    return render(request, "ui_app/addUser.html", {'status': True})
            #return redirect("utilisateurs")
    return render(request, "ui_app/addUser.html", {'user_form': user_form,
    'profile_form': profile_form})

# page update pssword user


def updatePassword(request, email):
    if request.method == "GET":
        return redirect("utilisateurs")
    elif request.method == "POST":
        return render(request, "ui_app/updatePassword.html", {'email': email})


def validateUpdatePassword(request, email):
    if request.method == "GET":
        return redirect("utilisateurs")
    elif request.method == "POST":
        userUpdated = User.objects.filter(email=email)
        ProfileUpdated = Profile.objects.filter(user_id=userUpdated.first().id)
        
        mdpUpdated = request.POST.get("mdp")
        mdpConfirmUpdated = request.POST.get("mdpConfirm")
        if mdpUpdated == mdpConfirmUpdated:
            userUpdated.update(password=make_password(mdpUpdated))
            ProfileUpdated.update(passwordConfirm=make_password(mdpUpdated))
            return redirect("utilisateurs")
        else:
            return render(request, "ui_app/updatePassword.html", {'email': email, 'status': True})

# methode de supprimer un utilisateur


def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('/ui_app/utilisateurs')
    return render(request, 'ui_app/utilisateurs.html', {'user': user})


def statistiques(request):
    # locataire
    usersLocataire = User.objects.filter(profile__profil='Locataire').count
    # locateur
    usersLocateur = User.objects.filter(profile__profil='Locateur').count
    # chambre
    chambres = Chambre.objects.all().count
    # reservation
    reservations = Reservation.objects.all().count
    #reservation >> en attente
    reservationPending = Reservation.objects.filter(status='P').count
    #reservation >> expirée
    reservationExpired = Reservation.objects.filter(status='E').count
    #reservation >> active
    reservationActive = Reservation.objects.filter(status='A').count
    #benefice 
    #***********************
    #*******************
    #ne fonctionne pas si j'essaie de calculer la somme
    #Reservation.objects.all().annotate(tota=Sum('total'))

    totalpr = 1
   
    benefice = ((totalpr)* 25/100) 
    return render(request, 'ui_app/statistiques.html',
                  {'usersLocataire': usersLocataire, 'usersLocateur': usersLocateur, 
                  'chambres': chambres, 'reservations': reservations,'reservationPending':reservationPending,
                  'reservationExpired':reservationExpired,
                  'reservationActive':reservationActive,'total':totalpr, 'benefice': benefice})
