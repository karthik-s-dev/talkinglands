# Talking Lands API Documentation

This document provides a comprehensive guide on how to interact with the Talking Lands backend server, which is developed using Python's FastAPI and utilizes MongoDB as a spatial database for handling and storing geospatial data.

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

