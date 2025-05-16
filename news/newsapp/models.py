from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return f"<User {self.username}>"
    

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    source = models.CharField()

    def __str__(self):
        return f"<News {self.title}>"