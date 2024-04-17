from django.contrib import admin
from .models import TovarCreate, Image, Carousel


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class TovarAdmins(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('title', 'category', 'tags_list')

    def tags_list(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

    tags_list.short_description = 'Теги'


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(TovarCreate, TovarAdmins)
admin.site.register(Carousel, CarouselAdmin)
