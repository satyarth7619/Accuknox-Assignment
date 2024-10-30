# The synchronous behavior defined a (post_save) "signal" that takes some time to finish.

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(5) 
    print("Signal handler finished")
    
user = User.objects.create(username="testuser")
print("User saved")
