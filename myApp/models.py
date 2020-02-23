from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length = 18)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.username)


class Project(models.Model):
    submissionDate = models.DateTimeField(auto_now_add = True, auto_now = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 20)
    pitch = models.CharField(max_length = 140)


    def __str__(self):
        return self.title