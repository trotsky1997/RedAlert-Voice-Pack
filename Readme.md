# RedAlert Voice Pack

![Avatar](avatar.jpg)

红警盟军女性语音包,代码遵从 MIT 许可.音乐版权归属于 ©EA

Female Voice pack, code licensed by MIT. Music copyright belongs to EA

使用 EasyVoicePackTool 工具构建.

## 工具使用方法

1. 在`saekiraku.rainbow-fart\voice-packages`目录下克隆本仓库 `git clone https://github.com/trotsky1997/RedAlert-Voice-Pack`
`cd RedAlert-Voice-Pack` 
2. 删除本仓库内的语音文件 `rm -rf *.mp3` 
3. 将您要使用的语音文件放入本文件夹 
4. 修改`EasyVoicePackTool.py`内的语音包信息 `info`

```json
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
```

5. 执行`Python EasyVoicePackTool.py`
