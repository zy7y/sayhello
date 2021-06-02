from django.contrib import admin

# Register your models here.

from .models import Text

# admin.site.register(Text)


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    # 需要显示字段
    list_display = ('name', 'create_at')
    # 每页数量 默认100条
    list_per_page = 10
    # 搜索字段
    search_fields = ['name']
    # 筛选字段
    list_filter = ['create_at']