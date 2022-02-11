
# QR Code Application

This is a basic QR Code application.
Using this application you can generate QR code for you text/links.
Using this application you can read (decode) QR codes.

## Author - Atharva Parkhe

- Github - [atharvparkhe](https://www.github.com/atharvparkhe/)
- LinkedIn - [Atharva Parkhe](https://www.linkedin.com/in/atharva-parkhe-3283b2202/)
- Instagram - [atharvparkhe](https://www.instagram.com/atharvparkhe/)
- Twitter - [atharvparkhe](https://www.twitter.com/atharvparkhe/)

## Features

- Generate QR codes for text and links.
- QR codes generated are universally accepted.
- Read/Decode QR codes.
## Tech Stack

**Backebd:** Django *(Python)*

**Frontend:** ReactJS *(Java-Script)*

## API Reference

#### Get all items

```http
  POST /api/read/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `file` | `image (file)` | **Required**. Upload Image file (form-data) |

**RESPONSE** - Decoded text from the QR code Image.

#### Get item

```http
  GET /api/generate/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `text`      | `string` | **Required**. Text to be converted into QR code |

**RESPONSE** - QR code.

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
  git clone https://github.com/atharvparkhe/QRcode.git
```

***Step#4 :*** Go to the project directory

```bash
  cd QRcode
```

***Step#5 :*** Install dependencies

```bash
  pip install -r requirements.txt
```

***Step#6 :*** Make Migrations

```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
```

***Step#7 :*** Run Server

```bash
  python3 manage.py runserver
```

Check the terminal if any error.

## Documentation

The docs folder contain all the project documentations and screenshots related the project.

Postman Endpoints - https://www.getpostman.com/collections/cd81994f26e4f66094be

## Demo

Youtube Tutorial - I will upload tutorial video soon. Stay Tuned.
