from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# from django.db.models.signals import post_save
# from django.dispatch import receiver
from django.db import IntegrityError



# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    Name = models.TextField(default="Mike")

    def save_profile(self):
      self.save()
  
    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile
    
    

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 65)
    question = models.TextField(max_length=300)
    author_name = models.CharField(max_length=50,default='Anonymous')
    date_written = models.DateField(auto_now=True)
            
    def __str__(self):
        return self.title

    @classmethod
    def get_user_name(cls, id):
        return cls.objects.filter(user__id=id)

    def get_absolute_url(self):
        return reverse("home")
    



class Comment(models.Model):
    user= models.ForeignKey(User)
    post=models.ForeignKey('Post',null=True)
    comment= models.CharField(max_length=100)
    posted_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
