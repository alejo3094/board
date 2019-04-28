from django.db import models
from applications.board.models import Board
from applications.user.models import Users

# Create your models here.
class noteRequest(models.Model):
    STATE_CHOICES = (('ACCEPTED','ACCEPTED'), ('CANCELLED','CANCELLED'), ('WITHOUT_CHECKING','WITHOUT_CHECKING'))
    content = models.CharField(max_length=200,verbose_name="contenidoNoteRequest")
    userCreator = models.ForeignKey(Users, on_delete=models.CASCADE)
    boarDestiny = models.ForeignKey(Board, on_delete=models.CASCADE)
    requestState = models.CharField(max_length=30, choices=STATE_CHOICES)
