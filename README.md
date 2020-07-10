![NO SUPPORT](http://add.sh/images/no-support.png) ![NO GUARANTEE](http://add.sh/images/no-guarantee.png)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# gnow :: **g**it commit for **now**

## 注意

このソフトウェアはサポート無し・動作保証無しです。第三者からの要望は受け付けていません。

## 説明

git commit と git push を行うためのコマンド 'gnow' です。

発音: グナウ[gnaʊ]

## ダウンロード

```
cd /home/YOUR-DIR/
git clone https://github.com/addshlab/gnow.git
```

## インストール

```
$ sh install.sh
```

sudo実行パスワードを求められます。

`/usr/local/bin/` に `bin/gnow` のシンボリックリンクを貼ってコマンド化します。

## アンインストール

```
$ sh uninstall.sh
```

## メッセージの意味

### install.sh / uninstall.sh

* create 'gnow' command. -> gnow コマンドの作成に成功した
* delete 'gnow' command. -> gnow コマンドの削除に成功した
* failed create 'gnow' command. ｰ> gnow コマンドの作成に失敗した
* 'gnow' command already exist. -> gnow コマンドが既に存在する
* 'gnow' file not found. -> gnow コマンドの実体ファイルが無い。ダウンロードが正常にできてないかったり、ファイルの一部が削除されている可能性がある

### gnow

* Ready? 'no' or press ENTER -> 準備ができましたか。no と書いて中止するか、そのままエンターキーを押して実行してください
* (補足) no 以外に、NO と n、Ctrl-c でも中止できます

## 使い方

### 引数なし


```
$ gnow
```

* `git status` のファイルの状態をコミットメッセージとしてコミット
* カレントブランチに `git push`

### メッセージ引数あり

```
$ gnow README追加
```

* 引数に指定したメッセージでコミット
* カレントブランチに `git push`

## コメント

* 殆どの場合カレントブランチにコミットするのでブランチ指定の機能は削除した
* gitそのものに関する設定は事前に行っておいてください

## 履歴

* 2020-07-10 コミットメッセージの任意追加機能
* 2020-07-10 リポジトリ名 gnow, gnow コマンドに変更。シェルスクリプトを cfn としてコマンド化した後にタイプミスが多発したため、git の頭文字と now を組み合わせた
* 2020-07-09 リポジトリ名 commit-for-now, cfn コマンドとして Github 公開
