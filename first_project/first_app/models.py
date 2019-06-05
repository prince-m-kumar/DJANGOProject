from django.db import models

# Create your models here.
class Topic(models.Model):
    """docstring for Topic."""
    top_name = models.CharField(max_length=264,unique=True)
    # def __init__(self):
    #     super(Topic, self).__init__()
    #
    #
    def __str__(self):
        return self.top_name


class webPage(models.Model):
    """docstring for webPage."""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length = 264,unique=True)
    url= models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(webPage,on_delete=models.CASCADE)
    date = models.DateField()

    """docstring for AccessRecord."""
    def __str__(self):
        return str(self.date)


    # def __init__(self, arg):
    #     super(webPage, self).__init__()
    #     self.arg = arg
class User(models.Model):
    """docstring for User."""
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.CharField(max_length=264,unique=True)
    # def __init__(self):
    #     super(Topic, self).__init__()
    #
    #
    def __str__(self):
        return self.first_name
