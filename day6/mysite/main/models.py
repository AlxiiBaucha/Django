from django.db import models

# models.py

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()

    def __str__(self):
        return self.title


