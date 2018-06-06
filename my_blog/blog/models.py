from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    category = models.ForeignKey(to='Category',default=None,blank=True)
    # class Meta:
    #     ordering = ('-pk',)


class Category(models.Model):
    category_name = models.CharField(max_length=150,unique=True)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return u'%s' % self.category_name


