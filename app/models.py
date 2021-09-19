from django.db import models


class Task(models.Model):
    task = models.CharField(max_length=256, null=False)
    person = models.CharField(max_length=126, null=False)

    def __str__(self):
        return f"{self.task}, {self.person}"
