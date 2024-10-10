from django.db import models

class Job(models.Model):
    jobLink = models.CharField(max_length=10000000)
    dateApplied = models.IntegerField()

    def __str__(self):
        return self.title
