# Talking Lands API Documentation

This document provides a comprehensive guide on how to interact with the Talking Lands backend server, which is developed using Python's FastAPI and utilizes MongoDB as a spatial database for handling and storing geospatial data.

#### How to Run the Application

1. **Clone the Repository**  
   Clone this repository to your local machine using:

   `git clone https://github.com/karthik-s-dev/talkinglands.git`

2. Ensure **Python** is Installed
3. Create and Activate a Virtual Environment

  `python -m venv venv`
  `venv\Scripts\activate`

4. Install Dependencies

  `pip install -r requirements.txt`

5. Update the **.env** File
6. Run the Application
  `uvicorn main:app`
## MongoDB Schemas

### Point Collection

- `name`: String (Name of the point)
- `description`: String (Description of the point)
- `location`: Point (MongoEngine's Point field to store geospatial data)

### Polygon Collection

- `name`: String (Name of the Polygon)
- `description`: String (Description of the Polygon)
- `coordinates`: Polygon (MongoEngine's Polygon field to store geospatial polygon data)

## Pydantic Models

### Point Model (Request Body)

- `name`: String
- `description`: String
- `location`: list of floats (Format: `[longitude, latitude]`)

### Polygon Model (Request Body)

- `name`: String
- `description`: String
- `location`: list of (list of list of (floats)) (Format: `[   [     [lat,lang],[lat,lang],..   ]   ]`)

## API Endpoints

### POST /point

- **Description**: Creates a new point document.
- **Request Body**: `Point` model.
- **Responses**:
  - `201 Created`: Point created successfully.
  - `400 Bad Request`: Invalid data provided.  
  - `500 Failed to update point`: Invalid data provided.

### GET /point/{id}

- **Description**: Retrieves a point by its document ID.
- **Path Parameters**:
  - `id`: UUID (The ID of the point document)
- **Responses**:
  - `200 OK`: Successfully retrieved point.
  - `404 Not Found`: No point found with the given ID.

### PUT /point/{id}

- **Description**: Updates an existing point document.
- **Path Parameters**:
  - `id`: UUID (The ID of the point document)
- **Request Body**: `Point` model.
- **Responses**:
  - `200 OK`: Point updated successfully.
  - `404 Not Found`: No point found with the given ID.

### DELETE /point/{id}

- **Description**: Deletes a point by its document ID.
- **Path Parameters**:
  - `id`: UUID (The ID of the point document)
- **Responses**:
  - `200 OK`: Point deleted successfully.
  - `404 Not Found`: No point found with the given ID.

### GET /points

- **Description**: Retrieves a list of points.
- **Query Parameters**:
  - `start`: Integer (Pagination start index)
  - `end`: Integer (Pagination end index)
- **Responses**:
  - `200 OK`: List of points returned successfully.

### GET /points/bounding_box

- **Description**: Retrieves points within a specified bounding box.
- **Query Parameters**:
  - `north`: Float (Northern latitude of the bounding box)
  - `south`: Float (Southern latitude of the bounding box)
  - `east`: Float (Eastern longitude of the bounding box)
  - `west`: Float (Western longitude of the bounding box)
- **Responses**:
  - `200 OK`: List of points within the bounding box returned successfully.

### GET /points/radius

- **Description**: Retrieves points within a specified radius.
- **Query Parameters**:
  - `latitude`: Float (Central latitude of the search area)
  - `longitude`: Float (Central longitude of the search area)
  - `radius`: Float (Radius in meters)
- **Responses**:
  - `200 OK`: List of points within the radius returned successfully.



### POST /polygon

- **Description**: Creates a new polygon document.
- **Request Body**: `Polygon` model.
- **Responses**:
  - `201 Created`: Polygon created successfully.
  - `500 Failed to save polygon`: Invalid data provided.

### GET /polygon/{polygon_id}

- **Description**: Retrieves a polygon by its document ID.
- **Path Parameters**:
  - `id`: UUID (The ID of the polygon document)
- **Responses**:
  - `200 OK`: Successfully retrieved polygon.
  - `404 Not Found`: No polygon found with the given ID.

### PUT /polygon/{id}

- **Description**: Updates an existing polygon document.
- **Path Parameters**:
  - `id`: UUID (The ID of the polygon document)
- **Request Body**: `Polygon` model.
- **Responses**:
  - `200 OK`: Polygon updated successfully.
  - `404 Not Found`: No point found with the given ID.
  - `500 Failed to update polygon`: Invalid data provided.

### DELETE /polygon/{id}

- **Description**: Deletes a polygon by its document ID.
- **Path Parameters**:
  - `id`: UUID (The ID of the polygon document)
- **Responses**:
  - `200 OK`: Polygon deleted successfully.
  - `404 Not Found`: No polygon found with the given ID.

### GET /polygons

- **Description**: Retrieves a list of polygons.
- **Query Parameters**:
  - `start`: Integer (Pagination start index)
  - `end`: Integer (Pagination end index)
- **Responses**:
  - `200 OK`: List of polygons returned successfully.


### GET /polygons/bounding_box

- **Description**: Retrieves polygons within a specified bounding box.
- **Query Parameters**:
  - `north`: Float (Northern latitude of the bounding box)
  - `south`: Float (Southern latitude of the bounding box)
  - `east`: Float (Eastern longitude of the bounding box)
  - `west`: Float (Western longitude of the bounding box)
- **Responses**:
  - `200 OK`: List of polygons within the bounding box returned successfully.

### GET /polygons/radius

- **Description**: Retrieves polygons within a specified radius.
- **Query Parameters**:
  - `latitude`: Float (Central latitude of the search area)
  - `longitude`: Float (Central longitude of the search area)
  - `radius`: Float (Radius in meters)
- **Responses**:
  - `200 OK`: List of polygons within the radius returned successfully.
