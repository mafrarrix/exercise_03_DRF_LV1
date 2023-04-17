from django.db import models

class JobOffer(models.Model):
    
    company_name = models.CharField(max_length=50)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=30)
    job_description = models.TextField()
    salary = models.IntegerField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    create_at = models.DateField()
    avabile = models.BooleanField(default=True)
    
    
    def __str__(self):
        return f"{self.company_name} {self.job_title}"
        
