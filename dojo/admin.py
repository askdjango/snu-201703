from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'content_size', 'tags', 'lnglat']
    # list_display_links = ['title']
    list_editable = ['title']
    search_fields = ['title']
    list_filter = ['created_at', 'status']
    actions = ['make_published']

    def make_published(self, request, queryset):
        total = queryset.update(status='p')
        self.message_user(request, '{}건을 발행했습니다.'.format(total))
    make_published.short_description = '선택된 항목을 발행하기'

    def content_size(self, post):
        html = '<span style="color: blue;">{}</span>글자'.format(len(post.content))
        return mark_safe(html)
    content_size.short_description = '글자수'
    # content_size.allow_tags = True  # deprecated

admin.site.register(Post, PostAdmin)

