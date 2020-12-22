from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    memo = models.TextField(blank=True, verbose_name="Memo")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    