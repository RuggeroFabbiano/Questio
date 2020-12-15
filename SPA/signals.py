"""
Signals for SPA app.
"""

import random
import string
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Question

@receiver(pre_save, sender=Question)
def add_slug(sender, instance, *args, **kWArgs):
    """
    Creates slug for question (from question name + random digits)
    """
    if instance and not instance.slug:
        slug_name = slugify(instance.content)
        random_digits = "".join(random.choice(string.digits) for _ in range(3))
        instance.slug = slug_name + "-" + random_digits
