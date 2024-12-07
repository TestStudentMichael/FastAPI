# swagger_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**del_by_id_del_delete**](DefaultApi.md#del_by_id_del_delete) | **DELETE** /del | Del By Id
[**edit_user_edit_put**](DefaultApi.md#edit_user_edit_put) | **PUT** /edit | Edit User
[**id_list_list_get**](DefaultApi.md#id_list_list_get) | **GET** /list | Id List
[**init_init_get**](DefaultApi.md#init_init_get) | **GET** /init | Init
[**new_user_create_post**](DefaultApi.md#new_user_create_post) | **POST** /create | New User

# **del_by_id_del_delete**
> object del_by_id_del_delete(id)

Del By Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = NULL # object | 

try:
    # Del By Id
    api_response = api_instance.del_by_id_del_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->del_by_id_del_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_user_edit_put**
> object edit_user_edit_put(body)

Edit User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.UserClass() # UserClass | 

try:
    # Edit User
    api_response = api_instance.edit_user_edit_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->edit_user_edit_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserClass**](UserClass.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_list_list_get**
> object id_list_list_get()

Id List

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Id List
    api_response = api_instance.id_list_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->id_list_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_init_get**
> object init_init_get()

Init

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Init
    api_response = api_instance.init_init_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->init_init_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_user_create_post**
> object new_user_create_post(body)

New User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.UserClass() # UserClass | 

try:
    # New User
    api_response = api_instance.new_user_create_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->new_user_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserClass**](UserClass.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

