import requests
import os

path_text = "celine_farach.txt"

f = open(path_text,'r')
url = f.read()
f.close()

urls = url.split()
# print("Number of urls: {}".format(len(urls)))
# print("__________________________")
#
# for i in urls[:20]:
#     print(i)


# loc_data = "./data/"
# try:
#     os.makedirs(loc_data)
# except:
#     pass
# iimage = 0
# for i in urls:
#     try:
#         f = open(loc_data + 'image{:05.0f}.jpg'.format(iimage),'wb')
#         f.write(requests.get(i).content)
#         f.close()
#         iimage += 1
#     except Exception as e:
#         print("\n{} {}".format(e,i))
#         pass


