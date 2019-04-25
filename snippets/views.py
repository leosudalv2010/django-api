from rest_framework import renderers, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class SnippetViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a snippet instance.
    list:
        Return all snippets,ordered by most recent joined.
    create:
        Create a new snippet.
    delete:
        Remove an existing snippet.
    update:
        Update an existing snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request):
        """
        Show the highlighted snippet.
        """
        snippet = self.get_object()
        return Response(snippet.highlighted)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        Return an user instance.
    list:
        Return all users, ordered by most recent joined.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


