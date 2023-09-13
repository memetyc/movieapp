from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.





class MovieAdmin(admin.ModelAdmin):

    list_display = ('title','is_active',"is_home",'display_genres')
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('genres','language','is_active',"is_home")
    search_fields = ('title','description')
    list_editable =('is_active',"is_home")
    
    def display_genres(self, obj):
        html = '<ul>'
        for i in obj.genres.all():
            html += f'<li> {i} </li>'
        html += '</ul>'
        return mark_safe(html)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name','gender','duty_type')
    list_filter = ('gender','duty_type')
    search_fields = ('first_name','last_name')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('full_name','movie','ratting')
    list_filter = ('movie','full_name')
    search_fields = ('movie__title',)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title','is_active']
    list_editable = ['is_active']


admin.site.register(Movie,MovieAdmin)

admin.site.register(Person,PersonAdmin)
admin.site.register(Contact)
admin.site.register(Genre)
admin.site.register(Video)
admin.site.register(Comment,CommentAdmin)


admin.site.register(Slider,SliderAdmin)


