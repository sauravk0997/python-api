from marshmallow import  fields
from lib.schemas import *
from robot.api.deco import keyword, library
from lib.schemas.ESPNFanSchema import *



class CustomFields(fields.Field):
    def _deserialize(self, entry, attr, ctx, **k):
        pass

