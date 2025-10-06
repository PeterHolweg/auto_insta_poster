import requests
from .config import IG_USER_ID, IG_LONG_LIVED_TOKEN


GRAPH_BASE = "https://graph.facebook.com/v17.0"




def create_media_container(image_url: str, caption: str = None) -> str:
"""Return creation_id"""
url = f"{GRAPH_BASE}/{IG_USER_ID}/media"
da
