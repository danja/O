import os
from urllib import request
from os.path import join, getsize

baseURL = "http://hyperdata.it/projects/"

for root, dirs, files in os.walk('../Projects'):
    # print(root, "consumes", end=" ")
    # print("Parent =", root)
    parentURL = baseURL+request.pathname2url(root)[3:]
    print(parentURL)
    # print(sum(getsize(join(root, name)) for name in files), end=" ")
    #print("bytes in", len(files), "non-directory files")
    for filename in files:
        # print(filename)
        url = parentURL+"/"+request.pathname2url(filename)
        print(url)
        with open(join(root, filename)) as file:
            lines = file.readlines()
            for line in lines:
                print(line)
