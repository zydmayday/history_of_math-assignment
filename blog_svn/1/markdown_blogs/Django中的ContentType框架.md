关于上一篇文章中提到的点击量插件，其中用到的一个很关键的技术就是Django中的[contentType][1]，个人觉得有必要好好掌握一下。

按照我的个人理解，`ContentType`表面上就是一个坯子，不代表任何具体的模型，通过传入相应`model`的名称，`app`名称等，可以变换成相应的模型，并能够提供一些该模型的属性和信息。

--------------------

####模型：
```
class ContentType
	app_label #对应的app名称
	model     #对应的model名称
	name      #model对应的verbose_name
```

####模型实例的方法：
> ContentType.get_object_for_this_type(**kwargs)[source]
> 我们可以通过`ContentType.objects.get([args])`来获得某一个具体的model，然后通过一系列的查询条件，获取对应的模型实例。

> ContentType.model_class()[source]
> 获取模型的class

例如：
```
>>> from django.contrib.contenttypes.models import ContentType
>>> user_type = ContentType.objects.get(app_label="auth", model="user")
>>> user_type
# <ContentType: user>
>>> user_type.model_class()
# <class 'django.contrib.auth.models.User'>
>>> user_type.get_object_for_this_type(username='Guido')
# <User: Guido>
``` 

####ContentTypeManager
既然是`model`，就肯定会涉及到Manager类，文档中介绍了此类的几个重要方法，这里就插件中用到的方法做一个示例：
```
>>> from django.contrib.auth.models import User
>>> user_type = ContentType.objects.get_for_model(User)
>>> user_type
# <ContentType: user>
```


####用法总结

文档中介绍了`ContentType`的两种功能：

1. 我们可以不用import具体的`models` `class`，而是将`app_label`和`model`作为参数传递给`contentType`来实时（runtime）的生成`model`对象和实例。
2. 在某一个`model`中加入`ContentType`属性，用于和其他指定的`model`相关联，这样就可以间接的操作那些`model`了。

当然，第二种方法肯定是比较常用的，比如我使用的hitcount插件，就是在他自己的HitCount模型中加入`ContentType`，用来和我的博文进行关联，从而记录每篇文章的点击量。

------------------

####在HitCount中的具体实践

models.py中的两个主要模型：
```
# 记录具体点击数以及和第三方model的关联
class HitCount(models.Model):
    hits            = models.PositiveIntegerField(default=0)
    modified        = models.DateTimeField(default=datetime.datetime.utcnow)
    content_type    = models.ForeignKey(ContentType,
                        verbose_name="content type",
                        related_name="content_type_set_for_%(class)s",)
    object_pk       = models.TextField('object ID')
    content_object  = generic.GenericForeignKey('content_type', 'object_pk')

# 记录每一次点击的信息
class Hit(models.Model):
    created         = models.DateTimeField(editable=False)
    ip              = models.CharField(max_length=40, editable=False)
    session         = models.CharField(max_length=40, editable=False)
    user_agent      = models.CharField(max_length=255, editable=False)
    user            = models.ForeignKey(AUTH_USER_MODEL, null=True, editable=False)
    hitcount        = models.ForeignKey(HitCount, editable=False)
```
我们主要关注有关ContentType的部分，这里使用的`ForeignKey`和`TextField`我们应该都很了解，那`generic.GenericForeignKey`是什么呢？查阅文档后发现这个是Django自带的语法，加上了这三行之后，就可以保存每一个HitCount实例具体关联的`model`及其`id`，从而进行操作。

添加HitCount：
```
# ctype是由ContentType.objects.get_for_model(obj)获得
# obj则是具体的模型实例
obj, created = HitCount.objects.get_or_create(content_type=ctype, object_pk=object_pk)
```
之后再将已经添加的HitCount实例作为参数，创建Hit即可。

----------------

####总结

至此，我们了解了`ContentType`的一些基本知识，并赋予实例进行了说明（从创建model到具体的添加操作），当然，实际的情况肯定要比上述所说的要复杂的多，例如，如何获取到具体的模型实例，如何设计custom_tag，如何进行判断与筛选（是否为有效点击）等等。

随着我对HitCount源代码更深入的了解，会继续剖析其工作原理，并在接下来的文章中与大家分享。







[1]: https://docs.djangoproject.com/en/dev/ref/contrib/contenttypes/