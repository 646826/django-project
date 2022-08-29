from django.db import models

class OrgLink(models.Model):
    title = models.TextField()
    description = models.TextField()
    url = models.URLField()
    slug = models.SlugField()
    
    def __str__(self):
        return f"{self.title} - {self.url}"