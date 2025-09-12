================================================================================
Rust製パッケージをインストールしてコマンドラインから実行できるのは、なぜ？
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

* Python製パッケージの場合（例：`sampleproject <https://pypi.org/project/sampleproject/>`__）
* Rust製パッケージの場合（例：`Ruff <https://pypi.org/project/ruff/>`__）

**Python** 製パッケージをインストールしてコマンドラインから実行できるのは、なぜ？
==========================================================================================

.. code-block:: shell

    $ python -m venv .venv --upgrade-deps  # Python 3.13.0
    $ source .venv/bin/activate
    (.venv) $ python -m pip install sampleproject
    (.venv) $ .venv/bin/sample  # /usr/bin/sample と区別
    Call your main application code here

metadata の project.scripts
--------------------------------------------------

.. code-block:: toml
    :caption: `sampleproject の pyproject.toml 抜粋 <https://github.com/pypa/sampleproject/blob/621e4974ca25ce531773def586ba3ed8e736b3fc/pyproject.toml#L151-L154>`__

    [project.scripts]
    sample = "sample:main"

仮想環境下にスクリプト
--------------------------------------------------

.. code-block:: shell

    $ ls -l .venv/bin/sample
    -rwxr-xr-x  1 user  group  211 Sep 12 11:23 .venv/bin/sample
    $ file .venv/bin/sample
    .venv/bin/sample: a /.../.venv/bin/python script text executable, ASCII text

「エントリポイントスクリプト」（『ハイパーモダンPython』）

.. 仮想環境は有効化でPATHに入る

エントリポイントスクリプトの中身
--------------------------------------------------

.. literalinclude:: sample-command
    :language: python

シバンにPythonのパス
--------------------------------------------------

.. literalinclude:: sample-command
    :language: python
    :lines: 1

* **Python処理系で実行**！

.. distlibによる

🥟Python製パッケージをインストールしてコマンドラインから実行できるのは、なぜ？
================================================================================

* インストールでテキストファイル（**Pythonスクリプト**）が置かれる
* シバンにより、Python処理系で実行される

**Rust** 製パッケージをインストールしてコマンドラインから実行できるのは、なぜ？
================================================================================

.. code-block:: shell

    $ python -m venv .venv --upgrade-deps
    $ source .venv/bin/activate
    (.venv) $ python -m pip install ruff
    (.venv) $ ruff check --fix --extend-select I

仮想環境下にバイナリ
--------------------------------------------------

.. code-block:: shell

    $ ls -lh .venv/bin/ruff
    -rwxr-xr-x  1 user  group    30M Sep 12 11:30 .venv/bin/ruff
    $ file .venv/bin/ruff
    .venv/bin/ruff: Mach-O 64-bit executable arm64

🔑maturin
======================================================================

* https://www.maturin.rs/#maturin
* **Rustバイナリ** はもちろん、pyo3などバインディングを使ったクレートをPythonパッケージとしてビルド・公開できるツール

Rust版 sampleproject
--------------------------------------------------

.. code-block:: rust
    :caption: :file:`src/main.rs`

    fn main() {
        println!("Call your main application code here");
    }

.. code-block:: shell

    $ cargo run --quiet
    Call your main application code here

:file:`pyproject.toml` 追加
--------------------------------------------------

.. code-block:: toml
    :caption: 完全版 `pyproject.toml <https://github.com/ftnext/sampleproject-rs/blob/0.0.2/pyproject.toml>`__

    [build-system]
    requires = ["maturin>=1.8,<2.0"]
    build-backend = "maturin"

    [tool.maturin]
    bindings = "bin"
    strip = true

ローカルでインストールして実行
--------------------------------------------------

.. code-block:: shell

    (.venv) $ uvx maturin build
    (.venv) $ python -m pip install target/wheels/sampleproject_rs-0.0.2-py3-none-macosx_11_0_arm64.whl
    (.venv) $ .venv/bin/sample
    Call your main application code here

別案：``maturin develop`` なら `.venv/bin/sample` のインストールまで

PyPIにも公開
--------------------------------------------------

https://pypi.org/project/sampleproject-rs/

.. code-block:: shell
    :caption: GitHub Codespaces にて

    $ pipx run --spec sampleproject-rs sample
    Call your main application code here

macOS向けなどのバイナリは今後対応予定

bindings = "bin" (:file:`pyproject.toml`)
--------------------------------------------------

    Maturin also supports distributing binary applications written in Rust as Python packages using the ``bin`` bindings.

https://www.maturin.rs/bindings#bin

Ruffの :file:`pyproject.toml`
--------------------------------------------------

.. code-block:: toml
    :emphasize-lines: 2

    [tool.maturin]
    bindings = "bin"
    manifest-path = "crates/ruff/Cargo.toml"
    module-name = "ruff"
    python-source = "python"
    strip = true
    exclude = [
        "crates/ruff_linter/resources/test/fixtures/**/*",
        "crates/ruff_linter/src/rules/*/snapshots/**/*"
    ]

https://github.com/astral-sh/ruff/blob/0.13.0/pyproject.toml#L46-L55

🌯Rust製パッケージをインストールしてコマンドラインから実行できるのは、なぜ？
================================================================================

* テキストファイルではなく、バイナリが置かれる
* ビルドバックエンドに maturin を使うと、**Rustで作ったバイナリがPythonパッケージになる**

ご清聴ありがとうございました
--------------------------------------------------
