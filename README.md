# ThaiTTS
帮你读泰语的小玩意儿
# 安装
首先你电脑得有Python环境，没有的话请自行安装

创建虚拟环境并安装依赖，建议直接用PyCharm打开项目，PyCharm会自动创建虚拟环境并安装依赖
```bash
pip install -r requirements.txt
```
# 使用
修改text.txt文件，写入你想要合成的泰语文本，每一行文本是单独合成一个音频文件的

之后使用虚拟环境运行main.py
```bash
python main.py
```
合成的音频文件会保存在当前的文件夹中

如果不想要wav文件，可以转换为mp3文件
```bash
python wav2mp3.py
```
当然mp3文件需要ffmpeg支持，如果没有安装ffmpeg，可以去[官网](https://ffmpeg.org/download.html)下载安装