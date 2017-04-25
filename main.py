# coding=utf-8

import os
from os import path
import pickle
import hashlib
import pprint

def getHash(item):
    filename, fileext = os.path.splitext(item)
    hashedName = hashlib.sha1(path.basename(filename).encode()).hexdigest()+fileext
    return hashedName

# Variables
folders = dict()
hashes = open('hashes','wb')
ignore = list()

#Ignore list
ignore.append(os.path.basename(__file__))
ignore.append('__pycache__')
ignore.append('hashes.json')

def dirsearch(root='.'):
    folders[root]={'hash': getHash(root), 'items': dict()}
    for i in os.listdir(root):
        if i not in ignore:
            #print('Item : '+ i + ', root : ' + root + ', hash : ' + getHash(i))
            if os.path.isdir(path.join(root,i)):
                dirsearch(os.path.join(root,i))
            folders[root]['items'][i]=getHash(i)

dirsearch('.')
pickle.dump(folders,hashes)
pprint.pprint(folders)
hashes.close()
