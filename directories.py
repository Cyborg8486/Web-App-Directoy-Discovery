import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


def discover_directories(target_url, file_name):
    file = open(file_name, 'r')
    for line in file:
        directory = line.strip()
        full_url = target_url + '/' + directory
        response = request(full_url)
        if response:
            print('[*] Discovered Directory At This Path: ' + full_url)


if __name__ == "__main__":
    target_url = input('[*] Enter Target URL: ')
    file_name = input('[*] Enter Name Of The File Containing Directories: ')
    discover_directories(target_url, file_name)
