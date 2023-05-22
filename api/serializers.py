from rest_framework import serializers
from guest_book_app.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="comment-detail")

    class Meta:
        model = Comment
        fields = [
            "url",
            "id",
            "name",
            "comment",
        ]

    def validate_name(self, data):
        queryset = Comment.objects.filter(name__iexact=data)
        if queryset.exists():
            raise serializers.ValidationError(
                f"{data} already exist. Enter a unique name."
            )
        return data
