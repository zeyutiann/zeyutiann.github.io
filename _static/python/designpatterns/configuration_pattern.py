from __future__ import annotations
from typing import Dict

conf = {'MONGO_HOST':'localhost','MONGO_PORT':'1231'}


class Config:

    def __init__(self, conf:Dict):
        self._config = conf

    def get_property(self, property_name: str):
        return self._config.get(property_name,None)


class MongoConfig(Config):

    @property
    def host(self):
        return self.get_property('MONGO_HOST')

    @property
    def port(self):
        return self.get_property('MONGO_PORT')

