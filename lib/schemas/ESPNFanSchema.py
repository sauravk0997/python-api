from importlib.metadata import metadata
from sre_constants import GROUPREF_EXISTS
from marshmallow import Schema, fields, RAISE, ValidationError
import requests
from pprint import pprint
from lib.schemas.common import CustomFields




class entryMetadataSchema(Schema):
    #class Meta:
        #unknown = RAISE

    teamAbbrev          = fields.String(required=True)
    leagueFormatTypeId  = fields.Integer(required=True)
    pointsDelta         = fields.Integer(required=True)
    leagueSubTypeId     = fields.Integer(required=True)
    streakLength        = fields.Integer(required=False)
    customizable        = fields.Boolean(required=True)
    active              = fields.Boolean(required=True)
    nextGen             = fields.Boolean(requred=True)
    draftComplete       = fields.Boolean(required=True)
    scoringTypeId       = fields.Integer(required=True)
    streakType          = fields.Integer(required=False)
    leagueTypeId        = fields.Integer(required=True)
    draftInProgress     = fields.Boolean(required=True)
    
    
class groupsSchema(Schema):
    #class Meta:
        #unknown = RAISE

    groupId             = fields.Integer(required=True)
    wins                = fields.Integer(required=False)
    losses              = fields.Integer(required=False)
    ties                = fields.Integer(required=False)
    groupSize           = fields.Integer(required=False)
    groupName           = fields.String(required=True)
    groupManager        = fields.Boolean(required=True)
    draftDate           = fields.Integer(requred=False, allow_none=True)
    draftType           = fields.Integer(required=False)
    draftStatus         = fields.Integer(required=False)
    leagueStatus        = fields.Integer(required=False)
    createDate          = fields.Integer(required=False)
    lastUpdate          = fields.Integer(required=False)    
    points              = fields.Float(required=False)
    rank                = fields.Integer(required=False)
    fantasyCastHref     = fields.String(required=False, allow_none=True)
    href                = fields.String(required=False, allow_none=True)


class recordSchema(Schema):


    losses              = fields.Integer(required=True)
    wins                = fields.Integer(required=True)


# class groupSettingsSchema(Schema):

#     name                = fields.String(required=False)


# class challengeGroupsSchema(Schema):


#     groupSettings       = fields.Nested(groupSettingsSchema, required=False)


#class scoreByGroupSchema(Schema):


    

class scoreSchema(Schema):
    #class Meta:
        #unknown = RAISE

    eliminated          = fields.Boolean(required=True)
    overallScore        = fields.Integer(required=True)
    percentile          = fields.Float(required=False)
    rank                = fields.Integer(required=False)
    record              = fields.Nested(recordSchema, required=True)



class logoURLsSchema(Schema):
    #class Meta:
        #unknown = RAISE

    logoSecondary       = fields.String(required=True)
    logoPrimary         = fields.String(required=True)
    darkLogoURL         = fields.String(required=True)
    lightLogoURL        = fields.String(required=True)
    


class EntrySchema(Schema):
    #class Meta:
        #unknown = RAISE

    createDate          = fields.Integer(required=False)
    entryId             = fields.Integer(required=False)
    entryLocation       = fields.String(required=False)
    entryMetadata       = fields.Nested(entryMetadataSchema, required=False)
    entryNickname       = fields.String(required=False)
    gameId              = fields.Integer(required=False)
    groups              = fields.List(fields.Nested(groupsSchema),required=False)
    lastUpdate          = fields.Integer(requred=True)
    percentile          = fields.Integer(required=False)
    logoType            = fields.String(required=False)
    logoUrl             = fields.String(required=False)
    losses              = fields.Integer(required=False)
    points              = fields.Integer(required=False)
    rank                = fields.Integer(required=False)
    restrictionType     = fields.Integer(required=False)
    seasonId            = fields.Integer(required=False)
    ties                = fields.Integer(required=False)
    wins                = fields.Integer(required=False)
    entryURL            = fields.String(required=False)
    abbrev              = fields.String(required=False)
    name                = fields.String(required=False)
    description         = fields.String(required=False)
    logoURL             = fields.String(required=False)
    signupURL           = fields.String(required=False, allow_none=True)
    href                = fields.String(required=False)
    entryUuid           = fields.String(required=False)
    lastAvailableDate   = fields.Integer(required=False)
    challengeId         = fields.String(required=False)
    logoURLs            = fields.Nested(logoURLsSchema, required=False)
    gameUrl             = fields.String(required=False)
    entryName           = fields.String(required=False)
    challengeGroups     = CustomFields(required=False)
    score               = fields.Nested(scoreSchema, required=False)
    scoreByGroup        = fields.String(required=False)
    scoreboardFeedURL   = fields.String(required=False, allow_none=True)
    scoreByGroup        = CustomFields(required=False)
    




