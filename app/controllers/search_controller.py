from app.models.search_model import searchModle
from app.data_classes.search_data_classes.search_data import SearchConditions


class searchController:
    def search(search_conditions: SearchConditions):
        result = searchModle.login(search_conditions)
        return result
