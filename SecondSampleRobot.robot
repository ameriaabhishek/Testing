*** Settings ***
Library           Sample.py

*** Variables ***

*** Test Cases ***
Sample_Test_Case
    ${response}=    sample_func
    Should Be Equal    ${response}    PASSED