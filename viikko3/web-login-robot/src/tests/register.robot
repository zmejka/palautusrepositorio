*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  anna
    Set Password  anna1234
    Set Password Confirmation  anna1234
    Submit Registration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  an
    Set Password  anna1234
    Set Password Confirmation  anna1234
    Submit Registration
    Register Should Fail With Message  Not valid username

Register With Valid Username And Too Short Password
    Set Username  anna
    Set Password  anna1
    Set Password Confirmation  anna1 
    Submit Registration
    Register Should Fail With Message  Not valid password

Register With Nonmatching Password And Password Confirmation
    Set Username  anna
    Set Password  anna1234
    Set Password Confirmation  anna5678
    Submit Registration
    Register Should Fail With Message  Password confirmation does not match

Login Afret Successful Registeration
    Set Username  anna
    Set Password  anna1234
    Set Password Confirmation  anna1234
    Submit Registration
    Go To Login Page
    Set Username  anna
    Set Password  anna1234
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  bella
    Set Password  bella1234
    Set Password Confirmation  anna5678
    Submit Registration
    Go To Login Page
    Set Username  bella
    Set Password  bella1234
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

