from django.db import models


class LogModel(models.Model):
    time_start = models.TimeField(auto_now_add=True)
    time_end = models.TimeField(auto_now_add=True)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.date}'
