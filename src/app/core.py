""" Модуль для работы с API VK и API Яндекс.Диска """

import requests

from settings import VKBase, VKMethods


class VK:
    """ Класс для работы с API VK """

    def __init__(self, token=VKBase.VK_TOKEN, version=VKBase.VK_API_VERSION) -> None:
        self.access_token = token
        self.version = version
        self.params = {"access_token": self.access_token, "v": self.version}

    def get_max_photo_size(self, owner_id=VKBase.VK_TEST_USER_ID, count=5, album_id='profile'):
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
            d = item['date']

            photo_dict = {'likes': likes, 'url': url, 'date': d}
            max_photo_size.append(photo_dict)

        return max_photo_size


if __name__ == '__main__':
    from pprint import pprint

    vk = VK()
    pprint(vk.get_max_photo_size())
