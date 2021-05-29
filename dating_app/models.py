from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # https://docs.djangoproject.com/en/3.2/ref/contrib/auth/

    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('', 'Unspecified'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='')

    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)

    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
