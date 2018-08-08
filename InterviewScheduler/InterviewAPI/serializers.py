from . import models
from rest_framework import serializers


class ViewSlotSerializer(serializers.ModelSerializer):
    """
    serializes fields in Interview object
    """
    class Meta:
        model = models.Slot
        fields = '__all__'


def slot_validator(slot):
    if slot.strftime('%M') != '00' or slot.strftime('%S') != '00':
        raise serializers.ValidationError("Time should be start of each hour")
    return slot


class CreateSlotSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(validators=[slot_validator])
    end_date = serializers.DateTimeField(validators=[slot_validator])

    class Meta:
        model = models.Slot
        fields = '__all__'


class InterviewSlotsSerializer(serializers.Serializer):
    names = serializers.ListField()
