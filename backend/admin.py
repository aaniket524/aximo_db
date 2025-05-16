from django.contrib import admin
from .models import WorkProcessModel
from .models import HomeTestimonialModel

from .models import TeamModel
from .models import *

# Register your models here.



admin.site.register(WorkProcessModel)
admin.site.register(HomeTestimonialModel)
admin.site.register(TeamModel)
admin.site.register(Services)
admin.site.register(SingleService)
admin.site.register(Tag)
admin.site.register(Category)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'views')
    search_fields = ('title',)
    list_filter = ('category', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)