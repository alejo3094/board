from django.db import models
from applications.board.models import Board
from applications.user.models import Users

# Note is a model to represent a systems's notes, for each board
class Note(models.Model):
    content = models.CharField(max_length=200,verbose_name="contenidoNota")
    userCreator = models.ForeignKey(Users, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)