from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TaskList(models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task +"-"+str(self.done)