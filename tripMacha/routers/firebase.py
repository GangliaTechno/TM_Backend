from fastapi import FastAPI,APIRouter
from firebase_admin import auth

firebase_api_router= APIRouter()

NoUser = {
    'uid': None,
    'email': None,
    'display_name': None,
    'photo': 'https://logowik.com/content/uploads/images/cat8600.jpg',
    'phone_no': 9999999999
}


@firebase_api_router.get("/userinfo/{firebase_id}")
def get_user(firebase_id: str):
    user = auth.get_user(firebase_id)
    if (user):
        json_data = {
            'uid': user.uid,
            'email': user.email,
            'display_name': user.display_name,
            'photo':user.photo_url,
            'phone_no':user.phone_number}
        return json_data
    else:
        return NoUser