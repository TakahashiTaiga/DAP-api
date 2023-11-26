from app.data_classes.user_data_classes.user_data import UserData
from execut_sql_impl.execute_sql import executeSql


class loginExecuteSqlImpl:
    def __init__(self, email, encryptedpass):
        self.email = email
        self.encryptedpass = encryptedpass
        self.execute_sql = executeSql()

        self.sql = "SELECT user_id, user_name FROM users WHERE email = {} AND password = {}".format(
            self.email, self.encryptedpass)

    def execute_login(self):
        self.execute_sql.create_connection()
        result = self.execute_sql.execute_sql(self.sql)
        self.execute_sql.close_coonnection()

        return result
