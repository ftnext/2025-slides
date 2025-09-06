======================================================================
2025年のPython環境はここまで **簡単** になりました！
======================================================================

環境構築ツールパビリオン クイックツアー

2025/09/06 大吉祥寺.pm LT nikkie

「2025年の今、みんなに聞いてほしいこと」（`プロポーザルのテーマ <https://x.com/kichijojipm/status/1932238845694849063>`__）
============================================================================================================================================

* 2025年時点のPython環境が著しく簡単になっていることを全力で伝えます（`プロポーザル <https://fortee.jp/dai-kichijojipm-2025/proposal/a9a04d16-766c-4b65-9206-bf4200a136b8>`__）
* 2025年は **大阪・関西万博** の年です

この5分だけ **ここは万博** です
--------------------------------------------------

「うわ〜！大屋根リングだ〜〜」

Python環境構築パビリオン🏛️
======================================================================

.. https://dic.pixiv.net/a/%E8%88%88%E5%A5%AE%E3%81%97%E3%81%A6%E3%81%8D%E3%81%9F%E3%81%AA

「興奮してきたな。入ってみよう。ウィーン」

本パビリオンは、Python環境の **パラダイムシフト** を展示しています
----------------------------------------------------------------------

* 前説
* uvを使った3つの展示

前説：Pythonとライブラリ
======================================================================

Web開発・機械学習・自動化などなど、便利なライブラリが `PyPI <https://pypi.org/>`__ にたくさん公開されているPythonなのですが...

ライブラリはどこにインストールされるか
--------------------------------------------------

* インストール先は **グローバルに1箇所** （:file:`site-package`）
* 1つのPython処理系に、同じライブラリのバージョン違いが共存できない

仮想環境 という **ディレクトリ**
--------------------------------------------------

* 💡ライブラリのインストール先（:file:`site-package`）を都度作る
* pnpmの :file:`node_modules` やcomposerの :file:`vendor` に相当
* ライブラリの **バージョン違いを可能に** する

仮想環境 **人力** 管理の時代💪
======================================================================

.. code-block:: shell

    $ python -m venv .venv --upgrade-deps  # 1
    $ source .venv/bin/activate  # 2
    (.venv) $ python -m pip install openai  # 3

私が7-8年前に入門したときの方法（`Pythonチュートリアル <https://docs.python.org/ja/3/tutorial/venv.html>`__）

1. 仮想環境 :file:`.venv` ディレクトリを作る
--------------------------------------------------

**Python処理系は前提** で、標準ライブラリの `venv <https://docs.python.org/ja/3/library/venv.html>`__ 使用

.. code-block:: shell
    :emphasize-lines: 1

    $ python -m venv .venv --upgrade-deps  # 1
    $ source .venv/bin/activate  # 2
    (.venv) $ python -m pip install openai  # 3

2. 1でできたシェルスクリプトを **俺たちが毎回叩く**！（人力）
----------------------------------------------------------------------

環境変数 ``PATH`` の更新など：「仮想環境を有効化」

.. code-block:: shell
    :emphasize-lines: 2

    $ python -m venv .venv --upgrade-deps  # 1
    $ source .venv/bin/activate  # 2
    (.venv) $ python -m pip install openai  # 3

3. 依存ライブラリを仮想環境にインストール
--------------------------------------------------

標準のインストーラ `pip <https://pip.pypa.io/en/stable/>`__

.. code-block:: shell
    :emphasize-lines: 3

    $ python -m venv .venv --upgrade-deps  # 1
    $ source .venv/bin/activate  # 2
    (.venv) $ python -m pip install openai  # 3

（ツール提案の流れの末に）2024年 uv 到来
======================================================================

* Rustで書かれた、Pythonプロジェクト管理ツール（集大成的）
* uvだけ入れればよい（Pythonを自動で入れる）
* 開発者が **人力で仮想環境管理からの解放** （パラダイムシフト！）

uvのインストール
--------------------------------------------------

.. code-block:: shell

    $ curl -LsSf https://astral.sh/uv/install.sh | sh
    $ brew install uv
    $ # cargo などなど

https://docs.astral.sh/uv/getting-started/installation/

展示1️⃣ 手札は、全PyPI！
======================================================================

* インストールすることで **コマンドラインツールとしても使えるライブラリ** がある

.. code-block:: bash

    % uvx openai api chat.completions.create -g user 'Python環境構築ツールパビリオンを訪れた感想は？' -m gpt-5
    Installed 16 packages in 29ms
    実地で訪れたわけではないので体験談は語れませんが、「Python 環境構築ツール」をテーマにしたパビリオンだと想定すると、こんな点が印象に残りそうです。

.. docker run --rm -it debian:bullseye bash
    apt update && apt install -y curl
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.local/bin/env
    uvx openai -h

これまで：人力で仮想環境を用意してそこにインストールしてきた
------------------------------------------------------------

