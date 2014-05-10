from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=255, null=True)
    pub_date = models.DateTimeField()
    excerpt = models.TextField(null=True)
    text = models.TextField()
    header_image = models.FileField(upload_to='blog/%Y/%m/%d', null=True, blank=True)
    post_color = models.CharField(max_length=20, null=True)
    tags = models.CharField(max_length=80, blank=True)
    published = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])
