#!./venv/bin/python
import json
import uuid


class FileStorage(object):

    __file_path = 'conversation.json'
    __data = {}

    def all(self):
        return self.__data
    
    def new(self, obj):
        id = str(uuid.uuid4())
        self.__data[id] = obj

    def save(self):
        ''' saves the object to a json file '''
        new_obj = {}
        for key, value in self.__data.items():
            new_obj.update({key: value})
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(new_obj, file)

    def reload(self):
        ''' reloads the object from a json file '''
        try:
            with open(self.__file_path, 'r') as file:
                file_content = json.load(file)
                for key, value in file_content.items():
                    self.__data.update({key: value})
        except FileNotFoundError:
            pass