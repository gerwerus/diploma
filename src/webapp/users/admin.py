from django.contrib import admin
from .models import Person, Account, InvestTest


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "middle_name", "birth_date")
    search_fields = ("first_name", "last_name", "middle_name")
    list_filter = ("birth_date",)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("person", "balance", "update_date")
    list_filter = ("update_date",)
    search_fields = ("person__first_name", "person__last_name")
    list_editable = ("balance",)


@admin.register(InvestTest)
class InvestTestAdmin(admin.ModelAdmin):
    list_display = ("name", "technical_name", "person")
    search_fields = ("name", "technical_name")
    list_filter = ("person",)
