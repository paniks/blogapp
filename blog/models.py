from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    '''Example of custom model manager. Filter QuerySet by column 'status' with value 'published' '''
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                                            .filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'),
                      ('published', 'Published'))

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               related_name='blog_posts',
                               on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    objects = models.Manager()  # default manager
    published = PublishedManager()  # custom manager

    class Meta:
        ordering = ('-publish',)    # that's responds for sorting posts by publish date, minus means descending order

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])


class Comments(models.Model):
    post = models.ForeignKey(Post,
                             related_name='comments',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment added by {} to post {}'.format(self.name, self.post)
