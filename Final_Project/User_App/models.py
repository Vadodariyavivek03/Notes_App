from django.db import models

# Create your models here.

class UserSignup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=15)
    mobile=models.BigIntegerField()
    profile_image = models.ImageField(upload_to="profile_images/", blank=True, null=True)

    def __str__(self):
        return self.fullname

class mynotes(models.Model):
    uploaded_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(UserSignup, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    desc=models.TextField()
    subject=models.CharField(max_length=50)
    notes_file=models.FileField(upload_to='Notes_Data')
    status_opt=[
        ('Pending','Pending'),
        ('Approve','Approve'),
        ('Rejected','Rejected')
    ]
    status=models.CharField(max_length=10, choices=status_opt, default='Pending')
    updated_at=models.DateTimeField(blank=True, null=True)

class contact(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fullname=models.CharField(max_length=50)
    email=models.EmailField()
    msg=models.TextField()