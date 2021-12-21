from django.db import models
from django.shortcuts import get_object_or_404, render
from rest_framework import response
from django.contrib.auth.models import User
# from ui_app.models import User
from ui_app.models import Ville,Reservation, Chambre
from django.contrib.auth.hashers import check_password, make_password

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .serializers import VilleSerrializers, ReservationSerializers, ChambreSerializers, LoginSerializer, UserSerializer, ProfilSerializer

from drf_yasg.utils import swagger_auto_schema

# Create your views here.

#/api/towns

class VilleViewSet(viewsets.ViewSet):
    @swagger_auto_schema(
        tags=["Towns"], responses={200: VilleSerrializers(many=True)}
    )
    def list(self, request):
        
        villes = Ville.objects.all()
        villes_serializer = VilleSerrializers(villes, many = True)

        return Response({"data" : villes_serializer.data}, status = status.HTTP_200_OK)

#/api/reservations

class ReservationsViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        tags=["Reservations"], responses={200: ReservationSerializers(many=True)}
    )
    def list(self, request):
       token_key = request.META["HTTP_AUTHORIZATION"].split(" ")[1]   # recuperer le token
       user = Token.objects.filter(key=token_key).first().user
       reservations= (user.locataire.all() | user.locateur.all())
       reservations_serializer = ReservationSerializers(reservations, many = True)
       return Response({"data" : reservations_serializer.data}, status = status.HTTP_200_OK)
     
    @swagger_auto_schema(
        tags=["Reservations"], request_body = ReservationSerializers
    )
    def create(self, request):
        nbr_personnes = request.data["nbr_personnes"]
        in_date = request.data["in_date"]
        out_date = request.data["out_date"]
        total = request.data["total"]
        status1 = request.data["status"]
        chambre = Chambre.objects.get(id = request.data["chambre"])
        locataire = User.objects.get(id = request.data["locataire"])
        locateur =  User.objects.get(id = request.data["locateur"])
        reservation = Reservation.objects.create(
            nbr_personnes=nbr_personnes,
            in_date=in_date,
            out_date=out_date,
            total=total, 
            status=status1, 
            chambre=chambre, 
            locataire=locataire, 
            locateur=locateur )

        return Response(
            {
                "message": "La reservation avec l'Id : {} est créée !".format(reservation.id)
            },
        status = status.HTTP_201_CREATED
        )

#/api/reservation/{reservation_id}

class ReservationViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Reservation"], responses={200: ReservationSerializers(many=False)}
    )
    def retrieve(self, request, pk):
        token_key = request.META["HTTP_AUTHORIZATION"].split(" ")[1]   # recuperer le token
        user = Token.objects.filter(key=token_key).first().user
        reservations= get_object_or_404(user.locataire, pk=pk)
        reservations_serializer = ReservationSerializers(reservations)
        return Response({"data" : reservations_serializer.data}, status = status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=["Reservation"], request_body = ReservationSerializers
    )
    def update(self, request, pk=None):
        token_key = request.META["HTTP_AUTHORIZATION"].split(" ")[1]   # recuperer le token
        user = Token.objects.filter(key=token_key).first().user
        nbr_personnes = request.data["nbr_personnes"]
        in_date = request.data["in_date"]
        out_date = request.data["out_date"]
        total = request.data["total"]
        status1 = request.data["status"]
        chambre = Chambre.objects.get(id = request.data["chambre"])
        locataire = User.objects.get(id = request.data["locataire"])
        locateur =  User.objects.get(id = request.data["locateur"])
        user.locataire.filter(id=pk).update(nbr_personnes=nbr_personnes,
            in_date=in_date,
            out_date=out_date,
            total=total, 
            status=status1, 
            chambre=chambre, 
            locataire=locataire, 
            locateur=locateur)
        return Response({"message": "La reservation a ete modifiee !"},status = status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=["Reservation"]
    )
    def destroy(self, request,pk):
        reservation = get_object_or_404(Reservation, pk=pk)
        reservation.delete()
        return Response(status=204)

#/api/rooms

class ChambreViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Rooms"], responses={200: ChambreSerializers(many=True)}
    )
    def list(self, request):
        token_key = request.META["HTTP_AUTHORIZATION"].split(" ")[1]   # recuperer le token
        user = Token.objects.filter(key=token_key).first().user
    #    user_filter = user.objects.filter(profile__profil='Locateur')

      #  if(user_filter.exists()):
        chambres = user.chambre_set.all()
        chambres_serializer = ChambreSerializers(chambres, many = True)
        return Response({"data" : chambres_serializer.data}, status = status.HTTP_200_OK)
        # else:
        #     return Response({"message" : "l'utilisateur n'est pas un locateur !" }, status = status.HTTP_200_OK)



    @swagger_auto_schema(
        tags=["Rooms"], request_body = ChambreSerializers 
    )
    def create(self, request):
        
        ville =  Ville.objects.get(id = request.data["ville"])
        locateur = User.objects.get(id = request.data["locateur"])
        capacite = request.data["capacite"]   
        prix = request.data["prix"]   

        chambre = Chambre.objects.create(ville = ville, locateur = locateur, capacite = capacite, prix = prix)

        return Response({"message": "La chambre avec l'Id : {} est créée !".format(chambre.id)},status = status.HTTP_200_OK)

# /api/room/{room_id}

class RoomViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Room"], responses={200: ChambreSerializers(many=False)}
    )
   
    def retrieve(self, request, pk):
        token_key = request.META["HTTP_AUTHORIZATION"].split(" ")[1]   # recuperer le token
        user = Token.objects.filter(key=token_key).first().user
        chambres= get_object_or_404(user.chambre_set.all(), pk=pk)
        chambres_serializer = ChambreSerializers(chambres)
        return Response({"data" : chambres_serializer.data}, status = status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=["Room"], request_body = ChambreSerializers 
    )
    def update(self, request, pk=None):
        ville =  Ville.objects.get(id = request.data["ville"])
        locateur = User.objects.get(id = request.data["locateur"])
        capacite = request.data["capacite"]
        prix = request.data["prix"]
        Chambre.objects.filter(id=pk).update(ville = ville, locateur = locateur, capacite = capacite, prix = prix)
        return Response({"message": "La chambre a ete modifiee !"},status = status.HTTP_200_OK)
    @swagger_auto_schema(
        tags=["Room"]
    )
    def destroy(self, request, pk):
        chambre = get_object_or_404(Chambre, pk=pk)
        chambre.delete()
        return Response(status=204)


#/api/user

class UserViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["User"], responses={200: UserSerializer(many = False)}
    )
    def list(self, request):
        token_key = request.META["HTTP_AUTHORIZATION"].split(" ")[1]   # recuperer le token
        user = Token.objects.filter(key=token_key).first().user
        
        user_serializer = UserSerializer(user, many = False)
        return Response({"data" : user_serializer.data}, status = status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=["User"], request_body= UserSerializer
    )
    def update(self, request,pk):
        email = request.data["email"]
        password = request.data["password"]
        username = request.data["username"]
        genre = request.data["genre"]
        profil = request.data["profil"]

        token_key = request.META["HTTP_AUTHORIZATION"].split(" ")[1]   # recuperer le token
        user = Token.objects.filter(key=token_key).first().user

        user.objects.update(email = email, password = password, username = username, genre = genre, profil = profil )

        return Response({"message": "L'utilisateur a ete modifiee !"},status = status.HTTP_200_OK)


# /api/login

@swagger_auto_schema(
    method="post", tags=["Authentication"], request_body=LoginSerializer
)
@api_view(['POST'])
def login(request):
    email = request.data["email"]
    password = request.data["password"]
    user = User.objects.filter(email=email)

    if(user.exists()):
        auth_success = check_password(password, user.first().password)

        if(auth_success):
            token = Token.objects.filter(user=user.first())

            if(token.exists()):
                return Response({"token" : "Token {}".format(token.first().key)}, status = status.HTTP_200_OK)
            else:
                token = Token.objects.create(user=user.first())
                return Response({"token" : "Token {}".format(token.key)}, status = status.HTTP_200_OK)

        else:
            return Response({"message" : "Mot de passe incorrect !"}, status = status.HTTP_404_NOT_FOUND)
    else:
        return Response({"message" : "L'utilisateur n'existe pas !"}, status = status.HTTP_404_NOT_FOUND)

#/api/logout

@swagger_auto_schema(method="get", tags=["Authentication"])
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout(request):
    token_key = request.META["HTTP_AUTHORIZATION"].split(" ")[1] # recuperer le token

    invalidated_token = Token.objects.filter(key=token_key).first() 
    invalidated_token.delete()

    return Response({"message" : "Deconnexion effectuée avec succès !"}, status = status.HTTP_200_OK)
