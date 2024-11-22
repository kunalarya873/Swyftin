Django Image Hash API
=====================

This project provides a REST API to calculate and store the MD5 and perceptual hash (pHash) of images from public URLs. It also supports CRUD operations for managing the stored image hashes.

Features
--------

*   **Calculate MD5 and pHash**: Accepts a public image URL, computes its MD5 and pHash, and saves the details in the database.
*   **CRUD Operations**: Supports List, Retrieve, Update, and Delete for stored image hashes.

API Endpoints
-------------

Method

Endpoint

Description

`POST`

`/api/calculate-hash/`

Accepts an image URL and calculates hashes.

`GET`

`/api/image-hashes/`

Retrieves all stored image hashes.

`GET`

`/api/image-hashes/<id>/`

Retrieves a specific image hash by ID.

`PUT`

`/api/image-hashes/<id>/`

Updates a specific image hash entry.

`DELETE`

`/api/image-hashes/<id>/`

Deletes a specific image hash entry.

Setup
-----

1.  **Clone the repository**:
    
    `git clone https://github.com/kunalarya873/Swyftin`
    
    `cd imageshashapi` 
    
3.  **Install dependencies**:
    
    `pip install -r requirements.txt` 
    
4.  **Apply migrations**:
    
    `python manage.py migrate` 
    
5.  **Run the server**:
    
    `python manage.py runserver` 
    
6.  **Test APIs**:
    
    *   Use the attached `postman.json` file to import all endpoints into Postman for testing.
