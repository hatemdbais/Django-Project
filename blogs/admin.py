from django.contrib import admin
from .models import SignUp
from .form import SignUpForm
from django.contrib.sites.models import Site
# Register your models here.


class SignUpAdmin(admin.ModelAdmin):

    list_display = ["id", "__str__", "timestamp", "updated"]

    form = SignUpForm

    class Meta:
        model = SignUp


admin.site.register(SignUp, SignUpAdmin)


admin.site.unregister(Site)


class SiteAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'domain')
    readonly_fields = ('id',)
    list_display = ('id', 'name', 'domain')
    list_display_links = ('name',)
    search_fields = ('name', 'domain')


admin.site.register(Site, SiteAdmin)
