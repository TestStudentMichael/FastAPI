# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = NULL # object | 

try:
    # Del By Id
    api_response = api_instance.del_by_id_del_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->del_by_id_del_delete: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserClass() # UserClass | 

try:
    # Edit User
    api_response = api_instance.edit_user_edit_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->edit_user_edit_put: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Id List
    api_response = api_instance.id_list_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->id_list_list_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Init
    api_response = api_instance.init_init_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->init_init_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserClass() # UserClass | 

try:
    # New User
    api_response = api_instance.new_user_create_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->new_user_create_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**del_by_id_del_delete**](docs/DefaultApi.md#del_by_id_del_delete) | **DELETE** /del | Del By Id
*DefaultApi* | [**edit_user_edit_put**](docs/DefaultApi.md#edit_user_edit_put) | **PUT** /edit | Edit User
*DefaultApi* | [**id_list_list_get**](docs/DefaultApi.md#id_list_list_get) | **GET** /list | Id List
*DefaultApi* | [**init_init_get**](docs/DefaultApi.md#init_init_get) | **GET** /init | Init
*DefaultApi* | [**new_user_create_post**](docs/DefaultApi.md#new_user_create_post) | **POST** /create | New User

## Documentation For Models

 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [UserClass](docs/UserClass.md)
 - [ValidationError](docs/ValidationError.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

