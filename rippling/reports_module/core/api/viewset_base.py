from rest_framework import viewsets
from rest_framework.parsers import JSONParser


class BaseViewSet(viewsets.ViewSet):
    parser_classes = [JSONParser]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
