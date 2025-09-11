================================================================================
Rust製パッケージをインストールしてコマンドラインから実行できるのは、なぜ？
================================================================================

:Event: Python Meetup Fukuoka #4
:Presented: 2025/09/12 nikkie

このLTは、以下ができる理由を自分の言葉で説明するものです
======================================================================

.. code-block:: shell

    $ python -m venv .venv --upgrade-deps
    $ source .venv/bin/activate
    (.venv) $ python -m pip install ruff
    (.venv) $ ruff check --fix --extend-select I

本LTのスコープ（パッケージの場合分け）
--------------------------------------------------

* Python製パッケージの場合（例：openai）
* Rust製パッケージの場合（例：Ruff）

Python製パッケージをインストールしてコマンドラインから実行できるのは、なぜ？
================================================================================

.. code-block:: shell

    $ python -m venv .venv --upgrade-deps
    $ source .venv/bin/activate
    (.venv) $ python -m pip install openai
    (.venv) $ openai api chat.completions.create -g user 'Python使いに向けて博多弁でご挨拶して' -m gpt-5

metadata の project.scripts
--------------------------------------------------

.. GitHubから

仮想環境下にスクリプト
--------------------------------------------------

.. ls -l .venv/bin/openai

.. 『ハイパーモダンPython』での呼び名 エントリポイントスクリプト

.. 仮想環境は有効化でPATHに入る

スクリプトの中身
--------------------------------------------------


シバンにPythonのパス
--------------------------------------------------

.. distlibによる

Python製パッケージをインストールしてコマンドラインから実行できるのは、なぜ？
================================================================================

* テキストファイルが置かれる
* シバンにより、Python処理系で実行される

Rust製パッケージをインストールしてコマンドラインから実行できるのは、なぜ？
================================================================================

.. code-block:: shell

    $ python -m venv .venv --upgrade-deps
    $ source .venv/bin/activate
    (.venv) $ python -m pip install ruff
    (.venv) $ ruff check --fix --extend-select I

仮想環境下にバイナリ
--------------------------------------------------

.. ls -l .venv/bin/ruff

🔑maturin
======================================================================

練習で作ったRust製CLI ``repeatrs``
--------------------------------------------------

.. code-block:: shell

    % cargo run --quiet -- position エミリー 5
    エミリーエミリーエミリーエミリーエミリー
    % cargo run --quiet -- option -s 大好き   
    大好き大好き大好き

:file:`pyproject.toml` 追加
--------------------------------------------------

.. projectは端折る？

.. code-block:: toml

    [build-system]
    requires = ["maturin>=1.8,<2.0"]
    build-backend = "maturin"

    [project]
    name = "repeatrs"
    version = "0.1.0"
    requires-python = ">=3.9"

    [tool.maturin]
    bindings = "bin"
    strip = true

ローカルでインストールして実行
--------------------------------------------------

maturin build して ローカルの仮想環境に wheel をインストール

.. PyPI版？

bindings = "bin" (:file:`pyproject.toml`)
--------------------------------------------------

.. https://www.maturin.rs/bindings

Rust製パッケージをインストールしてコマンドラインから実行できるのは、なぜ？
================================================================================

* テキストファイルではなく、バイナリが置かれる
* ビルドバックエンドに maturin を使うと、Rustで作ったバイナリがPythonパッケージになる

.. ruffやuvのpyproject.toml
