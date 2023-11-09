from app.models.directory_model import directoryModle


class directoryController:
    def top():
        result = directoryModle.top()
        return result

    def file(file_path: str):
        result = directoryModle.file(file_path)
        return result
