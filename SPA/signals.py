import random, string
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Question

@receiver(pre_save, sender=Question)
def addSlug(sender, instance, *args, **kWArgs):
    if instance and not instance.slug:
        instance.slug = slugify(instance.content)+"-"+"".join(random.choice(string.digits) for _ in range(3))
