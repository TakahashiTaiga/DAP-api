from app.data_classes.user_data_classes.user_data import UserData
from app.dto_classes.login_dto import LoginDto
from app.execut_sql_impl.user_execute_sql_impl import login_execute_sql_impl


class userModel:
    async def login(user_data: UserData):
        email = UserData.email
        # encript
        encryptedpass = UserData.password

        # sql
        result = login_execute_sql_impl(email, encryptedpass)

        # insert data to dto
        login_dto = LoginDto(user_ig=result.user_id,
                             user_name=result.user_name)

        return login_dto
