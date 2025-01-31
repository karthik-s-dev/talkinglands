
# Talking Lands Assessment

I used `Python's FastAPI` for developing the Backend server and Use `MongoDB` for spatial database to handle and store geospatial data.

## *Mongoengine Schemas*
#### **Point** collection
    1. name - String
    2. description - String
    3. location - Point(mongoengine's point field)

## *Pydantic Model(Request body)*
#### **Point** Model
    1. name - String
    2. description - String
    3. location - list(float) --> longitude first, latitude second

# APIs
#### **POST-Point**
- Pass the Point model as request body to the endpoint `/point`.
- This will create the new Point document.

#### **Get-Point**
- Request at endpoint `/point` with document id.
- This will return a Point.

#### **Put-Point**
- Pass the Point model as request body to the endpoint `/point` with document id.
- This will return updated Point document.

#### **GET-Points**
- Request at endpoint `/points` with range query parameters such as start and end .
- This will return list of Points.

#### **GET-Points(bounding box query)**
- Request at endpoint `/points/bounding_box` with coordinates for a bounding box such as north, south, east and west.
- This will return list of Points within the Bounding box.

#### **GET-Points(Radius query)**
- Request at endpoint `/points/radius` with latitude, longitude and Radius.
- This will return list of Points within radius.