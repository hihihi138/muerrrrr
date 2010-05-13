from django.db import models
from datetime import datetime

class User(models.Model):
    name = models.CharField(max_length=30)
    reg_date = models.DateTimeField(default=datetime.now())
    email = models.EmailField()
    intro = models.TextField(max_length=4096)

    def __unicode__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    flash_url = models.URLField()
    posted_by = models.ForeignKey(User)
    post_date = models.DateTimeField(default=datetime.now())
    category = models.CharField(max_length=30)
    tags = models.CharField(max_length=60)

    def save_vid(self):
	from datetime import datetime
	dt_string = datetime.strftime(self.post_date, "%Y%m%d%H%M%S")
	return dt_string[0:4] + "/" + dt_string[4:6] + "/" + dt_string[6:8] + "/" + dt_string[8:14]
    vid = property(save_vid)

    def __unicode__(self):
        return self.title
    class Meta:
	ordering = ['-post_date']

class Comment(models.Model):
    subject = models.ForeignKey(Video)
    user = models.ForeignKey(User)
    email = models.EmailField(blank=True)
    pub_date = models.DateTimeField(default=datetime.now())
    context = models.TextField(max_length=4096)
    from_addr = models.URLField(blank=True)

    def __unicode__(self):
        return self.subject

class Log(models.Model):
    log_title = models.CharField(max_length=100)
    log_content = models.TextField(max_length=4096)
    log_time = models.DateTimeField(default=datetime.now())
    
    def __unicode__(self):
	return self.log_title
    class Meta:
	ordering = ['-log_time']
