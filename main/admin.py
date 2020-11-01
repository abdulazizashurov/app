from django.contrib import admin
from .models import *



class NewAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Yangilikning Sarlavhasi/Sana ", {'fields': ["name", "datetime"]}),
        ("Yangilik Haqida", {'fields': ["about"]}),
    ]

class SocialAdmin(admin.ModelAdmin):
        fieldsets = [
            ("Asosiy Sarlavha Rasmlari", {'fields': ["image1", "image2","image3"]}),
            ("Ichtimoiy Tarmoqlar", {'fields': ["facebook","instagram","telegram"]}),
        ]


class SubjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Fan Nomi va Fan Haqida Ma'lumot", {'fields': ["subject", "about"]}),
        ("Narxlar va Tartibi", {'fields': ["price", "num"]}),
    ]
class TeacherAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Ustoz/Rasmlari/Fanlari ", {'fields': ["name", "img",'subject']}),
        ("Ichtimoiy Tarmoqlari", {'fields': ["facebook", "instagram","telegram"]}),
    ]
class PupilsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Ismi/Familyasi", {'fields': ["first_name", "last_name"]}),
        ("Tanlangan Fan/ Telefon", {'fields': ["subject_name", "phone"]}),
    ]
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(New,NewAdmin)
admin.site.register(SocialNetwork,SocialAdmin)
admin.site.register(Pupils,PupilsAdmin)