
# *** Settings    ***





# *** Settings ***
# Documentation       Fan API  tests are executing with positive, negative combinations along with schema validation
# ...                 to run: robot --pythonpath $PWD ./testsuite/-tests.robot

# Metadata    Author      Saurav Kumar
# Metadata    Date        12-10-2022

# Library             RequestsLibrary
# Library             lib.schemas.ESPNFanSchema
# Library             lib.validators.ESPNFanAPIValidators
# Library             OperatingSystem
# Library             Collections
# Resource            resource/ESPNFanAPIResource.robot



# *** Test Cases ***
# Get ESPN Fan Response
#     ${response}=        A GET request to ${Base_url} should respond with 200
#     Fan Schema from ${response}   should be valid