class MetaDataSchema(Schema):
    class Meta:
        unknown = RAISE

    entry               = fields.Nested(EntrySchema, required=False)
    inSeason            = fields.Boolean(required=False)
    isLive              = fields.Boolean(required=False)


class TypeSchema(Schema):
    #class Meta:
        #unknown = RAISE

    id                  = fields.Integer(required=True)
    name                = fields.String(required=True)
    code                = fields.String(required=True)
    isDeletable         = fields.Boolean(required=True)
    isDelegated         = fields.Boolean(required=True)
    maxAllowed          = fields.Integer(required=True)

class PreferenceSchema(Schema):
    #class Meta:
        #unknown = RAISE

    id                  = fields.String(required=True)
    createDate          = fields.Integer(required=False)
    lastUpdateDate      = fields.Integer(required=False)
    createSource        = fields.String(required=False)
    lastUpdateSource    = fields.String(required=False)
    metaData            = fields.Nested(MetaDataSchema,required=False)
    sortGlobal          = fields.Integer(required=True)
    isHidden            = fields.Boolean(required=True)
    typeId              = fields.Integer(required=True)
    affinity            = fields.Integer(required=True)
    type                = fields.Nested(TypeSchema, required=False)
    isImplicit          = fields.Boolean(required=False)

class ProfileSchema(Schema):
    #class Meta:
        #unknown = RAISE

    id                  = fields.String(required=True)
    createDate          = fields.Integer(required=True)
    lastUpdateDate      = fields.Integer(required=False)
    lastUpdateSource    = fields.String(required=True)
    isInsider           = fields.Boolean(required=True)
    isPremium           = fields.Boolean(required=True)
    hasNotificationPreferences    = fields.Boolean(required=False)
    useSortGlobal       = fields.Boolean(required=False)


class ESPNFanSchema(Schema):
    class Meta:
        unknown = RAISE

    id                  = fields.String(required=True)
    anon                = fields.Boolean(required=True)
    lastAccessDate      = fields.String(required=True)
    createDate          = fields.String(required=True)
    createSource        = fields.String(required=True)
    lastUpdateSource    = fields.String(required=True)
    lastUpdateDate      = fields.String(required=True)
    lastAccessSource    = fields.String(required=False,allow_none=True)
    profile             = fields.Nested(ProfileSchema, required=False)
    preferences         = fields.List(fields.Nested(PreferenceSchema), required=False)



if __name__ == '__main__':

    target = 'https://fan.api.espn.com/apis/v2/fans/%7B6E458CFC-7B0E-4811-8B3D-504CF5F7D4C0%7D?displayHiddenPrefs=true&context=fantasy&useCookieAuth=true&source=fantasyapp-ios&featureFlags=challengeEntries'

    resp = requests.get(target)

    if resp.status_code == 200:
        try:
            page = ESPNFanSchema().load(resp.json())

        except ValidationError as ve:
            pprint(ve.messages)
        else:
            print(f'{target} received with status code {resp.status_code} has been Validated')
    else:
        print(f'Received unexpected status code {resp.status_code} from {target}')


