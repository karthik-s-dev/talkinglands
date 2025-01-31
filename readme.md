
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

