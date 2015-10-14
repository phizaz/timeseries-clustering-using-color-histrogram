import json

class File:

    @staticmethod
    def save(var, file_path):
        with open(file_path, 'w') as outfile:
            json.dump(var, outfile)

    @staticmethod
    def open(file_path):
        with open(file_path, 'r') as readfile:
            return json.load(readfile)


