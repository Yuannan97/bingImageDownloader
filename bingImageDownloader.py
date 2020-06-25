from bing_image_downloader import downloader
import cv2
import os

#firstly, youshould pip3 install bing-image-downloader
#example  downloadImges('technology', 'dataset/', 'image', 1, (1600,1000))
#use default arguments  downloadImages('communication)
#query and type should be a string. quantity should be an integer. Size to be a tuple.

def resize(subDir, size, storePath):
    path_to_imgDatabase = 'dataset/bing/'
    path  = path_to_imgDatabase + subDir
    l = subDir.split(' ')
    storeFile = storePath + l[0] + '.jpg'

    for root, dirs, files in os.walk(path):
        for file in files:
            imgPath = os.path.join(root,file)
            img = cv2.imread(imgPath)
            img = cv2.resize(img,size)
            print(storeFile)
            cv2.imwrite(storeFile,img)
            #cv2.imwrite(imgPath,img)

def downloadImges(query, storePath = 'dataset/bing/', imgType = 'image', quantity = 1, size = (1600,900)):
    search = query + ' ' + imgType
    try:
        downloader.download(search, limit= quantity, adult_filter_off=True, force_replace=False)
        resize(search,size, storePath)
    except FileNotFoundError:
        downloader.download(query, limit= quantity, adult_filter_off=True, force_replace=False)
        resize(query, size, storePath)
