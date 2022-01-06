import os
import random
import string
from shutil import copyfile

n = 500

path = os.path.dirname(os.path.abspath(__file__))

user_profile = os.environ['USERPROFILE']

dirs = []
dirs.append(user_profile + "\\Desktop\\")
dirs.append(user_profile + "\\Documents\\")
dirs.append(user_profile + "\\Downloads\\")
dirs.append(user_profile + "\\Pictures\\")
dirs.append(user_profile + "\\Videos\\")
dirs.append(user_profile + "\\Music\\")

def randomString():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(8))

for i in range(n):

    variety = str(random.randint(0, 9))
    src = path + '\\sneks\\' + variety + '.jpg'
    name = randomString()
    dst = dirs[random.randint(0, len(dirs)-1)] + name + '.jpg'

    print(src, dst)
    copyfile(src, dst)
