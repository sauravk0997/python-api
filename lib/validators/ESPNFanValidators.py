from itertools import count
import logging
from lib.schemas import *
from marshmallow import ValidationError
from robot.api.deco import keyword, library
from robot.api.exceptions import Failure
import requests



@library(scope='GLOBAL', version='5.0.2')
class ESPNFanValidators(object):
    """JSON validation for ESPN Sports Core API"""

    def __init__(self, *p, **k):
        pass
    
    @keyword('Fan Schema from ${response} should be valid', tags=['schema checks', 'functional', 'CoreV3'], types={'response': requests.Response})
    def sports_resp_is_valid_for_badminton(self, response) -> bool:
        try:
            schema = ESPNFanSchema().load(response.json())     
        except ValidationError as ve:
            raise Failure(f'Schema Data failed validation: {ve.messages}')
        return True



    @keyword('Validate the correct name of key')
    def validate_the_name_of_key(self, response, key) -> bool :
        try:
            if key in response:
                if response[key] == "":
                    
                    logging.error(f"Expected the key {key} is not null, actually found {response[key]}")
                    
                
            else:
                logging.error(f"Key {key} is not available in response ")

        except ValidationError as ve:
            raise Failure(f'Data failed validation: {ve.messages}')
        
        return True

    @keyword('Get the count of the key')
    def get_the_count_of_key(self, response, key) -> bool :
        try:

            # count = 0
            # for i in response[key]:
            #     if i != "":
            #         count += 1
            length = len(response[key])
  
            logging.info(f"The total value of {key} in response is {length}")
               
        except ValidationError as ve:
            raise Failure(f'Data failed validation: {ve.messages}')
        
        return True


    @keyword('Get the value of the key')
    def get_the_value_of_key(self, response, key1, key) -> bool :
        try:
            
            for i in response[key1]:
                if i == key:
                    x = response[key1][key]

                    logging.info(f"The value of response is {x}")
               
        except ValidationError as ve:
            raise Failure(f'Data failed validation: {ve.messages}')
        
        return True



    @keyword('Get the value of the base key')
    def get_the_value_of_base_key(self, response, key) -> bool :
        try:
            
            for i in response:
                if i == key:
                    x = response[key]

                    logging.info(f"The value of response of base schena is {x}")
               
        except ValidationError as ve:
            raise Failure(f'Data failed validation: {ve.messages}')
        
        return True

    


    @keyword('Get the value of the preferences key')
    def get_the_value_of_preferences_key(self, response,  key) -> bool :
        try:
            URL = []
            length = len(response['preferences'])
            for j in range(length):
                for k in response["preferences"][j]["metaData"]["entry"]:
                    if k == key:
                        x = response["preferences"][j]["metaData"]["entry"][key]
                        URL.append(x)
            UniqueURL= set(URL)
            count = len(UniqueURL)
                        
            logging.info(f"The value of response of preference unique URL is {UniqueURL} and its count is {count} ")
                       
        except ValidationError as ve:
            raise Failure(f'Data failed validation: {ve.messages}')
        
        return True
    @staticmethod
    def Groups_Response_URL(response, key):
        try:
            URL = []
            length = len(response['preferences'])
            
            for j in range(length):
                for k in response["preferences"][j]["metaData"]["entry"]:
                    if 'groups' in k:
                        length1 = len(response["preferences"][j]["metaData"]["entry"]['groups'])
                        for l in response["preferences"][j]["metaData"]["entry"]['groups'][length1-1]:
                            if l == key:
                                x = response["preferences"][j]["metaData"]["entry"]['groups'][length1-1][key]
                                URL.append(x)
                    
            UniqueURL= set(URL)
            return UniqueURL
        except ValidationError as ve:
            raise Failure(f'Data failed validation: {ve.messages}')
        
        

    

    @keyword('Get the value of the groups key')
    def get_the_value_of_groups_key(self, response,  key) -> bool :
        try:
            # URL = []
            # length = len(response['preferences'])
            
            # for j in range(length):
            #     for k in response["preferences"][j]["metaData"]["entry"]:
            #         if 'groups' in k:
            #             length1 = len(response["preferences"][j]["metaData"]["entry"]['groups'])
            #             for l in response["preferences"][j]["metaData"]["entry"]['groups'][length1-1]:
            #                 if l == key:
            #                     x = response["preferences"][j]["metaData"]["entry"]['groups'][length1-1][key]
            #                     URL.append(x)
                    
            # UniqueURL= set(URL)
            Unique_URL= 
        
            count = len(Unique_URL)
            
            
            logging.info(f"The value of response of groups unique URL is {Unique_URL} and its count is {count} ")
                       
        except ValidationError as ve:
            raise Failure(f'Data failed validation: {ve.messages}')
        
        return True


    @keyword('Get the status code 200 of all links')
    def get_the_status_code_of_all_links(self, response,  key) -> bool :
        try:
            URL = []
            length = len(response['preferences'])
            for j in range(length):
                for k in response["preferences"][j]["metaData"]["entry"]:
                    if k == key:
                        x = response["preferences"][j]["metaData"]["entry"][key]
                        URL.append(x)
            UniqueURL= set(URL)
                   
            for i in UniqueURL:
                r = requests.get(i)
                StatusCode= r.status_code
                assert StatusCode == 200
                logging.info(f"The status code of URL  {i}  is {StatusCode} ")
                        
        except ValidationError as ve:
            raise Failure(f'Data failed validation: {ve.messages}')
        
        return True


    @keyword('Get the status code 200 of all groups links')
    def get_the_status_code_200_of_all_links(self, response,  key) -> bool :
        try:
            URL = []
            length = len(response['preferences'])
            
            for j in range(length):
                for k in response["preferences"][j]["metaData"]["entry"]:
                    if 'groups' in k:
                        length1 = len(response["preferences"][j]["metaData"]["entry"]['groups'])
                        for l in response["preferences"][j]["metaData"]["entry"]['groups'][length1-1]:
                            if l == key:
                                x = response["preferences"][j]["metaData"]["entry"]['groups'][length1-1][key]
                                URL.append(x)
                    
            UniqueURL= set(URL)
            for i in UniqueURL:
                r = requests.get(i)
                StatusCode= r.status_code
                assert StatusCode == 200
                logging.info(f"The status code of URL  {i}  is {StatusCode} ")
                       
        except ValidationError as ve:
            raise Failure(f'Data failed validation: {ve.messages}')
        
        return True
           













    

