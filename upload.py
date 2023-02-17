import requests
import os

def main(use_proxy=False):
    for file in os.listdir():
        if file.endswith(".py"):
            upload(file,use_proxy=use_proxy)
            
def upload(file,use_proxy=False):
    username = 'chiringuito17'
    token = 'f69bc95422a4b27a66fff92e3bb12d105fc0d888'
    host = 'www.pythonanywhere.com'
    path = f'/home/chiringuito17/FarmTelegramBot/{file}'
    files = {'content': open(file,'rb').read()}
    proxy = {'https': 'jose.cardenas@estudiantes.fbio.uh.cu:barca100@10.6.100.71:3128'}
    auth = ('jose.cardenas@estudiantes.fbio.uh.cu','barca100')

    response = requests.post(
        f'https://{host}//api/v0/user/{username}/files/path{path}',
        headers={'Authorization': f'Token {token}'},
        files=files,
        proxies=proxy if use_proxy else None
    )
    if response.status_code == 200:
        print('Successfully')
    else:
        print(response.status_code)

if __name__ == "__main__":
    main(use_proxy=True)