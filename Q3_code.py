# We create a user and a corresponding user profile when the user is saved.
# If there is an error that causes a rollback and check if the profile was also rolled back.

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.models import UserProfile 


@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    UserProfile.objects.create(user=instance)
    print("UserProfile created for:", instance.username)
try:
    with transaction.atomic():
        user = User.objects.create(username="testuser")
        raise Exception("Simulated error")
except Exception as e:
    print("Error occurred, rolling back:", e)
    
profile_exists = UserProfile.objects.filter(user__username="testuser").exists()
print("Was UserProfile saved?", profile_exists)
