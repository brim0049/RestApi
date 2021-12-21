from django.db.models import fields
from rest_framework import serializers
from ui_app.models import Ville, Reservation, Chambre, Profile
from django.contrib.auth.models import User

class VilleSerrializers(serializers.ModelSerializer):
    class Meta:
        model = Ville
        fields =("id", "ville")

class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields =("id", "chambre", "locateur", "locataire", "nbr_personnes", "in_date", "out_date", "total", "status")

class ChambreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chambre
        fields=("id", "ville", "locateur", "capacite", "prix")

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password")

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("profil","genre")

class UserSerializer(serializers.ModelSerializer):
    profil= ProfilSerializer(source = "profile")
    class Meta:
        model = User 
        fields = ("email", "password","username","last_login", "profil")  # "profil","genre",