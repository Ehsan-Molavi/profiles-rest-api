from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profiles_api import serializers, models, permissions
from rest_framework.authentication import TokenAuthentication


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
        'some HTTP methods',
        'lool like a traditional Django View',
        'give you more controls',
        'is mapped manually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})


    def post(self, request):
        """Doc post: create hello with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hello {name}"
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk=None):
        """Handle updating object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """some Doc"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Doc Return hello"""
        a_viewset = [
        'uses actions like: list create retrieve update partial update delete',
        'atomaticly maps to urls using routers',
        'provides more funtionality with less code'
        ]

        return Response({'message':'hello', 'a_ViewSet':a_viewset})

    def create(self, request):
        """craete new hello"""
        serializer = self.serializer_class(data= request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, pk=None):
        """Doc Handle getting onj by id"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handle update an obj"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """D"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """D"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating a class"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (permissions.UpdateOwnProfile,)


    
