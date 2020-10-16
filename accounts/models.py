from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # job_description=models.CharField('Должность', max_length=100, default='-')
    # phone_number=models.CharField('Номер телефона',max_length=15, default='-')
    pass
