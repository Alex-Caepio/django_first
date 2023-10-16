from datetime import datetime
from django.db import models
from django.db.models import signals
from django.db.models.signals import pre_save
from django.dispatch import receiver

CREATED = 'created'
UPDATED = 'updated'
DELETED = 'deleted'


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    status = models.CharField(max_length=100, default=CREATED)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.text


# @receiver(signals.pre_save, sender=Post)
# def post_save_handler(sender, instance, **kwargs):
#     raise Exception('Error')


# pre_save.connect(post_save_handler, sender=Post)

@receiver(signals.post_save, sender=Post)
def post_save_handler(sender, instance, **kwargs):
    if Post.objects.filter(category=instance.category).count() >= MAX_COUNT_PER_CATEGORY.get(instance.category,
                                                                                             DEFAULT_MAX_COUNT):
        Post.objects.filter(category=instance.category).order_by('created_at').first().delete()
        print("Deleted!")


MAX_COUNT_PER_CATEGORY = {
    'science': 2,
    'math': 3,
    'history': 4,
}

DEFAULT_MAX_COUNT = 5
