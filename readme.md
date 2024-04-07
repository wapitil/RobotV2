## 平台环境
- Ubuntu 20.04.5 LTS server
- python3.8

**项目介绍**
- Offline1_STT 离线语音识别
    -vosk-model-small-cn-0.22 语音模型
    -recording.py 录音
    -stt.py 语音识别主程序
- Offline2_Music 离线音乐识别
    - 
## 安装依赖项
下载clash-for-linux,修改变量**CLASH_URL**的值
```bash
$ git clone https://github.com/Elegycloud/clash-for-linux-backup.git
$ cd clash-for-linux
$ nano .env
```
然后启动项目
```bash
$ cd clash-for-linux
$ sudo bash start.sh
$ source /etc/profile.d/clash.sh
$ proxy_on
```
开启代理之后下载会缩短时间
```bash
$ sudo apt-get update
$ sudo apt-get install libgl1-mesa-glx
$ sudo apt-get install libsndfile1
$ sudo apt install alsa-utils
$ pip install -r requirement.txt
```

## 配置声卡
找出声卡设备的设备号，然后更改声卡设置，
```bash
$ aplay -l
$ sudo nano ~/.asoundrc
```
例如我的card是1，device是0
```text
pcm.!default {
    type asym
    playback.pcm {
        type plug
        slave.pcm "hw:1,0"
    }
    capture.pcm {
        type plug
        slave.pcm "hw:1,0"
    }
}

ctl.!default {
    type hw
    card 1
}
```

## 上传至github
### 生成ssh密钥
在终端输入前三行命令，然后使用第四行命令查看并复制您的SSH公钥到剪贴板：
```bash
$ ssh-keygen -t rsa -b 4096 -C "您的GitHub邮箱地址"
$ eval "$(ssh-agent -s)"
$ ssh-add ~/.ssh/id_rsa
$ cat ~/.ssh/id_rsa.pub
```
然后录到您的GitHub账户。
在右上角，点击您的头像，然后点击"Settings"。
在侧边栏中，点击"SSH and GPG keys"。
点击"New SSH key"或"Add SSH key"。点击“新建 SSH 密钥”或“添加 SSH 密钥”。
在"Title"字段中，为您的密钥添加一个描述性的标签。
在"Key"字段中，粘贴您的公钥。
点击"Add SSH key"。点击“添加 SSH 密钥”。

### 上传过程
1. 在树莓派上打开终端，使用以下命令安装Git：
```bash
$ sudo apt update
$ sudo apt install git
```

2. 配置Git用户名称和电子邮件地址：
```bash
$ git config --global user.name "您的GitHub用户名"
$ git config --global user.email "您的GitHub邮箱地址"
```

3. 创建GitHub仓库
登录到您的GitHub账户。
点击页面右上角的"+"，选择"New repository"。
填写仓库名称和描述（可选），选择仓库是否公开。
点击"Create repository"。点击“创建存储库”。

4. 初始化本地仓库
在树莓派上，导航到您的项目目录，然后初始化为Git仓库：
```bash
$ cd /路径/到/您的/项目
$ git init
```

5. 添加文件到仓库
将项目文件添加到仓库中,提交更改信息
```bash
$ git add .
$ git commit -m "首次提交"
```
这会添加目录中的所有文件。如果只想添加特定文件，可以使用git add 文件名。

6. 关联远程账户
```bash
$ git remote add origin https://github.com/用户名/仓库名.git
$ git push -u origin main
```