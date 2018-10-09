# bib2ref

<<<<<<< HEAD
bibファイルからスライドに貼る参考文献を作るのが面倒だったので作りました。
=======
bibファイルから文書やスライドに載せる参考文献を作るのが面倒だったので自動生成するようにしました。
>>>>>>> a01501b570cf775df3850e18a3b6773602f061b4

## template  
    bibdeskのテンプレートです。txt形式とMarkdown形式の２種類あります。

### 使い方

    1. Bibdesk -> Preferences -> Templates
    1. 画面右下の+ボタンを押してテンプレートを登録
    1. 引用したい論文を右クリック -> Copy Using Template -> bib2***

### 消し方
    Bibdesk -> Preferences -> Templates -> Reset All

## bibparse
最初のアプローチです。bibdeskにいい機能があったので途中放棄。

### 使い方
1. フォルダ内に.bibを置く
2. make
3. pdfが表示されるので必要なところをコピー

### 動作環境

- only for OS X
- Python 3
- Texlive 2018
<<<<<<< HEAD

'''pip install bibtexparser'''
=======
>>>>>>> a01501b570cf775df3850e18a3b6773602f061b4
