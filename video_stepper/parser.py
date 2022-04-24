import os
import json
from typing import List


class PlaylistFileParser:
    def __init__(self, file: str):
        self.file = file

        ext = os.path.splitext(self.file)[-1]
        if ext == '.json':
            self.parse = self.__parse_json
        elif ext == '.csv':
            self.parse = self.__parse_csv
        else:
            raise ValueError(f'file type "{ext}" was recieved.')

    def parse(self) -> List[str]:
        """Parse function to be overridden on instantiation
            depending on if a json or csv is passed"""
        pass

    def __parse_json(self) -> List[str]:
        with open(self.file, 'r') as json_data:
            data = json.load(json_data)
        return data['data']

    def __parse_csv(self) -> List[str]:
        with open(self.file, 'r') as csv_data:
            data = csv_data.readlines()
        return self.__format_csv_data(data)

    @staticmethod
    def __format_csv_data(data: List[str]) -> List[str]:
        return [line.split(',')[0] for line in data[1:]]


if __name__ == '__main__':
    parser = PlaylistFileParser('data/star-wars-release.json')
    print(parser.parse())
