from django.db import models

# Create your models here.
class links(models.Model):
    link_address=models.CharField(max_length=500,null=True,blank=True)
    link_name=models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.link_name