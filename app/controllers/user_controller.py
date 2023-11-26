from app.models.user_model import userModel
from app.data_classes.user_data_classes.user_data import UserData


class userController:
    def login(user_data: UserData):
        login_dto = userModel.login(user_data)
        return login_dto
