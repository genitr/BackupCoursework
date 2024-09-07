""" Модуль для работы с API VK и API Яндекс.Диска """

import requests

from src.app.settings import VKBase, VKMethods, YDMethods


class VK:
    """ Класс для работы с API VK """

    def __init__(self, user_id, token=VKBase.TOKEN, version=VKBase.API_VERSION) -> None:
        self.user_id = user_id
        self.access_token = token
        self.version = version
        self.params = {"access_token": self.access_token, "v": self.version}

    def get_max_photo_size(self, count=5, album_id='profile'):
        """ Возвращает фотографии профиля максимального размера """

        params = {
            "owner_id": self.user_id,
            "count": count,
            "album_id": album_id,
            "extended": 1
        }
        response = requests.get(VKMethods.PHOTOS_GET, params={**self.params, **params}, timeout=3)

        data = response.json()
        max_photo_size = []

        for item in data['response']['items']:
            likes = item["likes"]["count"]
            url = item['sizes'][-1]["url"]
            date = item['date']
            size = item['sizes'][-1]['type']

            photo_dict = {'likes': f'{likes}', 'url': url, 'date': date, 'size': size}
            max_photo_size.append(photo_dict)

        return max_photo_size


class YD:
    """ Класс для работы с API Яндекс.Диска """

    def __init__(self, access_token):
        self.access_token = access_token
        self.headers = {'Authorization': 'OAuth ' + self.access_token}

    def create_folder(self, folder_name):
        """ Создание новой папки на Яндекс.Диск """

        params = {'path': folder_name}

        response = requests.put(YDMethods.FILES, params=params, headers=self.headers)

        return response.status_code

    def upload_file(self, file_data: dict, folder_name: str):
        """ Загрузка файла на Яндекс.Диск """

        path = folder_name + '/' + file_data['likes']
        params = {'path': path, 'url': file_data['url']}

        response = requests.post(YDMethods.UPLOAD_FILE, params=params, headers=self.headers)

        return response.status_code

    def get_file_info(self, path, max_photo_size_source):
        """ Получение информации о файлах """

        params = {'path': path}

        response = requests.get(YDMethods.FILES, params=params, headers=self.headers)

        data = response.json()

        file_info_list, file_info_dict, image_size = [], {}, ''

        for i in data['_embedded']['items']:
            file_name = i['name'] + '.' + i['mime_type'].split('/')[-1]

            for j in max_photo_size_source:
                if i['name'] == j['likes']:
                    image_size = j['size']

                file_info_dict = {'file_name': file_name, 'size': image_size}

            file_info_list.append(file_info_dict)

        return file_info_list


if __name__ == '__main__':
    pass
