from dotenv import dotenv_values
config = {**dotenv_values(".env")}

try:
    db_url = config['DATABASE_URL']
    db_name = config['DATABASE_NAME']
except KeyError:
    print("Please check the '.env' file.")
    exit(1)


from mongoengine import connect
connect(host = db_url)


from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def test():
    return {"message":"Running good :)"}


from pydantic_models import PointModel, PolygonModel
from mongo_models import Point, Polygon
import json


########  POINTS APIs #############
@app.post("/point")
async def create_point(point: PointModel):
    point = Point(name=point.name, description=point.description, location=point.location)
    point.save()
    return json.loads(point.to_json())

@app.get("/point/{point_id}")
async def get_point(point_id:str):
    point = Point.objects(id=point_id).first()
    if point:
        return json.loads(point.to_json())
    else:
        raise HTTPException(status_code=404, detail="Point not found")

@app.put("/point/{point_id}")
async def put_point(point_id:str,point: PointModel):
    point_doc = Point.objects(id=point_id).first()
    if point_doc:
        point_doc.update(name=point.name, description=point.description, location=point.location)
        return json.loads(point_doc.to_json())
    else:
        raise HTTPException(status_code=404, detail="Point not found")

@app.delete("/point/{point_id}")
async def delete_point(point_id:str):
    point_doc = Point.objects(id=point_id).first()
    if point_doc:
        point_doc.delete()
        return {"message":"Deleted successfully."}
    else:
        raise HTTPException(status_code=404, detail="Point not found")

@app.get("/points")
async def get_points(start:int=0,end:int=100):
    points = Point.objects().skip(start).limit(end - start)
    return [json.loads(point.to_json()) for point in points]

@app.get("/points/bounding_box")
async def get_points_within_bbox(north: float, south: float, east: float, west: float):
    points = Point.objects(
        location_marker__geo_within_box=[(west, south), (east, north)]
    )
    return [json.loads(point.to_json()) for point in points]

@app.get("/points/radius")
async def get_points_within_radius(longitude: float, latitude: float, max_distance: float = 1000):
    points = Point.objects(location__near=[longitude, latitude], location__max_distance=max_distance)
    return [json.loads(point.to_json()) for point in points]














########  POLYGON APIs #############


@app.post("/polygon")
def create_polygon(polygon: PolygonModel):
    try:
        polygon_doc = Polygon(
            name=polygon.name,
            description=polygon.description,
            coordinates=polygon.coordinates
        )
        polygon_doc.save()
        return json.loads(polygon_doc.to_json())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save polygon: {str(e)}")

@app.get("/polygon/{polygon_id}")
def get_polygon(polygon_id: str):
    polygon = Polygon.objects(id=polygon_id).first()
    if not polygon:
        raise HTTPException(status_code=404, detail="Polygon not found")
    return json.loads(polygon.to_json())

@app.put("/polygon/{polygon_id}")
def update_polygon(polygon_id: str, polygon: PolygonModel):
    polygon_doc = Polygon.objects(id=polygon_id).first()
    if not polygon_doc:
        raise HTTPException(status_code=404, detail="Polygon not found")
    try:
        polygon_doc.update(
            name=polygon.name,
            description=polygon.description,
            coordinates=polygon.coordinates
        )
        return {"message": "Polygon updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update polygon: {str(e)}")
    

@app.delete("/polygon/{polygon_id}")
def delete_polygon(polygon_id: str):
    polygon_doc = Polygon.objects(id=polygon_id).first()
    if not polygon_doc:
        raise HTTPException(status_code=404, detail="Polygon not found")
    polygon_doc.delete()
    return {"message": "Polygon deleted successfully"}

@app.get("/polygons")
def get_all_polygons(start: int = 0, end: int = 100):
    polygons = Polygon.objects().skip(start).limit(end - start)
    return [json.loads(polygon.to_json()) for polygon in polygons]


@app.get("/polygons/bounding_box")
def get_polygons_in_bbox(north: float, south: float, east: float, west: float):
    polygons = Polygon.objects(
        coordinates__geo_within_box=[(west, south), (east, north)]
    )
    return [json.loads(polygon.to_json()) for polygon in polygons]

@app.get("/polygons/radius")
def get_polygons_radius(longitude: float, latitude: float, max_distance: float = 1000):
    polygons = Polygon.objects(
        coordinates__near=[longitude, latitude],
        coordinates__max_distance=max_distance
    )
    return [json.loads(polygon.to_json()) for polygon in polygons]