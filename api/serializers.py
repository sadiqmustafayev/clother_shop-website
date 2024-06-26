from core.models import Blog
from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Blog
    fields = '__all__'


  def to_representation(self, instance):
    data = super().to_representation(instance)
    data['image'] = instance.image.url
    data['created_at'] = instance.created_at.strftime('%d-%m-%Y')
    return data
  
