from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Activity(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.category

class Schedule(models.Model):
    date = models.DateField()
    activities = models.ManyToManyField(Activity)

    def __str__(self):
        return str(self.date)