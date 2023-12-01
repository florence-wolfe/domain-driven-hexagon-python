from pymongo import MongoClient
from django.apps import AppConfig


class Main(AppConfig):
    name = "main"
    verbose_name = "Main"

    def ready(self):
        # Connect to MongoDB - Replace with your connection string
        client = MongoClient("mongodb://localhost:28017/")

        # Create or access a database
        db = client["ddd_db"]
        # Create or access a collection
        db["connected_report"]
