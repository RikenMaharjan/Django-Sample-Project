from django.contrib.auth import get_user_model
from django.db import models
from apps.core.models import DateTimeModel
#from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

USER = get_user_model()

class Profile(DateTimeModel):
    image = models.ImageField( upload_to='user/', blank = True)
    # phonenumber = PhoneNumberField(); # from django-phonenumber-field 
    user = models.OneToOneField(USER, on_delete = models.CASCADE, related_name = 'user_kp_profile')

    def __str__(self):
        return f"user {self.user} profile"
