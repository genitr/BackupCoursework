""" Модуль содержит различные настройки приложения """

import os
from enum import StrEnum

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class VKBase(StrEnum):
    VK_TOKEN = os.getenv("VK_TOKEN")
    VK_BASE_URL = os.getenv("VK_URL")
    VK_USER_ID = os.getenv("VK_USER_ID")
    VK_TEST_USER_ID = os.getenv('VK_TEST_USER_ID')
    VK_API_VERSION = "5.199"


class VKMethods(StrEnum):
    PHOTOS_GET = VKBase.VK_BASE_URL + 'photos.get'
