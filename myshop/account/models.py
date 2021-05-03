from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    address = models.CharField(max_length=250, default='', blank=True)
    postal_code = models.CharField(max_length=20, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=10, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user/%Y/%m/%d',
                              blank=True)

    def __str__(self):
        return 'Profil użytkownika {}.'.format(self.user.username)