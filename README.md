# MyTaxi 
## Running the program
- Configure your MySQL database_name, username, and password inside settings.py
- Create and activate virtual environment
- Install packages ``pip install -r requirements.txt``
- Apply migrations and run the project
  - python manage.py makemigrations
  - python manage.py migrate
  - python manage.py runserver
## Endpoints
- ``http://127.0.0.1:8000/create/`` GET (to list all of the orders) and POST (to make an order and get back id of a created order)
- ``http://127.0.0.1:8000/update-status/order_id/`` PUT (modify order's status: cancelled, accepted, or finished)
- ``http://127.0.0.1:8000/orders/clients/client_id/`` GET (to list all of the orders made by a particular client)
- ``http://127.0.0.1:8000/orders/clients/client_id/?from=YY-MM-DD&toYY-MM-DD/`` GET (to list orders made by a particular client within a given period)
- ``http://127.0.0.1:8000/create-driver/`` GET (to list all of the drivers) and POST (to create a driver)
- ``http://127.0.0.1:8000/create-client/`` GET (to list all of the clients) and POST (to create a client)
