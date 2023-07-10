from django.db import models

# Create your models here.
class FamilyMembers(models.Model):
    name=models.TextField(default='None')
    mobile=models.BigIntegerField(default=0)
    occupation=models.TextField(default='None')
    income=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Expenses(models.Model):
    membername=models.ForeignKey(FamilyMembers)
    expense=models.IntegerField(default=0)
    purpose = models.TextField(default=None,max_length=120)
