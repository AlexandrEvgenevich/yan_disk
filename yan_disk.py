import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_link(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': f"OAuth {token}"}
        params = {'path': file_path, 'overwrite': 'true'}
        link = requests.get(url, headers=headers, params=params)
        return link.json()

    def upload(self, file_path: str):
        href_json = self.get_link(file_path=file_path)
        href = href_json['href']
        up = requests.put(href, data=open(path_to_file, 'rb'))
        up.raise_for_status()
        if up.status_code == 201:
            print('success')


if __name__ == '__main__':

    path_to_file = 'rat.txt'
    token = ...
    uploader = YaUploader(token)
    uploader.upload(path_to_file)


