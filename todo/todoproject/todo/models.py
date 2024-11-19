from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)  # Görev başlığı
    description = models.TextField(blank=True)  # Görev açıklaması
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Görev atanan kullanıcı
    is_completed = models.BooleanField(default=False)  # Görev tamamlanma durumu

    def __str__(self):
        return self.title
