# It prints the thread ID of both the sender and the signal handler and if they match
# it proves that signals run in the same thread as the caller

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    print("Signal handler thread ID:", threading.get_ident())

print("Sender thread ID:", threading.get_ident())
user = User.objects.create(username="testuser")

