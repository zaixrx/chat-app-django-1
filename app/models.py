from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class Message(models.Model):
    user = models.CharField(max_length=128)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}: {self.content} [{self.timestamp}]'