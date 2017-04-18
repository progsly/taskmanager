from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

TASK_STAUSES = (
    (0, 'Active'),
    (1, 'Done'),
)


class Task(models.Model):
    name = models.TextField(max_length=200)
    desc = models.TextField()
    owner = models.ForeignKey(User)
    status = models.SmallIntegerField(default=0, choices=TASK_STAUSES)

    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True, default=timezone.now())

    def __str__(self):
        return self.name


class Done(models.Model):
    task = models.ForeignKey(Task, blank=False)
    how_is_done = models.ForeignKey(User, blank=False)

    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True, default=timezone.now())

    def __str__(self):
        return "{0} - done by {1}".format(self.task, self.how_is_done)