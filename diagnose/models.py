from django.db import models
from django.urls import reverse
# Create your models here.

class Diagnose(models.Model):
    diagnoseName = models.CharField(max_length=255)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.diagnoseName


    def get_absolute_url(self):
            return reverse('diagnoses')