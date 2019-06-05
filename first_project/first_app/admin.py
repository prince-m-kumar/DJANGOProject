from django.contrib import admin
from first_app.models import AccessRecord,Topic,webPage,User
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(webPage)
admin.site.register(User)
