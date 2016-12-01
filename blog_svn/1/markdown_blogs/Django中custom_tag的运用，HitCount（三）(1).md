Django中的template标签
=======

根据我个人对Django[官方文档][1]的理解，Django的文档主要分为两大类：一是template filter，用来对目标文本进行过滤处理，二是custom tags，用于对多个参数进行处理，类似于函数。

标签的初始化
=====

```
polls/
    __init__.py
    models.py
    templatetags/
        __init__.py
        poll_extras.py
    views.py
```
上述是如何建立一个自定义标签的文件，`poll_extra.py`就是我们的自定义标签文件。所有的自定义的方法都写在这个里面。
```
{% load poll_extras %}
```
上述代码写在template中，表示引用这个标签文件，并可以使用这个文件中的所有方法。

template filter
=====

```
from django import template

register = template.Library()

def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')
    
register.filter('cut', cut)
```
```
{{ somevariable|cut:"0" }}
```
上述代码表示创立一个标签并投入使用的完整过程。
value表示为需要进行过滤的对象，arg为使用时冒号后面的第一个参数，具体含义为将所有value中的arg全部删除掉。

所以说template filter主要的作用就是对已有的内容进行进一步的修整，达到自己想要的效果，一般情况下是够用了。

当然，我们也可以使用decorator的方式来给template filter做补充：
```
@register.filter
@stringfilter
def lower(value):
    return value.lower()
```
比如说如上述代码所示，第一个decorator表示不需要再另写代码进行注册，直接以函数名来进行注册；第二个decorator表示此value将会一直作为string类型存在，因为只有字符串在支持大小写的转换。

如上的decorator还有一些，例如`is_safe`， `needs_autoescape`和`expects_localtime`等，这里就不一一赘述，想要详细了解的可以查看Django的官方文档。

--------------

custom tags
==========

```
<p>This post was last updated at {% format_time blog_entry.date_updated "%Y-%m-%d %I:%M %p" %}.</p>
``` 
```
from django import template

def do_format_time(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, date_to_be_formatted, format_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires exactly two arguments" % token.contents.split()[0])
    if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
    return FormatTimeNode(date_to_be_formatted, format_string[1:-1])
```
```
class FormatTimeNode(template.Node):
    def __init__(self, date_to_be_formatted, format_string):
        self.date_to_be_formatted = template.Variable(date_to_be_formatted)
        self.format_string = format_string

    def render(self, context):
        try:
            actual_date = self.date_to_be_formatted.resolve(context)
            return actual_date.strftime(self.format_string)
        except template.VariableDoesNotExist:
            return ''
```
文档中说的很详细，我这里就简单的总结一下。parser这里没有用到就先不说，只要是token，token其实就是`{%...%}`中的所有元素，通过`split_contents`函数进行分割之后（按照空格进行分割），成为一个个的Node，当然，引号括起来的算一个Node，之后就是对这些Node进行处理并返回需要的数据了。做一些try...catch也是很有必要的，这样会显得我们的程序更加鲁棒一些。

render为最后执行的方法，return为最后实际返回的内容。所以我们的主要逻辑是可以写在render函数中的，整个构造还是相对容易理解的。

*这里我查阅了一些资料，可是对render方法中的context还是不太理解。*以我个人的理解，这里的context类似于render template中的Context，可以对其进行赋值，例如：`context['var1'] = 'aaa'`，这样我们就可以在template直接使用：`{{ var1 }}`。

我这里发现了一篇不错的博客，自制了一个可复用性强的tags，可以供大家学习，[地址][2]。

此外，文档中还介绍了custom tags的一些其他用法，例如：`Simple tags`，`Inclusion tags`等等，由于博客中暂时用不到，所以就先不介绍了。

--------------

在Hitcount中的应用
==========

注册方法：
```
def get_hit_count_javascript(parser, token):
    return GetHitCountJavascript.handle_token(parser, token)
    
register.tag('get_hit_count_javascript', get_hit_count_javascript)
```
主要逻辑放在了类中，如下：
```
class GetHitCountJavascript(template.Node):

    def handle_token(cls, parser, token):
        args = token.contents.split()
        
        if len(args) == 3 and args[1] == 'for':
            return cls(object_expr = parser.compile_filter(args[2]))

        else:
            raise TemplateSyntaxError, \
                    "'get_hit_count' requires " + \
                    "'for [object] in [timeframe] as [variable]' " + \
                    "(got %r)" % args

    handle_token = classmethod(handle_token)


    def __init__(self, object_expr):
        self.object_expr = object_expr


    def render(self, context):
        ctype, object_pk = get_target_ctype_pk(context, self.object_expr)
        
        obj, created = HitCount.objects.get_or_create(content_type=ctype, 
                        object_pk=object_pk)

        js =    "$.post( '" + reverse('hitcount_update_ajax') + "',"   + \
                "\n\t{ hitcount_pk : '" + str(obj.pk) + "' },\n"         + \
                "\tfunction(data, status) {\n"                         + \
                "console.log(data);" +\
                "\t\tif (data.status == 'error') {\n"                  + \
                "\t\t\t\n"                   + \
                "\t\t}\n\t},\n\t'json');"

        return js
```
使用方式在上一期的博客中已经提到过，如下所示：
```
{% get_hit_count_javascript for article %}
```

**Python also offers the @classmethod decorator, which generates methods on classes that take the class itself as the first argument. This might be useful in cases where you want to perform some introspection on the class object itself without instantiating it ------2014/10/04更新**

首先来看`handle_token`方法，我进行了资料的查阅，可还是一知半解。我觉得它应该是在`__init__`方法执行之前的一个过滤，通过自带的文档解析器`parser`解析出第三个参数后传给object_expr，cls为执行`handle_token`方法的Class类，进行实例化之后自动调用`__init__`方法保存object_expr，最后调用处理逻辑的render()方法。

```
def get_target_ctype_pk(context, object_expr):
    # I don't really understand how this is working, but I took it from the
    # comment app in django.contrib and the removed it from the Node.
    try:
        obj = object_expr.resolve(context)
    except template.VariableDoesNotExist:
        return None, None

    return ContentType.objects.get_for_model(obj), obj.pk
```
在执行render方法时，首先用上述方法获取到对象模型和对象的pk值。作者本人也对此方法不甚了解，不过可以肯定的是，其功能可以概括为通过之前解析得来的object_expr（对象描述）来反向获取到对象，再进一步获取到对象模型。

利用得到的模型创捷或者获取（get_or_create）实例，这里得到的实例就是用来记录每个文章点击量的HitCount对象。所以说之前解析器解析的也就是“文章”的object_expr（以我的博客为例，“文章”使用Article模型，则object_expr为article）。

最后返回一段js（这里需要jQuery的帮助），提交获取的信息，并交由view层处理，将HitCount自增一。这里作者使用了返回js，再二次提交的方式来进行HitCount的自增处理，个人感觉也可以直接在自定义的tags内部调用view层的方法进行处理。

-----------

总结
===

感觉Django自带的自定义标签方法还是很多变的，必须要自己亲身实践之后才能更加有体会。正如文中给出的博文链接所表现的，如果能够写出漂亮的自定义标签的话，不仅可以使代码变的更加优美，也会使自己的开发更加省力，这也是Django的一大特点之一，值得好好研究利用。






[1]: https://docs.djangoproject.com/en/1.7/howto/custom-template-tags/
[2]: http://www.b-list.org/weblog/2006/jun/07/django-tips-write-better-template-tags/