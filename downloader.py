import requests
import os

headers = {
    "x-press-shared-secret": "@_@", #it came to me in a dream
    "accept": "application/json,application/json",
    "user-agent": "Gumyocho ZRX 12.2.6",
    "accept-charset": "UTF-8",
    "connection": "Keep-Alive",
    "accept-encoding": "gzip"
}
log_file = 'log.txt'

if not os.path.exists(log_file):
    open(log_file, 'a').close()



with open('file', 'r') as file:
    urls = file.readlines()


for url in urls:
    url = url.strip()
    try:
        response = requests.get(url, headers=headers, allow_redirects=True)
        response.raise_for_status()


        filename = url.split("/")[-1]

        with open(filename, 'wb') as f:
            f.write(response.content)

        with open(log_file, 'a') as log:
            log.write(f"downloaded {filename}" + '\n')

        print(f"downloaded {filename}")

    except requests.exceptions.HTTPError as err:
        error_message = f"{url} failed to download: HTTP error: {err}"
        print(error_message)
        with open(log_file, 'a') as log:
            log.write(error_message + '\n')

    except requests.exceptions.RequestException as err:
        error_message = f"{url} failed to download: Request error: {err}"
        print(error_message)
        with open(log_file, 'a') as log:
            log.write(error_message + '\n')

    except Exception as err:
        error_message = f"{url} failed to download: {err}"
        print(error_message)
        with open(log_file, 'a') as log:
            log.write(error_message + '\n')
