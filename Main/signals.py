from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from .models import UserAccount, ShelterAccount
from django.template.defaultfilters import slugify

from .send_email import send_for_email


@receiver(post_init, sender=UserAccount)
def my_not_save(sender, instance, *args, **kwargs):
    instance.pre_register_user = instance.register_user

@receiver(post_save, sender=UserAccount)
def my_save(sender, instance, *args, **kwargs):
    if instance.register_user == 'Принять' and instance.pre_register_user == 'Отклонить':
        send_for_email(str(instance.email), 'Ваши данные для входа:', f"Ваш email: {instance.email}\nВаш пароль: {instance.password}", "Успешная регистрация!")



@receiver(post_init, sender=ShelterAccount)
def my_not_save(sender, instance, *args, **kwargs):
    instance.pre_register = instance.register

@receiver(post_save, sender=ShelterAccount)
def my_save(sender, instance, *args, **kwargs):
    if instance.register == 'Принять' and instance.pre_register == 'Отклонить':
        send_for_email(str(instance.email), 'Ваши данные для входа:', f"Ваш email: {instance.email}\nВаш пароль: {instance.password}", "Успешная регистрация!")
