# movies_django_rest_api
imdb like rest api using django rest api


#### Serialization

complex data type (movie object) --> convert to python native type (dictionary) --> Render to Json

#### De-Serialization

Render Json --> convert to python native type (dictionary) --> convert to complex data type

#### Architecture --> ask below questions before starting on building an API

1. Type of Serializers?
    * Serializer
    * ModelSerialzer
2. Type of Views?
    * Class Based Views  (APIview class)
        * APIview : Generic Views, Mixins, Concrete View Class, ViewSets & Routers
    * Function Based Views (@api_view())
3. Working with API? how to access etc?
    * DRF Browsable API
    * Postman
    * HTTPie
