## Django REST API Setup

This repository contains a Django project with a RESTful API using Django REST Framework.

## Prerequisites

Python (version 3.x recommended)

Django

Django REST Framework

## Setup Instructions

 Create a Virtual Environment:

 pip install virtualenvwrapper-win

 mkvirualenv environmentname

## Install Dependencies:

pip install django

pip install djangorestframework

Set up a new project with a single application

django-admin startproject Vendor

cd Vendor

django-admin startapp Vendor_App

Database migration

python manage.py makemigrations

python manage.py migrate

Superuser creation and Token generation

python manage.py createsuperuser

curl -X POST -d "username=your_superuser_username&password=your_superuser_password" http://localhost:8000/api-token-auth/

## Running the server

python manage.py runserver

Access Django Admin:

Open the Django admin at http://127.0.0.1:8000/admin/ and log in using the superuser credentials. this is to access the database as a admin user.

## How to run an API endpoint:

first we need to make sure that we migrated the models to database

then we need to start the server using "python manage.py runserver" command.

then we need to open another cmd prompt and open virtual environment and open the project folder and  httpie commands.


## Testing the API endpoints.

Stop the server running in cmd (press ctrl+c)

run the command:

python manage.py test

Using the API endpoints.

we can test API endpoints using curl or httpie commands.

Create a vendor:

http POST http://127.0.0.1:8000/api/vendors/ vendor_code=01 name="Vendor 1" contact_details="Contact 1" address="Address 1" "Authorization: Token your_obtained_token"

About this API endpoint:

here this endpoint is used to create a vendor by providing the vendor details.

List all Vendors details:

http http://127.0.0.1:8000/api/vendors/ "Authorization: Token your_obtained_token"

About this API endpoint:

here this endpoint is used to get the details of all vendors.

Retrieve a specific vendor's details:

http http://127.0.0.1:8000/api/vendors/{vendor_id}/ "Authorization: Token your_obtained_token"

About this API endpoint:

here this endpoint is used to get the details of vendor with vendor_id which was mentioned in the command.

Update a vendor's details:

using httpie:

PUT method:

http PUT http://127.0.0.1:8000/api/vendors/{vendor_id}/ vendor_code="updated vendor code" name="Updated Vendor Name" contact_details="Updated Contact Details" address="Updated Address" "Authorization: Token your_obtained_token"

PATCH method:

http PATCH http://127.0.0.1:8000/api/vendors/{vendor_id}/ name="Updated Vendor Name" contact_details="Updated Contact Details" address="Updated Address" "Authorization: Token your_obtained_token"

About this API endpoint:

here this endpoint we have two commands with different http methods (PUT,PATCH).As we have a primary key in the model the PUT method works as POST method (which means it creates a new vendor with given details). The PATCH method is 
used to update the vendor's details except vendor's id. here PUT handles updates by replacing the entire entity, so it creates a new entity. but where the PATCH handles by only updating the given fields.

Delete a vendor:

http DELETE http://127.0.0.1:8000/api/vendors/{vendor_id}/ "Authorization: Token your_obtained_token"

About this API endpoint:

here this endpoint is used to delete the vendor with given vendor_id.

Create a purchase_order:

http POST http://127.0.0.1:8000/api/purchase_orders/ po_number="01" vendor=01 order_date="2023-01-01" delivery_date="2023-01-10" items='[{"item_name": 20 }]' quality_rating=4.5 issue_date="2023-01-01" status="Pending" acknowledgment_date="2023-01-02" "Authorization: Token your_obtained_token"

About this API endpoint:

here this endpoint is used to create a purchase_order with given details.

List all purchase_orders details:

http http://127.0.0.1:8000/api/purchase_orders/ "Authorization: Token your_obtained_token"

About this API endpoint:

here this endpoint is used to get the details of all purchase_orders.

Retrieve a specific purchase_order's details:

http http://127.0.0.1:8000/api/purchase_orders/{po_id}/ "Authorization: Token your_obtained_token"

About this API endpoint:

here this endpoint is used to get the details of purchase_order with given po_id.

Update a purchase_order's details:

http PUT http://127.0.0.1:8000/api/purchase_orders/{po_id}/ po_number="UpdatedPO001" vendor="updatedid" order_date="2023-01-02T12:00:00" delivery_date="2023-01-15T12:00:00" items:='[{"item_name": 20 }]' quality_rating:=4.8 issue_date="2023-01-01" status="updated" acknowledgment_date="2023-01-02" "Authorization: Token your_obtained_token"

PATCH method:

http PATCH http://127.0.0.1:8000/api/purchase_orders/{po_id}/ order_date="2023-01-02T12:00:00" delivery_date="2023-01-15T12:00:00" items:='[{"item_name": "Updated Item", "quantity": 20 }]' quality_rating:=4.8 status="updated" "Authorization: Token your_obtained_token"

About this API endpoint:

here this endpoint we have two commands with different http methods (PUT,PATCH).As we have a primary key in the model the PUT method works as POST method (which means it creates a new purchase_order with given details). The PATCH method is used to update the purchase_order's details except purchase_order's number. here PUT handles updates by replacing the entire entity, so it creates a new entity. but where the PATCH handles by only updating the given fields.(we can provide any no of fields in PATCH method.)

Delete a purchase_order:

http DELETE http://127.0.0.1:8000/api/purchase_orders/{po_id}/ "Authorization: Token your_obtained_token"

About this API endpoint:

here this endpoint is used to delete a purchase_order with given po_id.
Retrieve a vendor's performance metrics:

http http://127.0.0.1:8000/api/vendors/1/performance/ "Authorization: Token your_obtained_token"

About this API endpoint:

here this endpoint is used to retrieve the performance metrics of a vendor with given vendor_id. this performance metrics contains on_time Delivery rate, quality rating average, average response time, fulfilment rate
On time delivery rate is calculated each time a PO status changes to "completed". this is the average of no of po delivered before the delivery_date and no of total po's delivered.
quality rating average is calculated after every po completion and it is the average of all ratings given to that specific vendor.
average response time is calculated each time a po is acknowledged by the vendor. it is the time difference between issue_date and acknowledgment_date for each po, and then the average of these times for all po's of the vendor.
fulfillment rate is calculated when po status is set to "completed". this is the average of no of successfully fulfilled pos (status = "completed" without issues) by the total no of pos issued to the vendor.

Update acknowledgment_data and trigger the recalculation of average_response_time:

http PATCH http://127.0.0.1:8000/api/purchase_orders/{po_id}/acknowledge/ "Authorization: Token your_obtained_token" acknowledgment_date="2023-12-20T12:00:00Z"

About this API endpoint:

here this endpoint is used to acknowledge the purchase_order with given po_id and trigger the recalculation of average_reponse_time.
