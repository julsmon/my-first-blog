from rest_framework import serializers
from .models import Step, Cycle, Program, MotorSetting, GeneralSetting

class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = '__all__'
