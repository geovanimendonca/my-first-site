from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cpf_field.models import CPFField





class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Exam = models.CharField(max_length=35)
    Pacient = models.CharField(max_length=50)
    #SCORE_CHOICES = zip( range(1,), range(1,n) )
    #Cpf_pacient = models.IntegerField(choices=SCORE_CHOICES, blank=False)
    Cpf_pacient = CPFField('cpf')
    Observations = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.TextField()
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Exame
  
'''
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
'''   