from pymongo import MongoClient

uri = "mongodb+srv://gangliatechnologies:XUwzWbVXpZKyjl3y@tripmacha.rg3vkkp.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client["travels"]
user_collection=db["user"]
plan_collection=db["trip"]
feedback_collection=db["feedback"]