from django.contrib import admin

from article.models import Article, Label, LabelsInArticle, Timeline, QuickNote

class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)

class LabelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Label, LabelAdmin)

class LabelsInArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(LabelsInArticle, LabelsInArticleAdmin)

class TimelineAdmin(admin.ModelAdmin):
    pass

admin.site.register(Timeline, TimelineAdmin)

class QuickNoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(QuickNote, QuickNoteAdmin)