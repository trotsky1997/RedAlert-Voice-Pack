import glob
import json
import os
files = glob.glob("*.mp3")

with open('./temp.json', "r") as f:
    temp = json.load(f, encoding="utf-8")
mapper = {tuple(i["keywords"]): i['voices'][0][0:i['voices'][0].find('0')]
          for i in temp["contributes"]}
keys = [i["keywords"] for i in temp["contributes"]]
num = len(keys)
for i, ix in enumerate(temp["contributes"]):
    ix["voices"] = files[i * len(files) // len(keys)
                                 :(i+1) * len(files) // len(keys)]

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
  "name": "RedAlert-Voice-Pack", #文件夹名称
  "display-name": "RedAlert Voice Pack", #语音包名称
  "avatar": "avatar.jpg", #封面
  "avatar-dark": "avatar-dark.jpg", #暗光风格封面
  "version": "0.0.1", #版本号
  "description": "Let's Rock! Commander!", #简介
  "languages": ["javascript"], #在哪些编程环境下启用本语音包
  "author": "Trotsky1997 Coded.Music by©EA-WestWood", #作者
  "gender": "female", #发音性别
  "locale": "en" #发音语言
}
os.remove('./manifest.json')
with open('./manifest.json', "w+") as f:
    json.dump(info, f)
