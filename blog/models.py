from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Posts(models.Model):
    pub_date = models.DateTimeField('date published')
    post_text = models.CharField(max_length=2000)
    post_title = models.CharField(max_length=30)
    post_id = models.AutoField(primary_key=True)


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, db_column="post_id",)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column="username",
    )
    pub_date = models.DateTimeField('date published', primary_key=True)
    comment = models.CharField(max_length=200)

