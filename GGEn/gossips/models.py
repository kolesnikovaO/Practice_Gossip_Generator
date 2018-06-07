from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Gossip(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    gossip_text = models.CharField(max_length=2048,null=False)
    create_date = models.DateTimeField(null=False)
    expire_date = models.DateTimeField(null=True)
    character_id = models.ForeignKey('Character', on_delete=models.CASCADE)
    is_enabled = models.BooleanField(null=False)
    def __str__(self):
        """
        String for reflecting gossip text
        """
        return self.gossip_text[0:20]


class Character(models.Model):
    name = models.CharField(max_length=200,null=False)
    about = models.CharField(max_length=800,null=False)
