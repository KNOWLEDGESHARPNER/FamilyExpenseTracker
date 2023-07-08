from django.contrib import admin

import familymembers


# Register your models here.
@admin.register(familymembers)
class FamilyMemberAdmin(admin.ModelAdmin):
    search_fields = ['name']