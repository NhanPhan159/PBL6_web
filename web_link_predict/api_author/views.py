from argparse import Action
from unicodedata import name
from rest_framework import viewsets
from api_author.models import Author, Publication
from api_author.serializers import AuthorSerializer, PublicationSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class Authorviewset(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=True,methods=['get'],url_path="get-publications")
    def getPublications(self,request,pk):
        querryset = Publication.objects.filter(id_author=pk)
        serializer = PublicationSerializer(querryset,many=True)
        if serializer:
            return Response(serializer.data)
        else: return Response("Nothing to show",status=201)
    
    @action(detail=True,methods=['post'],url_path="post-publications")
    def postPublication(self,request):
        serializer = PublicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    @action(detail=False,methods=['get'],url_path='get-suggest')
    def getSuggest(self,request):
        params = request.query_params
        data = {
            'author' : "Duc",
            'address' : 'DaNang'
        }
        querryset = Author.objects.filter(name=params['name']).values()
        print(list(querryset))
        return Response(data)