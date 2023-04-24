import requests
import os

linksfile = input(r'Enter path to file with links: ')
linksfile = linksfile.strip('"');
outputdirectory = input(r"Enter directory you would like to save images to: ")
outputdirectory = outputdirectory.strip('"');
links = []

with open(linksfile, "r", encoding="utf8") as file:
    links = file.readlines()
    for link in links:
        print(os.path.basename(link.split()[1]) + "\n")
        if '.' in link.split()[1] and (os.path.basename(link.split()[1])[-3:] == "jpg" or
                                       os.path.basename(link.split()[1])[-3:] == "png" or
                                       os.path.basename(link.split()[1])[-3:] == "gif" or
                                       os.path.basename(link.split()[1])[-4:] == "jpeg"):
            with open(rf"{outputdirectory}\{os.path.basename(link.split()[1])}",
                      'wb') as handle:
                response = requests.get(link.split()[1], stream=True)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)
