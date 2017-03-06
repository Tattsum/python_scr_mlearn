# python_scr_mlearn
[pythonによるスクレイピングと機械学習](https://www.amazon.co.jp/dp/4802610793)

# 開発環境
docker の動作確認
```
$ docker run hello-world
```

## Python + Anacondaのイメージをダウンロード 1-1から2-1まで
ここではminicondaを使用する
```
$ docker pull continuumio/miniconda3 #イメージダウンロード
$ docker run -i -t continuumio/miniconda3 /bin/bash #dockerのコンテナのコンソールへ
$ python3 -c "print(12*3)"
36 #動作確認
```

## Python3のライブラリを追加
1-1から2-1まで
pip3やbsなどをDL
```
$ apt-get update
$ apt-get upgrade -y
$ apt-get install python3-pip python3-requests
$ pip3 install beautifulsoup4
```
その他また追記で追加するかも...


## Selenium + PhantomJSの実行環境
2-2から
dockerにubuntu16.04を導入し、Selenium + PhantomJSの環境を整える
```
$ docker pull ubuntu:16.04
$ docker run -it ubuntu:16.04
```

ubuntu16.04上にPython3とSeleniumをインストール
```
$ apt-get update
$ apt-get upgrade
$ apt-get install -y python3 python3-pip python3-requests
$ pip3 install selenium
$ pip3 install beautifulsoup4
```

続いて、PhantomJSをインストール
```
$ apt-get install -y wget libfontconfig
$ mkdir -p /home/root/src && cd $_
$ wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
$ tar jxvf phantomjs-2.1.1-linux-x86_64/bin/
$ cd phantomjs/bin/
$ cp phantomjs /usr/local/bin/
```

日本語フォントが表示されるように調整
```
$ apt-get install -y fonts-migmix
$ cat <<EOF > /etc/fonts/local.conf
<?xml version="1.0"?>
<?DOCTYPE fontconfig SYSTEM "fonts.dtd">
  <fontconfig>
    <match target="pattern">
      <test qual="any" name="family">
        <string>serif</string>
      </test>
      <edit name="family" mode="assign" binging="strong">
        <string>MigMix 2P</string>
      </edit>
  </match>
</fontconfig>
EOF
```

docker imageをcommit
```
$ docker ps -a
# ここにあるコンテナIDをコピペ
$ docker commit (コンテナID) ubuntu-phantomjs
```

日本語設定
```
docker run -it -v $HOME:$HOME \
    -e LANG=ja_JP.UTF-8 \
    -e PYTHONIOENCODING=utf_8 \
    ubuntu-phantomjs /bin/bash
```

## python3 ライブラリ追加
3-3から追加 上記のdocker上で追加する
```
$ pip3 install pyyaml
$ pip3 install openpyxl
$ pip3 install pandas
```

## Python + MySQLの開発環境
dockerを利用し、Python+MySQLの開発環境を構築
3-2のより
```
$ docker pull ubuntu:16.04
$ docker run -it ubuntu:16.04
```

ログイン後
```
$ apt-get update
$ apt-get upgrade
$ apt-get install -y python3 python3-pip python3-requests
$ apt-get install -y mysql-server
$ apt-get install -y libmysqlclient-dev
$ pip3 install mysqlclient
```
docker imageをcommit
```
$ docker ps -a
# ここにあるコンテナIDをコピペ
$ docker commit (コンテナID) ubuntu-mysql
```

日本語設定
```
docker run -it -v $HOME:$HOME \
    -e LANG=ja_JP.UTF-8 \
    -e PYTHONIOENCODING=utf_8 \
    ubuntu-mysql /bin/bash
```

## mysqlを起動
起動させて、BDを作成
```
$ server mysql start
$ mysql -u root -p
mysql > CREATE DATABASE test;
```

## モジュール追加
追加するモジュール
```
$ pip3 install tinydb
$ pip3 install -U scikit-learn scipy matplotlib scikit-image
$ pip3 install pandas
$ pip3 install numpy
```

## Webアプリを実行する
dockerでPython実行する場合は以下を参照
```
$ docker run -it \
  -v $HOME:$HOME \
  -p 8080:8080 mlearn
```

## Ubuntu Linux (Docker)にtenorFlowをインストール
- 公式サイトよりdockerのイメージを配布している
```
$ docker run -it b.gcr.io/tenorflow/tensorflow:latest-devel
```

- 手元がLinux OSの場合
```
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install -y wget
$ cd ~/
$ wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
$ chomd 766 Anaconda3-4.2.0-Linux-x86_64.sh
$ ./Anaconda3-4.2.0-Linux-x86_64.sh
```

その後インストーラーが出てきて指示に従ってインストール。そのあとにtenorFlowをインストール
```
$ conda create -n tensorflow python=3.4
```

- MacOSの場合
```
$ brew update
$ brew install pyenv
$ export PYENV_ROOT="$HOME/.pyenv"
$ export PATH = "$PYENV_ROOT/bin:$PATH"
$ eval "$(pyenv init _)"
$ pyenv install Anaconda3-4.1.1
$ pyenv global Anaconda3-4.1.1
$ pyenv rehash
$ sudo easy_install pip
```

そのあとにtensorflowをインストール
```
$ export TF_BINARY_URL=https://storage.googleapis.com/tesnsorflow/mac/cpu/tensorflow-0.10.0-py3-none-any.whl
$ pip3 install --upgrade $TF_BINARY_URL
```

## Jupyter Notebookのセットアップ
Jupyter Notebookをインストール
```
$ pip3 install --upgrade pip3
$ pip3 install jupyter
```

## keras のインストール
kerasはPyPIを使う
```
$ pip3 install keras
$ vim ~/.keras/keras.json
  {
    "image_dim_ordering": "tf",
    "epsilon": "1e-07",
    "floatx": "float32",
    "backend": "tensorflow"
  }
```

## ライブラリのインストール
形態素解析に使われるライブラリ。インストールする
```
$ apt-get install -y mecab libmecab-dev mecab-ipadic
$ apt-get install -y mecab-ipadic-utf8
$ apt-get install -y libc6-dev build-essential
$ pip3 install mecab-python3
$ pip3 install janome
$ pip3 install gensim
```
