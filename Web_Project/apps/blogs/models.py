from django.db import models
from apps.core.models import DateTimeModel
from django.contrib.auth import get_user_model


USER = get_user_model()
# Create your models here.
class Blog(DateTimeModel):
    STATUS_CHOICE = (
        ('draft', 'draft'),
        ('published', 'published') #('s' , ' small ') ==> saved as S
    )
    author = models.ForeignKey(USER, on_delete = models.CASCADE , related_name = 'blog_user')# related_name is used to make reverse query
    title = models.CharField( max_length = 250)
    #slug = models.SlugField(max_length = 250 , uniq...)
    status = models.CharField( max_length = 10 , choices = STATUS_CHOICE , default = 'draft')


# class Model1:
#     our_field
#     pass
#
# class Model2:
#     m1 = Foreign key filed of Model1
#
# class Model3:
#     m2 = foreign key relation with model2
#
# m = Mdoel3.objects.all()
# F('m2__m1__our_field')
