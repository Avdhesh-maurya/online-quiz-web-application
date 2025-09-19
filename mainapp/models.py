from django.db import models
from django.contrib.auth.models import User  

class Question(models.Model):
    CATEGORY_CHOICES = [
        ("HTML", "HTML"),
        ("CSS", "CSS"),
        ("JavaScript", "JavaScript"),
        ("Python", "Python"),
        ("Django", "Django"),
        ("React", "React"),
        ("Express", "Express"),
        ("Tailwind", "Tailwind"),
        ("Node.js", "Node.js"),
        ("Angular", "Angular"),
        ("Vue", "Vue"),
        ("Bootstrap", "Bootstrap"),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    text = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255, blank=True, null=True)
    answer = models.CharField(max_length=255)  # store correct option text

    def __str__(self):
        return f"{self.category} - {self.text[:40]}"

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    score = models.IntegerField()
    total = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.category} ({self.score}/{self.total})"