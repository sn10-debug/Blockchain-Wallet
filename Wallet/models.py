from django.db import models

from hashlib import sha256

# Create your models here.


class Account(models.Model):
    Account_ID=models.AutoField
    Password=models.CharField(default="",max_length=8)
    Common_Public_Key=models.CharField(default="",max_length=64)
    Network_Public_keys=models.JSONField(default={"Solana":sha256("Not Valid".encode('utf-8')).hexdigest()})

    def __str__(self) -> str:
        return self.Common_Public_Key


# Python manage.py createsuperuser is used to create a new account in Django Administration

