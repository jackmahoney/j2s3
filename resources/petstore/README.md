# swagger-java-client

## Requirements

Building the API client library requires [Maven](https://maven.apache.org/) to be installed.

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn deploy
```

Refer to the [official documentation](https://maven.apache.org/plugins/maven-deploy-plugin/usage.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
    <groupId>io.swagger</groupId>
    <artifactId>swagger-java-client</artifactId>
    <version>1.0.0</version>
    <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
compile "io.swagger:swagger-java-client:1.0.0"
```

### Others

At first generate the JAR by executing:

    mvn package

Then manually install the following JARs:

* target/swagger-java-client-1.0.0.jar
* target/lib/*.jar

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.PetsApi;

import java.io.File;
import java.util.*;

public class PetsApiExample {

    public static void main(String[] args) {
        
        PetsApi apiInstance = new PetsApi();
        try {
            apiInstance.createPets();
        } catch (ApiException e) {
            System.err.println("Exception when calling PetsApi#createPets");
            e.printStackTrace();
        }
    }
}

```

## Documentation for API Endpoints

All URIs are relative to *http://petstore.swagger.io/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PetsApi* | [**createPets**](docs/PetsApi.md#createPets) | **POST** /pets | Create a pet
*PetsApi* | [**listPets**](docs/PetsApi.md#listPets) | **GET** /pets | List all pets
*PetsApi* | [**showPetById**](docs/PetsApi.md#showPetById) | **GET** /pets/{petId} | Info for a specific pet


## Documentation for Models

 - [Error](docs/Error.md)
 - [Pet](docs/Pet.md)
 - [Pets](docs/Pets.md)


## Documentation for Authorization

All endpoints do not require authorization.
Authentication schemes defined for the API:

## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issue.

## Author



