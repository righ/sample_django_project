import uuid

from django.db import models
from django.utils import timezone

# Create your models here.


class Status(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=10)
    description = models.TextField(default='', blank=True)

    def __str__(self):
        return f'{self.name} ({self.id})'


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    user = models.ForeignKey('accounts.User', null=True, on_delete=models.CASCADE)
    group = models.ForeignKey('accounts.Group', null=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.id})'


class Task(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    content = models.TextField(default='')

    tags = models.ManyToManyField(Tag)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_at} ({self.id})'


class Time(models.Model):
    id = models.BigAutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='times')
    note = models.TextField(default='')
    start = models.DateTimeField()
    end = models.DateTimeField(null=True)

    def __str__(self):
        return '{start}-{end}'.format(start=self.start, end=self.end)