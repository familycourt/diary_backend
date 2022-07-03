import uuid
from rest_framework.serializers import Serializer, ModelSerializer
from .models import Diary


class DiaryWriteSerializer(Serializer):

    def create(self, validated_data):
        diary = Diary.objects.create(
            admin=self.context['request'].user,
            code=str(uuid.uuid4())
        )
        diary.users.add(self.context['request'].user)
        return diary


class DiarySerializer(ModelSerializer):

    class Meta:
        model = Diary
        fields = '__all__'
