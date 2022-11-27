from datetime import datetime
import requests

from config import Config
from .. import db, scheduler
from ..models.weather import NwsObservation


base_url = "https://api.weather.gov/"


@scheduler.task("cron", id="nws_obs", minute=40, misfire_grace_time=900)
def get_observations():
    """Get latest weather observation data from an NWS station."""

    # Request data from NWS REST API
    headers = {"User-Agent": Config.DEFAULT_HTTP_USER_AGENT}
    resp = requests.get(
        f"{base_url}/stations/{Config.NWS_DEFAULT_STATION}/observations/latest",
        headers=headers,
    )
    props = resp.json()["properties"]

    # Insert data into local database
    obs = NwsObservation(
        timestamp=datetime.strptime(props["timestamp"], "%Y-%m-%dT%H:%M:%S%z"),
        station=props["station"][-4:],
        textDescription=props["textDescription"],
        temperature=props["temperature"]["value"],
        windSpeed=props["windSpeed"]["value"],
        barometricPressure=props["barometricPressure"]["value"],
        visibility=props["visibility"]["value"],
        precipitationLastHour=props["precipitationLastHour"]["value"],
        relativeHumidity=props["relativeHumidity"]["value"],
        windChill=props["windChill"]["value"],
        heatIndex=props["heatIndex"]["value"],
        cloudLayers=props["cloudLayers"][0]["amount"],
    )

    db.session.add(obs)
    db.session.commit()
