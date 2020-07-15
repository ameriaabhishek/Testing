*** Settings ***
Library           Sample.py

*** Variables ***

*** Test Cases ***
Sample_Test_Case
    ${response}=    sample_func
    log to console    ${response}
    Should Be Equal    ${response}    PASSED
