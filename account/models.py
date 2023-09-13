
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    avatar = models.FileField(upload_to='account',blank=True,null=True)
    locations = models.CharField(max_length=100,null=True,blank=True)

#yeni bir user kaydi olustugu zaman onunla baglanti kurup profile objesinide olusturuyor
@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#bir user kaydi guncellendigi zaman onunla baglanti kurup profile objesinide guncelliyor
@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()

