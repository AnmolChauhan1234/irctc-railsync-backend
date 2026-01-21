from django.db import models

class Train(models.Model):
    train_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)

    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.train_number} - {self.name}"
