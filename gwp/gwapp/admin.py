# from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
# from leaflet.admin import LeafletGeoAdmin
from .models import *
# Register your models here.


class UserBasicAdmin(admin.ModelAdmin):
    list_display = ('userID', 'userFirstName', 'userTaluka',)


admin.site.register(UserBasic, UserBasicAdmin)


class UserOtherInfoAdmin(admin.ModelAdmin):
    list_display = ('userID', 'userAreaOfLandOwned',)


admin.site.register(UserOtherInfo, UserOtherInfoAdmin)


class BorewellsYedshiAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'useTime',)


admin.site.register(BorewellsYedshi, BorewellsYedshiAdmin)


# class UserWellRegistrationAdmin(admin.ModelAdmin):
#     list_display = ('userID', 'userWellID','userWellActiveOrInact',)
#
#
# admin.site.register(UserWellRegistration, UserWellRegistrationAdmin)