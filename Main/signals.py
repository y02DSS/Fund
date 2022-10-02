from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Collection
from django.template.defaultfilters import slugify

# @receiver(pre_save, sender=User)
# def pre_smy_callbackave(sender, instance, *args, **kwargs):
#     instance.comment = slugify(instance.name)
#     instance.save(phone=instance.name)
#     super(User, instance).pre_save(sender, instance, *args, **kwargs)
#     # instance.Model.save(instance)
#     print("Request finished!")


@receiver(post_save, sender=Collection)
def my_save(sender, instance, *args, **kwargs):
    pass
    # models.Model.save(instance)