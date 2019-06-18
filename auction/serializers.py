from django.contrib.auth.models import User
from rest_framework import serializers

from auction.models import Item, Photo


# class PhotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Photo
#         fields = ('photo')


class ItemSerializer(serializers.ModelSerializer):
    #photo = PhotoSerializer()
    class Meta:
        model = Item
        fields = ('name', 'date_added', 'date_stop', 'description', 'price')
