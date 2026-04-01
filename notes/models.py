from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self) -> str:
        return f"{self.owner}: {self.content[:10]}"