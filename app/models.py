from django.db import models


class Task(models.Model):
    task = models.CharField(max_length=256, null=False)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
