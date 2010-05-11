from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    reg_date = models.DateTimeField()
    email = models.EmailField()
    intro = models.TextField(max_length=4096)

    def __unicode__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    embed_code = models.CharField(max_length=500)
    posted_by = models.ForeignKey(User)
    post_date = models.DateTimeField()
    category = models.CharField(max_length=30)
    tags = models.CharField(max_length=60)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    subject = models.ForeignKey(Video)
    user = models.ForeignKey(User)
    email = models.EmailField(blank=True)
    pub_date = models.DateTimeField()
    context = models.TextField(max_length=4096)
    from_addr = models.URLField()

    def __unicode__(self):
        return self.subject
