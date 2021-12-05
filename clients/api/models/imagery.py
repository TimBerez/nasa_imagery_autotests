"""Model for imagery request response."""

from pydantic import BaseModel

from core.core import AppConfig


class ImageryRequest(BaseModel):
    lat: float
    lon: float
    dim: float
    date: str
    cloud_score: bool
    api_key: str

    def __init__(self, **params):
        data = {
            'lat': params['lat'],
            'lon': params['lon'],
            'dim': params['dim'],
            'date': params['date'],
            'cloud_score': params['cloud_score'],
            'api_key': AppConfig().api_key
        }
        if params['api_key']:
            data['api_key'] = params['api_key']
        super().__init__(**data)


# pydantic is not support base64 normaly
class ImageryResponse(BaseModel):
    text: bytes
