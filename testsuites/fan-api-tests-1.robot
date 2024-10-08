*** Settings ***
Documentation       Fan API  tests are executing with positive, negative combinations along with schema validation
...                 to run: robot --pythonpath $PWD ./testsuite/-tests.robot

Metadata    Author      Saurav Kumar
Metadata    Date        12-10-2022

Library             RequestsLibrary
# Library             lib.schemas.ESPNFanSchema           
Library             OperatingSystem
Library             Collections
Resource            resource/ESPNFanAPIResource.robot
Library             lib.validators.ESPNFanValidators



*** Test Cases ***
Get ESPN Fan Response
    ${response}=        A GET request to ${Base_url} should respond with 200
    Fan Schema from ${response} should be valid
    Validate the correct name of key    ${response.json()}        profile
    Validate the correct name of key    ${response.json()}        preferences
    #Validate the correct name of key    ${response.json()}        xy
    Get the count of the key            ${response.json()}        profile
    Get the count of the key            ${response.json()}        preferences
    Get the value of the key            ${response.json()}        profile    id
    Get the value of the key            ${response.json()}        profile    createDate
    Get the value of the key            ${response.json()}        profile    isInsider
    Get the value of the base key       ${response.json()}        id
    Get the value of the preferences key    ${response.json()}       logoURL
    Get the value of the preferences key    ${response.json()}        href
    Get the value of the preferences key    ${response.json()}      signupURL
    Get the value of the preferences key    ${response.json()}       entryURL
    Get the value of the preferences key    ${response.json()}       scoreboardFeedURL
    Get the value of the preferences key    ${response.json()}       logoUrl
    Get the value of the groups key         ${response.json()}       fantasyCastHref
    Get the value of the groups key         ${response.json()}        href
    Get the status code 200 of all links    ${response.json()}       logoURL
    Get the status code 200 of all links    ${response.json()}        entryURL
    Get the status code 200 of all links    ${response.json()}        href
    Get the status code 200 of all groups links    ${response.json()}    fantasyCastHref
    Get the status code 200 of all groups links    ${response.json()}    href





