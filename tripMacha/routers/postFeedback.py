from fastapi import APIRouter
from config.database import feedback_collection
from models.SaveModel import FeedbackCollection
from bson import ObjectId
import pydantic.v1
from pprint import pprint

feedback_api_router=APIRouter()

# Create a custom encoder for ObjectId serialization
def encode_object_id(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")
# Add the custom encoder to pydantic's ENCODERS_BY_TYPE dictionary
pydantic.v1.json.ENCODERS_BY_TYPE[ObjectId] = encode_object_id

# Uncomment to enable feedbacks saving to mongoDB but will work if getforms is removed from the ConstactUs.jsx
# @feedback_api_router.post("/feedback")
# def createFeedback(feedback: FeedbackCollection):
#     data = feedback
#     new_feedback = {
#         "name" : data.name,
#         "email" : data.email,
#         "subject" : data.subject,
#         "messageContent" : data.messageContent
#     }

#     ins_feedback = feedback_collection.insert_one(new_feedback).inserted_id
#     return {"message": "inserted feedback", "feedback_id": str(ins_feedback)}  # Convert the ObjectId to str before returning

 