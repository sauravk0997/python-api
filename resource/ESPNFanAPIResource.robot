*** Settings ***

Library     RequestsLibrary
Library     Collections
Library     OperatingSystem


*** Variables ***

${Base_url}=    https://fan.api.espn.com/apis/v2/fans/%7B6E458CFC-7B0E-4811-8B3D-504CF5F7D4C0%7D?displayHiddenPrefs=true&context=fantasy&useCookieAuth=true&source=fantasyapp-ios&featureFlags=challengeEntries

*** Keywords ***

A GET request to ${endpoint} should respond with ${status}
    ${api_response}=    GET  url=${endpoint}  expected_status=${status}
    [Return]    ${api_response}