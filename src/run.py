from time import sleep
from tqdm import tqdm

from app.core import VK, YD
from app.common import photo_info, separator


def main(vk, yd):
    """ Функция для запуска программы """

    photos_list = vk.get_max_photo_size()

    backup_folder = 'BackupPhoto'

    status_code = yd.create_folder(backup_folder)

    if status_code == 201:
        for i in tqdm(photos_list, desc='резервное копирование файлов', colour='green', leave=False):
            sleep(0.01)
            yd.upload_file(i, backup_folder)
    elif status_code == 409:
        print('Папка BackupPhoto уже существует! Хотите продолжить?')
        folder_error = input('Введите название для новой папки или "да", чтобы продолжить: ')

        if folder_error.lower() == 'да' or folder_error.lower() == '"да"':
            for i in tqdm(photos_list, desc='резервное копирование файлов', colour='green', leave=False):
                sleep(0.01)
                yd.upload_file(i, backup_folder)
        else:
            backup_folder = folder_error
            yd.create_folder(backup_folder)

            for i in tqdm(photos_list, desc='резервное копирование файлов', colour='green', leave=False):
                sleep(0.01)
                yd.upload_file(i, folder_error)

    else:
        raise 'Неизвестная ошибка, перезапустите программу'

    separator('резервное капирование прошло успешно')

    sleep(3)
    info = yd.get_file_info(backup_folder, photos_list)

    for _ in tqdm(info, desc='запись информации о файлах', leave=False):
        sleep(0.1)
        photo_info(info)

    separator('информация о файлах сохранена в file_info.json')


if __name__ == '__main__':
    user_id = input('Введите id пользователя vk: ')
    access_token = input('Введите токен с Полигона Яндекс.Диска: ')

    vkontakte = VK(user_id)
    yandex = YD(access_token)

    separator('')

    for _ in tqdm(range(2000), desc='подключение...', colour='green', leave=False):
        sleep(0.00001)

    separator(f'user id: {user_id} \naccess token: {access_token}')
    separator(f'Будет создана папка BackupPhoto для загрузки файлов')
    sleep(1)

    main(vkontakte, yandex)
