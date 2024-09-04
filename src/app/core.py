""" Модуль для работы с API VK и API Яндекс.Диска """

import requests

from settings import VKBase, VKMethods, YDBase, YDMethods


class VK:
    """ Класс для работы с API VK """

    def __init__(self, token=VKBase.TOKEN, version=VKBase.API_VERSION) -> None:
        self.access_token = token
        self.version = version
        self.params = {"access_token": self.access_token, "v": self.version}

    def get_max_photo_size(self, owner_id=VKBase.TEST_USER_ID, count=5, album_id='profile'):
        """ Возвращает фотографии профиля максимального размера """

        params = {
            "owner_id": owner_id,
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

            photo_dict = {'likes': likes, 'url': url, 'date': date, 'size': size}
            max_photo_size.append(photo_dict)

        return max_photo_size


class YD:
    """ Класс для работы с API Яндекс.Диска """

    def __init__(self, access_token=YDBase.TOKEN):
        self.access_token = access_token
        self.headers = {'Authorization': 'OAuth ' + self.access_token}

    def create_folder(self, folder_name):
        params = {'path': folder_name}

        response = requests.put(YDMethods.FILES, params=params, headers=self.headers)

        return response.status_code

    def upload_file(self, folder: str, file_data: dict):
        path = folder + f'/{file_data['likes']}'
        params = {'path': path, 'url': file_data['url']}

        response = requests.post(YDMethods.UPLOAD_FILE, params=params, headers=self.headers)

        return response.status_code


if __name__ == '__main__':
    from pprint import pprint

    #vk = VK()
    #photos_list = vk.get_max_photo_size()
    #pprint(photos_list)
    yd = YD()

    pprint(yd.get_filename('Images'))
    #yd.create_folder('Images')

    #for item in photos_list:
    #    print(yd.upload_file('Images', item))
