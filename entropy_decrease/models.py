from django.db import models

# Create your models here.
class Item(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Score(models.Model):
    id = models.AutoField(primary_key=True)  # 自动创建的ID字段
    total_score = models.IntegerField()
    target_score = models.IntegerField(default=0)
    owner_id = models.IntegerField()
    min = models.IntegerField(default=1)
    max = models.IntegerField(default=100)
    def __str__(self):
        return f"ID: {self.id}, Total Score: {self.total_score}"

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Todo_item(models.Model):
    id = models.AutoField(primary_key=True)
    owner_id = models.IntegerField()
    description = models.TextField()
    random_score = models.IntegerField()
    done = models.BooleanField()
    def __str__(self):
        return f"{self.id}"
    