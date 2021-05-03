from django.db import models
from django.db.models.fields import *


class UserModel(models.Model):
    name = CharField(max_length=200)
    surname = CharField(max_length=200)
    university = CharField(max_length=200)
    faculty = CharField(max_length=200)
    email = EmailField(max_length=50)
    phone = FloatField(max_length=12)
    city = CharField(max_length=200)

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.university


class ProjectModel(models.Model):
    project_owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    subject = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.title
