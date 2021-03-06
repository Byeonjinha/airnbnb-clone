from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition"""

    list_display = ("room",
                    "check_in",
                    "check_out",
                    "guest",
                    "in_progress",
                    "is_finished",
                    )

    list_filter = ("status",)

    search_fields = ("name",)
# Register your models here.
