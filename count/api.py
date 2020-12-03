from .models import Apply
from rest_framework import serializers, viewsets

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Apply
        fields = '__all__'

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Apply.objects.all()
    serializer_class = MemberSerializer