from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,default=None, null=True, on_delete=models.CASCADE)
   # email = models.EmailField(max_length=30, default="none")
    MET_CHOICES = (('Locataire', 'Locataire'), ('Locateur', 'Locateur'))
    profil = models.CharField(max_length=9, choices=MET_CHOICES)
    MET_GENDER = (('M', 'Male'), ('F', 'Female'))
    genre = models.CharField(max_length=9, choices=MET_GENDER, default="none")
    #lastTime = models.DateTimeField()
    passwordConfirm = models.CharField(max_length=15, default="none")
    def __str__(self):
        return self.user.username 

class Ville (models.Model):
    id = models.AutoField(primary_key=True)
    ville = models.CharField(max_length=30)

class Chambre(models.Model):
    id = models.AutoField(primary_key=True)
    ville = models.ForeignKey("Ville", on_delete=models.CASCADE)
    # je cherche à mettre une condition que user doit etre un locateur
    locateur = models.ForeignKey(User, on_delete=models.CASCADE)
    capacite = models.IntegerField()
    prix = models.FloatField()


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    chambre = models.ForeignKey("Chambre", on_delete=models.CASCADE)
    # meme chose
    locateur = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="locateur",null=True)
    locataire = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="locataire", blank=True, null=True)
    nbr_personnes = models.IntegerField()
    in_date = models.DateTimeField()
    out_date = models.DateTimeField()
    total = models.FloatField()
    MET_CHOICES = (('P', 'Pending'), ('A', 'Active'), ('E', 'Expired'))
    status = models.CharField(max_length=9, choices=MET_CHOICES)


    """ @receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save() """
