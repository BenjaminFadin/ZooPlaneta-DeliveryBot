from django.db import models
from shared.models import BaseModel

UZ = "uz"
RU = "ru"


class User(BaseModel):
    LANGUAGE_CHOICE = (
        (UZ, 'uz'),
        (RU, 'ru'),
    )

    tg_user_id = models.PositiveIntegerField(unique=True)
    phone_number = models.CharField(max_length=12)
    lang = models.CharField(max_length=2, choices=LANGUAGE_CHOICE, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    username = models.CharField(max_length=30, null=True)
    first_name = models.CharField(max_length=25, null=True)
    last_name = models.CharField(max_length=25, null=True)

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'User'

    def __str__(self):
        user_info = f"ID: {self.tg_user_id}, {self.username}"
        return user_info

