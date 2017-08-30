from django.contrib import admin
from .models import Step, Cycle, Program, MotorSetting, GeneralSetting, CustomRelay, WaterInlet, Chemical, Output24

admin.site.register(Step)
admin.site.register(Cycle)
admin.site.register(Program)
admin.site.register(MotorSetting)
admin.site.register(GeneralSetting)
admin.site.register(CustomRelay)
admin.site.register(WaterInlet)
admin.site.register(Chemical)
admin.site.register(Output24)
