
from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Text(models.Model):
    searched_text = CharField(max_length = 255, blank=True, null=True)