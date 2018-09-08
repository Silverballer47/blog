from django import template
from ..models import Post,Category

register = template.Library()
#最新文章标签
@register.simple_tag
def get_rencent_posts():
    return Post.objects.all().order_by('-created_time')[:2]


#归档模板标签
#这里dates方法返回一个列表，列表每一个元素为每一篇文章（post）的创建时间，且是python的date对象，精确到月份，降序排列。例如我们写了 3 篇文章，分别发布于 2017 年 2 月 21 日、2017 年 3 月 25 日、2017 年 3 月 28 日，那么 dates 函数将返回 2017 年 3 月 和 2017 年 2 月这样一个时间列表，且降序排列，从而帮助我们实现按月归档的目的。
@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month',order='DESC')

#分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()

