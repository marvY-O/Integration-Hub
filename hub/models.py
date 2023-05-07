from django.db import models

# Create your models here.
class SchemaDetails(models.Model):
    bank = models.CharField(max_length = 10, default = None)
    schema = models.CharField(max_length = 100000, default = None)
    
    def __str__(self):
        return self.bank