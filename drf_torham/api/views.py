from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile, Comment
from .serializers import UserProfileSerializer, CommentSerializer


@api_view(['GET', 'POST'])
def user_profile(request):
    profiles = UserProfile.objects.all()
    serializer_data = UserProfileSerializer(profiles, many=True)
    return Response(serializer_data.data)


# @api_view(['GET', 'POST'])
# def user_profile(request):
#     return Response({'data': 'bahman'})

@api_view(['GET', 'POST'])
def comments(request):
    comments = Comment.objects.all()
    serializer_data = CommentSerializer(comments, many=True)
    return Response(serializer_data.data)
