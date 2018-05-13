from django.db import models

class Article(models.Model):
    title=models.CharField(max_length=32,default='Title')
    content=models.TextField(null=True)      # 允许它为空

    def  __str__(self):               # 使得admin中显示标题而不是object
        return self.title
