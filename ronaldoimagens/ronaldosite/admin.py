from django.contrib import admin
from django.contrib.auth.models import Group, User
from ronaldosite.models import Galeria, Imagem


class GalleryAdmin (admin.ModelAdmin):
    fields = ('nome',)
    list_display = ('nome',)

class ImagemAdmin (admin.ModelAdmin):
    fields = ('imagem', 'galeria',)
    list_display = ('galeria',)


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Galeria, GalleryAdmin)
admin.site.register(Imagem, ImagemAdmin)
