from django.db import models

from django.contrib.auth.models import User

from django.urls import reverse

# Create your models here.
#创建文章分类
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
#文章标签
class Tag(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
#文章类
class Post(models.Model):
    title=models.CharField(max_length=70)
    body=models.TextField()
    created_time=models.DateTimeField()#创建时间
    modified_time=models.DateTimeField()#更新时间
    excerpt = models.CharField(max_length=200,blank=True)#摘要
    category=models.ForeignKey(Category)
    tag=models.ManyToManyField(Tag,blank=True)
    author=models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Bk:detail',kwargs={'pk':self.pk})
    #对文章列表进行排序，首先依据created_time进行排序，-表示逆序排序，如果顺序相同，再以title排序。
    class Meta:
        ordering=['-created_time','title']
