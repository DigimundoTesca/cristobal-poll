from django.db import models
from django.core.validators import RegexValidator

class Poll(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Debe ingresar un número telefónico de 10 dígitos.",
    )

    name = models.CharField(max_length=90, default='')
    last_name = models.CharField(max_length=190, default='')
    last_module = models.CharField(max_length=120, default='')
    email = models.EmailField(default='', unique=True)
    phone_number = models.CharField(
        unique= True,
        max_length=10,
        validators=[phone_regex],
        error_messages={
            'unique': "Este número ya está registrado.",
        },
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'encuesta'
        verbose_name_plural = 'encuestas'
