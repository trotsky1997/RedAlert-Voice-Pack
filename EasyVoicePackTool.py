import glob
import json
import os
files = glob.glob("*")
for i in glob.glob("*.py") + glob.glob("*.json")+glob.glob("*.jpg"):
    files.remove(i)
with open('./temp.json', "r") as f:
    temp = json.load(f, encoding="utf-8")
mapper = {tuple(i["keywords"]): i['voices'][0][0:i['voices'][0].find('0')]
          for i in temp["contributes"]}
keys = [i["keywords"] for i in temp["contributes"]]
num = len(keys)
for i, ix in enumerate(temp["contributes"]):
    ix["voices"] = files[i * len(files) // len(keys):(i+1) * len(files) // len(keys)]

for i, ix in enumerate(temp["contributes"]):
    for j, jx in enumerate(ix["voices"]):
        oldname = jx
        os.rename(oldname, oldname+'_')
for i, ix in enumerate(temp["contributes"]):
    for j, jx in enumerate(ix["voices"]):
        oldname = jx
        newname = mapper[tuple(ix["keywords"])] + f'{j + 1:02d}.mp3'
        os.rename(oldname+'_', newname)
        ix["voices"][j] = newname
os.remove('./contributes.json')
with open('./contributes.json', "w+") as f:
    json.dump(temp, f)
info = {
    "name": "RedAlert",
    "display-name": "RedAlert Voice Pack",
    "avatar": "avatar.jpg",
    "avatar-dark": "avatar-dark.jpg",
    "version": "0.0.1",
    "description": "Let's Rock! Commander!",
    "languages": ["javascript"],
    "author": "Trotsky1997 Coded.Music by©EA-WestWood",
    "gender": "female",
    "locale": "en"
}
os.remove('./manifest.json')
with open('./manifest.json', "w+") as f:
    json.dump(info, f)
