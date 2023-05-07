# Django Gateway Application

This is a Django application that acts as a gateway between two endpoint APIs. It takes input bank name and other required attributes as input from an API and transforms the request to the format of the endpoint. The mappings are stored in a database.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Django 3.2 or higher
- Django REST framework 3.12 or higher

### Installing

1. Clone the repository to your local machine
2. Install the required dependencies using `pip install -r requirements.txt`
3. Set up the database by running `python manage.py migrate`
4. Start the Django development server by running `python manage.py runserver`

### Usage

To use the Django Gateway application, send a POST request to the `/gateway/` endpoint with the following parameters in the request body:

- `bank_name`: the name of the bank
- `action`: the action on the bank
-  `other attributes`: the other applicable attributes for the action on the bank api

The Django application will transform the request to the format of the endpoint and forward it to the appropriate API.

### Configuration

The mappings between the input parameters and the endpoint parameters are stored in a database. You can modify the mappings by updating the database entries. If you want to register a new bank to the endpoint use the `addBank` API by providing it all the schemas and actions as given below.

```
{
   "create":{
      "username":"TEST",
      "password":"TEST",
      "full_name":"TEST",
      "email":"TEST"
   },
   "deposit":{
      "acc_no":"TEST",
      "password":"TEST",
      "amount":"TEST"
   },
   "all":{
      "username":"TEST",
      "full_name":"TEST"
   },
   "withdraw":{
      "acc_no":"TEST",
      "password":"TEST",
      "amount":"TEST"
   }
}
```