.. code-block:: shell

    $ python -m venv openai-env --upgrade-deps
    $ source openai-env/bin/activate
    (openai-env) $ python -m pip install openai
    (openai-env) $ openai api chat.completions.create -g user 'Python環境構築ツールパビリオンを訪れた感想は？' -m gpt-5

.. 先行ツールとして ``pipx run`` もある

🆕 :command:`uvx`
--------------------------------------------------

* uvをインストールしたら使えます（`uv tool run <https://docs.astral.sh/uv/reference/cli/#uv-tool-run>`__ のエイリアス）
* uvが **一時的な仮想環境を作り**、そこにインストールしてコマンドラインツールを実行
* PyPIにある全てのコマンドラインツール（最大60万）が、仮想環境の人力管理無しで使い放題ってこと！

展示2️⃣ inline script metadata
======================================================================

.. literalinclude:: ../../samplecode/python-pavilion/script.py
    :language: python
    :lines: 11,17-19
    :caption: ライブラリを使ったスクリプト

.. code-block:: shell

    % uv run script.py 'Python環境構築ツールパビリオンを訪れた感想は？'
    Installed 16 packages in 35ms
    実際に会場へ行くことはできませんが、最近の動向を踏まえて「Python環境構築ツールが一堂に会したらこう感じる」という要約です。

これまで：依存ライブラリをインストールした仮想環境を人力で用意
----------------------------------------------------------------------

.. code-block:: shell

    $ python -m venv script-env --upgrade-deps
    $ source script-env/bin/activate
    (script-env) $ python -m pip install openai  # ここの伝達が人頼み
    (script-env) $ python script.py

🆕 `PEP 723 – Inline script metadata <https://peps.python.org/pep-0723/>`__
----------------------------------------------------------------------------------------------------

* Pythonスクリプトにコメントとして **依存ライブラリを示すメタデータ** を書けるようになった
* :command:`uv add openai --script script.py`

.. literalinclude:: ../../samplecode/python-pavilion/script.py
    :language: python
    :lines: 1-6

:command:`uv run` <metadata書いたscript>.py
--------------------------------------------------

1. uvがmetadataを読む
2. uvが **metadataを満たす仮想環境を用意**
3. uvが2の仮想環境でスクリプトを実行

metadataを書いたスクリプトは、別環境でもはるかに動かしやすくなったってこと！

.. さらに進んだ例 marimo

.. ブログ書きました https://tech.uzabase.com/entry/2024/06/07/180442

展示3️⃣ uvで楽々Pythonプロジェクト管理
======================================================================

uvで管理されたPythonプロジェクトであれば :command:`uv sync` だけ！

.. code-block:: shell
    :emphasize-lines: 3

    $ git clone https://github.com/ftnext/llm-deep-research.git
    $ cd llm-deep-research
    $ uv sync

これまで：人力で仮想環境にインストールして環境構築
--------------------------------------------------

.. code-block:: shell
    :emphasize-lines: 3-5

    $ git clone https://github.com/ftnext/llm-deep-research.git
    $ cd llm-deep-research
    $ python -m venv .venv --upgrade-deps
    $ source .venv/bin/activate
    (.venv) $ python -m pip install -e .

🆕 たった1つの :command:`uv sync` だけ
--------------------------------------------------

* uvが仮想環境 :file:`.venv` を作る
* そこに :file:`uv.lock` の通りに依存ライブラリをインストール

あとは :command:`uv run` <command> 連打
--------------------------------------------------

* ``uv run`` で 仮想環境 :file:`.venv` を有効にしたうえでコマンド実行
* 人力で有効化（``source .venv/bin/activate``）は不要

.. code-block:: shell

    $ uv run which python
    /.../llm-deep-research/.venv/bin/python

uvでPythonプロジェクトを始める
--------------------------------------------------

新規プロジェクトにおいては

* `uv init <https://docs.astral.sh/uv/reference/cli/#uv-init>`__
* `uv add <https://docs.astral.sh/uv/reference/cli/#uv-add>`__ (uv remove)

.. uvで管理していないPythonプロジェクト

まとめ🌯：2025年のPython環境はここまで簡単になりました！
======================================================================

* 手札は、全PyPI！ :command:`uvx`
* inline script metadata :command:`uv run` <metadata書いたscript>.py
* Pythonプロジェクトでは :command:`uv sync` して :command:`uv run` <command>

お前、誰だったのよ？
--------------------------------------------------

* nikkie（にっきー）・ **1000日** `ブログ <https://nikkie-ftnext.hatenablog.com/>`__ を書きました！（更新中）
* 機械学習エンジニア・LLM・自然言語処理（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）
* `Speeda AI Agent <https://www.uzabase.com/jp/info/20250630/>`__ 開発

.. image:: ../_static/uzabase-white-logo.png

uvで Python環境 自由✌️（ぶい）
======================================================================

ご清聴ありがとうございました

📣「"仮想環境"を人間が管理する時代は、もう終わりました。ツールに任せて楽してこーぜ！」

.. TODO 本LTのスコープ外

.. uvはRust実装（バイナリ提供）なので、Python処理系で動かすpipより速い
