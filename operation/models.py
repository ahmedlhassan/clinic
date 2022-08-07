from django.db import models

# Create your models here.
class Operation(models.Model):
    operationName = models.CharField(max_length=255)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.operationName