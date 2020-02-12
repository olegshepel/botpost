from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    created_by = models.ForeignKey(User, verbose_name='user', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField('description', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='user_likes', verbose_name='user likes', blank=True)

    def __str__(self):
        return '{}{}'.format(self.created_by, self.description)

    def like(self, user):
        self.likes.add(user)

    def dislike(self, user):
        self.likes.remove(user)
