""" Модуль содержит различные настройки приложения """

import os
from enum import StrEnum

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class VKBase(StrEnum):
    TOKEN = os.getenv("VK_TOKEN")
    BASE_URL = os.getenv("VK_URL")
    USER_ID = os.getenv("VK_USER_ID")
    TEST_USER_ID = os.getenv('VK_TEST_USER_ID')
    API_VERSION = "5.199"


class VKMethods(StrEnum):
    PHOTOS_GET = VKBase.BASE_URL + 'photos.get'


class YDBase(StrEnum):
    TOKEN = os.getenv('YANDEX_TOKEN')
    BASE_URL = os.getenv('YANDEX_URL')


class YDMethods(StrEnum):
    FILES = YDBase.BASE_URL + 'resources'
    UPLOAD_FILE = YDBase.BASE_URL + 'resources/upload'
