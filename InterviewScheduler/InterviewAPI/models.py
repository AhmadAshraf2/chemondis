from django.db import models
from django.contrib.auth.models import User


class Slot(models.Model):
    """
    class model for Interview object
    """
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)