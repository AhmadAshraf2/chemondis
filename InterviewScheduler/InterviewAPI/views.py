import json
from datetime import timedelta
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView
from . import models, serializers


class ViewAllSlots(ListAPIView):
    """
    Entertains GET request and returns single Interview object
    """
    queryset = models.Slot.objects.all()
    serializer_class = serializers.ViewSlotSerializer


class CreateSlot(CreateAPIView):
    """
    Entertains POST request and creates Interview object
    """
    serializer_class = serializers.CreateSlotSerializer


class InterviewSlots(GenericAPIView):

    serializer_class = serializers.InterviewSlotsSerializer

    def post(self, request, *args, **kwargs):
        """
          Api to send sms from oscar(logistics)
        """
        try:
            names = request.data['names']
            user_slots = {}

            for name in names:
                user_slots[name] = [s for s in models.Slot.objects.all().filter(user__username=name)]

            user_slots = clean_user_slots(user_slots)
            available_slots = suggested_slots(user_slots)

            return Response(json.dumps(available_slots), status=status.HTTP_200_OK)

        except Exception as e:
            pass


def clean_user_slots(slots):
    cleaned_user_slots = []

    for name, user_slots in slots.items():
        all_user_slots = []
        for slot in user_slots:
            all_user_slots += divide_slots(slot)

        cleaned_user_slots += [all_user_slots]

    return cleaned_user_slots


def divide_slots(slot):
    slots = []
    start = slot.start_date
    while start < slot.end_date:
        end = start + timedelta(minutes=60)
        slots += [start.strftime("%Y-%m-%d %H:%M:%S") + '---' + end.strftime("%Y-%m-%d %H:%M:%S")]
        start = end

    return slots


def suggested_slots(slots):
    available_slots = set.intersection(*map(set, slots))
    slots = []

    for slot in available_slots:
        start = slot.split('---')[0]
        end = slot.split('---')[1]
        slots.append({
            "start_date": start,
            "end_date": end,
        })

    return slots
