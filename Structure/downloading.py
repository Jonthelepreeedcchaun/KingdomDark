def dl_file(url, filename, path=''):
    import requests
    headers = requests.utils.default_headers()
    x = requests.get(url, headers=headers)
    if path=='':
        with open(filename, 'wb') as file:
            file.write(x.content); file.close()
    else:
        if not os.path.isdir(path): os.makedirs(path)
        with open(os.path.join(path,filename), 'wb') as file:
            file.write(x.content); file.close()

def dl_content(url):
    import requests
    headers = requests.utils.default_headers()
    x = requests.get(url, headers=headers)
    return x.text
