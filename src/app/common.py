import json


def photo_info(file_info):
    with open('file_info.json', 'w', encoding='utf-8') as f:
        json.dump(file_info, f, ensure_ascii=False, indent=2)


def separator(title: str):
    print(title)
    print('--------------------------------------------------------')


if __name__ == "__main__":
    pass


