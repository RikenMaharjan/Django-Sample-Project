from django.db import models

from apps.core.models import DateTimeModel


class Product(DateTimeModel):
    name = models.CharField(max_length=150, blank=False, null=False)
    title = models.CharField(max_length=150, blank=False, null=False)
    price = models.DecimalField(default=0, blank=False, null=False, max_digits=3, decimal_places=2)

    def save(self, force_insert = False , force_update = False , using = None , update_fields = None):

        
        """
        Is called when the object.create() method is called,
        when object.save() mehtod is called
        """
        self.title = self.title + 'suffix '
        super().save()
        

    def get_absolute_url(self):
        
     pass
