from django.contrib import admin

from .models.hospital import Doctor, Hospital, Specialty

# Register your models below


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "specialty",
        "days_available",
        "time_available",
        "hospital",
    )
    list_filter = (
        "name",
        "hospital",
        "specialty",
    )


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = (
        "name_of_specialty",
    )
    list_filter = (
        "name_of_specialty",
    )


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
    )
    list_filter = (
        "name",
        "address",
    )
