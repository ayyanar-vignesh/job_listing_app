from django.db import models

# Create your models here.
job_choices=(
    ('python_developer','PYTHON_DEVELOPER'),
    ('frontend_developer','FRONTEND_DEVELOPER'),
    ('backend_developer','BACKEND_DEVELOPER'),

)
class Joblisting(models.Model):

    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=60)
    qualifications=models.CharField(max_length=60)
    jobs=models.CharField(max_length=50,choices=job_choices,default='python_developer')


    def __str__(self):
        return self.firstname
