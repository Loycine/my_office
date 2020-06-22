from django.db import models

# Create your models here.

class Category(models.Model):
    category_text = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_text

class Phrase(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='phrase')
    phrase_text = models.CharField(max_length=200)
    explanation = models.CharField(max_length=200)
