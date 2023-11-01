from app.models.user_model import userModle as um
from app.data_classes.user_data_classes.user_data import UserData


class userController:
    def signup(userdata: UserData):
        result = um.signup(userdata)
        return result
