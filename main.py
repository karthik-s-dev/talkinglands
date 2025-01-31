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


from fastapi import FastAPI
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


from pydantic_models import PointModel
from mongo_models import Point
import json

@app.post("/point")
async def create_point(point: PointModel):
    point = Point(name=point.name, description=point.description, location=point.location)
    point.save()
    return point.to_json()

@app.get("/points")
async def get_points(start:int=0,end:int=100):
    points = Point.objects().skip(start).limit(end - start)
    return [json.loads(point.to_json()) for point in points]