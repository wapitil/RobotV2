## 平台环境
- Ubuntu 20.04.5 LTS server
- python3.8

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