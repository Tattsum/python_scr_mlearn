# python_scr_mlearn
pythonによるスクレイピングと機械学習

# 開発環境
dockerで、Python3 + Anacondaの環境を構築する
docker の動作確認
```
$ docker run hello-world
```

## Python + Anacondaのイメージをダウンロード
ここではminicondaを使用する
```
$ docker pull continuumio/miniconda3 #イメージダウンロード
$ docker run -i -t continuumio/miniconda3 /bin/bash #dockerのコンテナのコンソールへ
$ python3 -c "print(12*3)"
36 #動作確認
```

## Python3のライブラリを追加
pip3やbsなどをDL
```
$ apt-get update
$ apt-get upgrade -y
$ apt-get install python3-pip
$ pip3 install beautifulsoup4
```
その他また追記で追加するかも...
