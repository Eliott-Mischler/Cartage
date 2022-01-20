

from django.db import models
from django.utils import timezone


class Address(models.Model):
    street = models.CharField(max_length=60)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=40)

    def __str__(self):
        return ' '.join([self.street, str(self.zip_code), self.city])


class User(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    tel = models.IntegerField()
    car = models.BooleanField()
    rating = models.FloatField()
    total_votes = models.IntegerField()
    hours = models.IntegerField()

    def __str__(self):
        return self.email


class Trip(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_user", null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teacher_user", null=True)
    start = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='start_address')
    stop = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='stop_address')
    departure = models.DateTimeField()

    def has_passed(self):
        return self.departure > timezone.now()


class Message(models.Model):
    content = models.CharField(max_length=500)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    date = models.DateTimeField()



class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    contact = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact')



