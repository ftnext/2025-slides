======================================================================
2025年のPython環境はここまで簡単になりました！
======================================================================

環境構築ツールパビリオン クイックツアー

2025/09/06 大吉祥寺.pm LT nikkie

2025年、大阪・関西万博の年
======================================================================

`プロポーザルのテーマ「2025年の今、みんなに聞いてほしいこと」 <https://x.com/kichijojipm/status/1932238845694849063>`__

この5分だけ **ここは万博** です
--------------------------------------------------

.. うわ〜！大屋根リングだ〜

Python環境構築パビリオン🏛️
======================================================================

.. Python環境構築パビリオンがある。入ってみるか、ウィーン

本パビリオンは、Python環境の **パラダイムシフト** を展示しています
----------------------------------------------------------------------

前説：Pythonとライブラリ
======================================================================

Web開発・機械学習・自動化などなど、便利なライブラリが `PyPI <https://pypi.org/>`__ にたくさん公開されているのですが...

ライブラリはどこにインストールされるか
--------------------------------------------------

* PyPI から pip でインストール（:command:`python -m pip install openai`）
* **グローバルに1箇所** （:file:`site-package`）
* 1つのPython処理系に、同じライブラリのバージョン違いが共存できない

仮想環境 というディレクトリ
--------------------------------------------------

* 💡 :file:`site-package` を **ディレクトリごとに作る**
* pnpmの :file:`node_modules` やcomposerの :file:`vendor`
* ライブラリのバージョン違いを可能にする

仮想環境 **人力** 管理の時代💪
======================================================================

.. code-block:: shell

    $ python -m venv .venv --upgrade-deps  # 1
    $ source .venv/bin/activate  # 2
    (.venv) $ python -m pip install openai  # 3

私が7-8年前に入門したときの方法
--------------------------------------------------

1. 仮想環境を作る：標準ライブラリの `venv <https://docs.python.org/ja/3/library/venv.html>`__
2. 仮想環境を有効にする：俺たち！（人力）
3. 依存ライブラリをインストール： `pip <https://pip.pypa.io/en/stable/>`__

`Pythonチュートリアル <https://docs.python.org/ja/3/tutorial/venv.html>`__

.. ツールも提案されてきた

2024年 uv到来
======================================================================

* Rust で書かれた Python プロジェクト管理ツール
* 開発者が人力で仮想環境管理からの **解放** （パラダイムシフト！）

uv のインストール
--------------------------------------------------

.. code-block:: shell

    $ curl -LsSf https://astral.sh/uv/install.sh | sh
    $ brew install uv
    $ # などなど (cargo)

https://docs.astral.sh/uv/getting-started/installation/

展示1️⃣ 手札は、全PyPI！
======================================================================

* インストールすることで **コマンドラインツールとしても使えるライブラリ** がある
* 例えば、 `openai <https://pypi.org/project/openai/>`__

これまで：人力で仮想環境にインストールして使ってきた
------------------------------------------------------------

.. code-block:: shell

    $ python -m venv openai-env --upgrade-deps
    $ source openai-env/bin/activate
    (openai-env) $ python -m pip install openai
    (openai-env) $ openai api chat.completions.create -g user 'Python環境構築ツールパビリオンを訪れた感想は？' -m gpt-5

.. 先行ツールとして ``pipx run`` もある

🆕 :command:`uvx`
--------------------------------------------------

* ``uv tool run`` のエイリアス
* uvが **一時的な仮想環境を作り**、そこにインストールしてコマンドラインツールを実行
* PyPIにある全てのコマンドラインツールが、仮想環境の人力管理無しで使えるってこと！

展示2️⃣ inline script metadata
======================================================================

ライブラリを使ったスクリプトを書く（シェルスクリプト代わりに）

.. code-block:: python

    import httpx  # HTTPクライアント
    from rich.pretty import pprint  # きれいな出力

    resp = httpx.get("https://peps.python.org/api/peps.json")
    data = resp.json()
    pprint([(k, v["title"]) for k, v in data.items()][:10])

これまで：人力で仮想環境を用意していた
--------------------------------------------------

.. code-block:: shell

    $ python -m venv script-env --upgrade-deps
    $ source script-env/bin/activate
    (script-env) $ python -m pip install httpx rich
    (script-env) $ python script.py

🆕 `PEP 723 – Inline script metadata <https://peps.python.org/pep-0723/>`__
----------------------------------------------------------------------------------------------------

* Pythonスクリプトにコメントとして **依存ライブラリを示すメタデータ** を書けるようになった
* :command:`uv add httpx rich --script script.py`

.. code-block:: python

    # /// script
    # requires-python = ">=3.11"
    # dependencies = [
    #     "httpx",
    #     "rich",
    # ]
    # ///

:command:`uv run` script.py
--------------------------------------------------

1. uvがmetadataを読む
2. uvが **metadataを満たす仮想環境を用意**
3. uvが2の仮想環境でスクリプトを実行

.. さらに進んだ例 marimo

.. ブログ書きました https://tech.uzabase.com/entry/2024/06/07/180442

展示3️⃣ uvで楽々Pythonプロジェクト管理
======================================================================

uvで管理されたPythonプロジェクトであれば :command:`uv sync` だけ！

.. uv.lock

これまで：環境構築
--------------------------------------------------

git clone してから

.. code-block:: shell

    $ python -m venv .venv --upgrade-deps
    $ source .venv/bin/activate
    (.venv) $ python -m pip install -e .

🆕 :command:`uv sync` だけで環境構築完了
--------------------------------------------------

* uvが仮想環境 :file:`.venv` を作る
* そこに依存ライブラリをインストール
* Rust実装（バイナリ提供）なので、Python処理系で動かすpipより速い

:command:`uv run` <command>
--------------------------------------------------

* ``uv run`` で 仮想環境 :file:`.venv` を有効にしたうえでコマンド実行
* 人力で有効化は不要

.. code-block:: shell

    $ uv run which python

uvでPythonプロジェクトを始める
--------------------------------------------------

新規プロジェクトにおいては

* uv init
* uv add (uv remove)

.. uvで管理していないPythonプロジェクト

まとめ🌯：Python環境のパラダイムシフト
======================================================================

* 仮想環境を簡単に管理するツールが登場。uvを紹介
* :command:`uvx` ・ :command:`uv run <script.py または コマンド>`
* 私が7-8年前に入門したときの標準、人力管理は、もはや全人類経験しなくていいんです！！

uvで Python環境 自由✌️（ぶい）
======================================================================

ご清聴ありがとうございました

Happy Python Life!
