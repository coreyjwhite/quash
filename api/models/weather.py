"""Weather database table mapper classes."""

from .base import BaseModel
from sqlalchemy import Column, DateTime, Float, Integer, String


class NwsObservation(BaseModel):
    """NWS weather station observation data."""

    __tablename__ = "nws_observation"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    station = Column(String(4))
    textDescription = Column(String(99))
    temperature = Column(Float)
    windSpeed = Column(Float)
    barometricPressure = Column(Integer)
    visibility = Column(Integer)
    precipitationLastHour = Column(Integer)
    relativeHumidity = Column(Float)
    windChill = Column(Float)
    heatIndex = Column(Float)
    cloudLayers = Column(String(3))
