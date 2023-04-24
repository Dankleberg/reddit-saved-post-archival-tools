import os

directory = input('Enter path to "sub" directory: ')
links = []

for file in os.listdir(directory):
    filepath = os.path.join(directory, file)
    if os.path.isfile(filepath):
        try:
            lines = open(filepath, 'r', encoding="utf8").readlines()
        except:
            lines = open(filepath, 'r').readlines()
        finally:
            for line in lines:
                if "</span><a href=" in line:
                    link_start = line.index('f="')
                    if "</span><a href=" in line:
                        link_end = line.index('" target')
                    elif "<li><a href=" in line:
                        link_end = line.index('">')
                    if "imgur.com/a" in line:
                        links.append(rf"{os.path.splitext(os.path.basename(file))[0]}: {line[link_start + 3:link_end]}/zip")
                    else:
                        links.append(rf"{os.path.splitext(os.path.basename(file))[0]}: {line[link_start + 3:link_end]}")

for link in links:
    print(link)

linkfile = open(os.path.join(directory, "output.txt"), "w")
links.sort()
for link in links:
    linkfile.write(link + "\n")
linkfile.close()