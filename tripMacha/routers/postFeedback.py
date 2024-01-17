from fastapi import APIRouter
from config.database import feedback_collection
from models.SaveModel import FeedbackCollection
from bson import ObjectId
import pydantic.v1

feedback_api_router=APIRouter()

# Create a custom encoder for ObjectId serialization
def encode_object_id(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")
# Add the custom encoder to pydantic's ENCODERS_BY_TYPE dictionary
pydantic.v1.json.ENCODERS_BY_TYPE[ObjectId] = encode_object_id
@feedback_api_router.post("/feedback")
def createFeedback(feedback: FeedbackCollection):
    data = feedback.dict()
    ins_feedback = feedback_collection.insert_one(data).inserted_id
    return {"message": "inserted feedback", "feedback_id": str(ins_feedback)}  # Convert the ObjectId to str before returning

 