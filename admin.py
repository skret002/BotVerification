from django.contrib import admin
from .models import VerificationCode
# Register your models here.
class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in VerificationCode._meta.fields]
    
    class Meta:
        model = VerificationCode

admin.site.register(VerificationCode, VerificationCodeAdmin)