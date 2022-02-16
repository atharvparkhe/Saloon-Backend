
# Saloon Management Application

The basic aim for implementing Saloon management system is to eliminate the waiting time for the customers at saloon for waiting for their turn for the service.
This system would allow customers to view different saloons listed on the application, and view their services offered; also reserve seats for a specific service at any date and time according to their convenience and also pay in advance for the service they which they opted for.
The shopkeepers also get an interface to update the seats reservations and their services, also auto-generate invoice for the customers.

## Author - Atharva Parkhe

- Github - [atharvparkhe](https://www.github.com/atharvparkhe/)
- LinkedIn - [Atharva Parkhe](https://www.linkedin.com/in/atharva-parkhe-3283b2202/)
- Instagram - [atharvparkhe](https://www.instagram.com/atharvparkhe/)
- Twitter - [atharvparkhe](https://www.twitter.com/atharvparkhe/)

## Features

- The customer can select the service and saloon of their choice and select a slot for the screening of the movie.
- The customer can also book multiple seat for different services (if available).
- The customer can pay online for the service they booked in advance.
- The customer can also apply coupon codes to get discount.
- The customer will receive the invoice in their mail box.
- The Admins receive the list of orders and reservations.
- The admins can keep track of their orders and reservations and analyse them ignorer to improve them for the future.
- This provides a user friendly interface for both admins as well as sellers.
- The automated system is faster and more convenient.
- The customers get what they want at their finger tips.
- This eliminates/reduces the barriers of time required for ticket booking.
- This improves the reliability and efficiency of the process.
- This helps keep track of orders and analyse the sales.
- Saves the organisation’s time, resources and manpower.
- This improves the over all efficiency hence improving profits.


## Tech Stack

**Backebd:** Django (Python)

**Frontend:** IOS App (Swift)

## Run Locally

***Step#1 :*** Create Virtual Environment

```bash
  virtualenv env
```

***Step#2 :*** Activate Virtual Environment

```bash
  source env/bin/activate
```

***Step#3 :*** Clone the project

```bash
  git clone https://github.com/atharvparkhe/saloon.git
```

***Step#4 :*** Go to the project directory

```bash
  cd saloon
```

***Step#5 :*** Install dependencies

```bash
  pip install -r requirements.txt
```

***Step#6 :*** Create a .env file

***Step#7 :*** Make Migrations

```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
```

***Step#8 :*** Run Server

```bash
  python3 manage.py runserver
```

Check the terminal if any error.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`  -  Django Secret Key

`EMAIL_ID`  -  Email ID (which would be used to send emails)

`EMAIL_PW`  -  Email Password

`PUBLIC_KEY`  -  Razorpay API Public Key

`PRIVATE_KEY`  -  Razorpay API Private Key

Screen Shot for reference

![ENV file](docs/ss1.png)

## Documentation

The docs folder contain all the project documentations and screenshots related the project.

Postman Endpoints - https://www.getpostman.com/collections/1b6a6d804416782baaf1

Date Time Format -  dd/mm/yyyy hh:mm:ss

## Demo

Youtube Tutorial - I will upload tutorial video soon. Stay Tuned.
