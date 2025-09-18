from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    college = models.CharField(max_length=150, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=120)
    level = models.CharField(max_length=50, choices=[('Beginner','Beginner'),('Intermediate','Intermediate'),('Advanced','Advanced')], default='Beginner')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"

    def get_update_url(self):
        return reverse('skill_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('skill_delete', kwargs={'pk': self.pk})

class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)
    proof_link = models.URLField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"

    def get_update_url(self):
        return reverse('achievement_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('achievement_delete', kwargs={'pk': self.pk})

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    file = models.FileField(upload_to='certificates/', blank=True, null=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"

    def get_update_url(self):
        return reverse('certificate_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('certificate_delete', kwargs={'pk': self.pk})
