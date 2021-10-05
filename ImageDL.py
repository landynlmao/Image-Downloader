import requests

def download_files(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        print("Downloading...")
        with open("C:/Users/LJ_44/Desktop/"+local_filename, 'wb') as f:
            print("Writing data to file")
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    f.close()
    print("Download Complete")
    print("File saved as "+ local_filename)

while 1:
    print("Welcome to hell")
    image_url = input(str("Image URL: "))
    download_files(image_url)
    print("")
