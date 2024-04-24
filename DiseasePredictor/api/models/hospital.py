from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Specialty(models.Model):
    name_of_specialty = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.name_of_specialty)


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.CASCADE,
    )
    experience = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=255)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    days_available = models.TextField(max_length=255)
    time_available = models.TextField(max_length=255)

    def __str__(self) -> str:
        return str(self.name) + " " + str(self.specialty)
