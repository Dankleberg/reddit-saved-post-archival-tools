import requests
import os

linksfile = input('Enter path to file with links: ')
links = []

with open(linksfile, "r", encoding="utf8") as file:
    links = file.readlines()
    for link in links:
        print(link.split()[1])
        print(os.path.basename(link.split()[1]) + "\n")
        print(os.path.basename(link.split()[1])[-3:])
        if '.' in link.split()[1] and (os.path.basename(link.split()[1])[-3:] == "jpg" or
                                       os.path.basename(link.split()[1])[-3:] == "png" or
                                       os.path.basename(link.split()[1])[-3:] == "gif" or
                                       os.path.basename(link.split()[1])[-3:] == "jpeg"):
            with open(rf"C:\Users\ament\Downloads\RedditSaved\SavedPictures\{os.path.basename(link.split()[1])}",
                      'wb') as handle:
                print(True)
                response = requests.get(link.split()[1], stream=True)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)
