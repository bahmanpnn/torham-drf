from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile, Comment
from .serializers import UserProfileSerializer, CommentSerializer, CreateUserProfileSerializer


@api_view(['GET', 'POST'])
def user_profile(request):
    if request.method == 'GET':
        profiles = UserProfile.objects.all()
        serializer_data = UserProfileSerializer(profiles, many=True)
        return Response(serializer_data.data)
    if request.method == 'POST':
        req_data = request.data
        serializer = CreateUserProfileSerializer(data=req_data)
        # we don't want to fill instance and return ir like get method,we want to fill data with this serializer

        serializer.is_valid(raise_exception=True)  # raise_exception means that if errors exists return them!!
        serializer.save()
        return Response(serializer.data, status=201)


# @api_view(['GET', 'POST'])
# def user_profile(request):
#     return Response({'data': 'bahman'})

@api_view(['GET', 'POST'])
def comments(request):
    comments = Comment.objects.all()
    serializer_data = CommentSerializer(comments, many=True)
    return Response(serializer_data.data)
