from django.db import models
class VCard(models.Model):
    name=models.CharField(max_length=150)
    contact=models.BigIntegerField()
    def __str__(self):
        return self.name