from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView,ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserProfile, Comment
from .serializers import UserProfileSerializer, CommentSerializer, CreateUserProfileSerializer
from rest_framework import status


# @api_view(['GET', 'POST'])
# def user_profile(request):
#     return Response({'data': 'bahman'})

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
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def update_delete_user_profile(request, pk):
    if request.method == 'GET':
        profile = UserProfile.objects.get(pk=pk)
        if profile is not None:
            serializer_data = UserProfileSerializer(profile)
            return Response(serializer_data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        user_profile_pk = UserProfile.objects.get(pk=pk)
        if user_profile_pk is not None:
            serializer = UserProfileSerializer(
                instance=user_profile_pk,
                data=request.data
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        user_profile_pk = UserProfile.objects.get(pk=pk)
        user_profile_pk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def comments(request):
    comments = Comment.objects.all()
    serializer_data = CommentSerializer(comments, many=True)
    return Response(serializer_data.data)


class UserProfileView(APIView):
    def get(self, request):
        profiles = UserProfile.objects.all()
        serializer_data = UserProfileSerializer(profiles, many=True)
        return Response(serializer_data.data)

    def post(self, request):
        serializer = CreateUserProfileSerializer(data=request.data)
        # we don't want to fill instance and return ir like get method,we want to fill data with this serializer
        serializer.is_valid(raise_exception=True)
        # raise_exception means that if errors exists return them!!
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        user_profile_pk = UserProfile.objects.get(pk=pk)
        if user_profile_pk is not None:
            serializer = UserProfileSerializer(
                instance=user_profile_pk,
                data=request.data
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        user_profile_pk = UserProfile.objects.get(pk=pk)
        user_profile_pk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListUserProfileView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    # permission_classes = ...
    # pagination_class = ...


class CreateUserProfileView(CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = CreateUserProfileSerializer
    # permission_classes = ...
    # pagination_class = ...


class ListCreateUserProfileView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = CreateUserProfileSerializer
    # permission_classes = ...
    # pagination_class = ...
