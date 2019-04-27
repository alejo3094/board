from django.db import models
from applications.user.models import Users

# Board is a model to represent a system's boards
class Board(models.Model):
    boardName = models.CharField(max_length=50, verbose_name="boardName")
    idPublic = models.BooleanField()
    usuario = models.ForeignKey(Users, on_delete=models.CASCADE)

