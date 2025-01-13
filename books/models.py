from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,max_length=255)
    content  = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    cover = models.CharField(max_length=255, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("book_details", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_at']
        def __unicode__(self):
            return self.title