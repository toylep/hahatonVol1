from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class Specialization(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField("auth.User", related_name='specs')

    def __str__(self) -> str:
        return self.name

class MySession(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    session_id = models.TextField()
    tg_token = models.TextField(default="")
    expiration_time = models.DateTimeField()

    @classmethod
    def create_session(cls, user, session_id,token):
        expiration_time = timezone.now() + timedelta(minutes=1)
        return cls.objects.create(user=user, session_id=session_id, expiration_time=expiration_time,tg_token=token)

    @classmethod
    def get_session(cls, session_id):
        try:
            return cls.objects.get(session_id=session_id)
        except cls.DoesNotExist:
            return None

    def is_expired(self):
        return self.expiration_time < timezone.now()

    def delete_session(self):
        self.delete()


# class 