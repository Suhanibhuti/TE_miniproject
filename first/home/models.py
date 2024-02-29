from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# Create your models here.
class pdM(models.Model):
    Fname= models.CharField(max_length =122)
    RN=models.CharField(max_length =122)
    DOB=models.DateField()
    Email=models.CharField(max_length =122)
    MN=models.IntegerField(null=True)
    Gen=models.CharField(max_length =122)
    Caddr=models.CharField(max_length =122)
    Paddr=models.CharField(max_length =122)
    
    Ftname=models.CharField(max_length =122)
    Email1=models.CharField(max_length =122)
    MN1=models.IntegerField(null=True)
    
    Mtname=models.CharField(max_length =122)
    Email2=models.CharField(max_length =122)
    MN2=models.IntegerField(null=True)
    
    Stdmentor=models.CharField(max_length =122)
    EmailM=models.CharField(max_length =122)
    MNstdm=models.IntegerField(null=True)
    
    Factmentor=models.CharField(max_length =122)
    EmailF=models.CharField(max_length =122)
    MNfactm=models.IntegerField(null=True)
    
    dep=models.CharField(max_length =122)
    
    def __str__(self):
        return self.Fname
    

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name    
  
class attM(models.Model):
    month=models.CharField(max_length=122)
    percentage=models.IntegerField(null=True)
    # category=models.CharField(max_length=122)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(pdM, on_delete=models.CASCADE)

    def clean(self):
        super().clean()
        if self.category_id and attM.objects.filter(category=self.category).count() >= 3:
            raise ValidationError("The Semester can be only selected thrice!")

    def save(self, *args, **kwargs):
        self.full_clean()  # Validate before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category.name} - {self.month}" if self.category else self.month
    
    
class adM(models.Model):
    adSem= models.CharField(max_length=50)
    at1=models.IntegerField(null=True)
    at2=models.IntegerField(null=True)
    ia1=models.IntegerField(null=True)
    ia2=models.IntegerField(null=True)
    prelim=models.IntegerField(null=True)
    endsem=models.IntegerField(null=True)
    perf=models.CharField(max_length =122)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default =1) 
       
    def __str__(self):
        return f"{self.user.username}'s academic details for {self.adSem}"
        

class cocuM(models.Model):
    sem = models.CharField(max_length=20, default=1)
    professional_society = models.TextField()
    internship = models.TextField()
    paper_published = models.TextField()
    user_profile = models.ForeignKey(pdM, on_delete=models.CASCADE)


    def __str__(self):
        return self.sem


class excoM(models.Model):
    exsem = models.CharField(max_length=20, default=1)
    sports = models.TextField()
    nss = models.TextField()
    price = models.TextField()
    user_profile = models.ForeignKey(pdM, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.exsem
    
    
class plcM(models.Model):
    compname=models.CharField(max_length =122)
    package = models.DecimalField(max_digits=10, decimal_places=2)
    semester = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='placements')
    
    def __str__(self):
        return f"{self.compname} - {self.package} - Semester {self.semester} "

# class hsM(models.Model):
#     gre=models.CharField(max_length =122)
#     tofel=models.CharField(max_length =122)
#     cat=models.CharField(max_length =122)
    
#     def __str__(self):
#         return self.semester