======================================================================
Rustで作るPythonパッケージの例 sampleproject-rs の紹介
======================================================================

Rustで作るPythonパッケージの例 **sampleproject-rs** の紹介
======================================================================

:Event: Pythonの多様性 深掘りLT Night
:Presented: 2025/10/22 nikkie

お前、誰よ？
======================================================================

* nikkie（にっきー） :fab:`twitter` :fab:`github` @ftnext 
* PyCon JP 2025 では `標準ライブラリloggingの話 <https://2025.pycon.jp/en/timetable/talk/Z8ZYFA>`__ をしました
* 機械学習エンジニア。 `Speeda AI Agent <https://www.uzabase.com/jp/info/20250901/>`__ 開発（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）

.. image:: ../_static/uzabase-white-logo.png

Rustで書かれたPythonパッケージを **作れる** ようになりたい
======================================================================

:uv, Ruff: RustをバイナリにしてPyPIで配布
:Pydantic: Rustで書いたコードをPythonから呼び出せる

目標に近づくために sampleproject-rs で素振り💪
------------------------------------------------------------

https://pypi.org/project/sampleproject-rs/

sampleproject、知っている方？🙋
======================================================================

https://pypi.org/project/sampleproject/

☝️ :command:`uvx --from sampleproject sample`
------------------------------------------------------------

.. code-block:: console

    % uvx --from sampleproject sample
    Call your main application code here

✌️ ``sample.simple.add_one()``
------------------------------------------------------------

.. code-block:: console

    % uv run --with sampleproject \
        python -c "from sample import simple; print(simple.add_one(1))"
    2

Python **パッケージのサンプル**
------------------------------------------------------------

* PyPA（Python Packaging Authority）が作ってます：https://github.com/pypa/sampleproject/
* チュートリアル `Packaging Python Projects <https://packaging.python.org/en/latest/tutorials/packaging-projects/>`__
* Pythonパッケージを作りたい方におすすめ

私のsampleproject-rs
======================================================================

sampleprojectにインスパイアされ、爆誕させた

☝️ :command:`uvx --from sampleproject-rs sample`
------------------------------------------------------------

.. code-block:: console

    % uvx --from sampleproject-rs sample
    Call your main application code here

✌️ ``sample.simple.add_one()``
------------------------------------------------------------

.. code-block:: console

    % uv run --with sampleproject-rs \
        python -c "from sample import simple; print(simple.add_one(1))"
    2

**Rust実装** で完全再現です！！
------------------------------------------------------------

https://github.com/ftnext/sampleproject-rs

.. code-block:: rust

    fn main() {
        println!("Call your main application code here");
    }

    #[pyfunction]
    fn add_one(number: i32) -> i32 {
        number + 1
    }

sampleproject-rs からの学び
======================================================================

* *maturin*
* *PyO3*

1️⃣ :command:`maturin build` でPythonパッケージになる
------------------------------------------------------------

* maturinは、Rustで書かれたビルドバックエンド

.. code-block:: toml
    :caption: :file:`pyproject.toml`

    [build-system]
    requires = ["maturin>=1.8,<2.0"]
    build-backend = "maturin"

    [tool.maturin]
    bindings = "bin"  # バイナリの指定
    strip = true

.. 参考
    https://www.maturin.rs/tutorial
    https://nikkie-ftnext.hatenablog.com/entry/maturin-bindings-bin-python-package-from-rust-binary

Python製パッケージと違って **環境ごとのビルド** が必要
------------------------------------------------------------

.. https://nikkie-ftnext.hatenablog.com/entry/try-maturin-pypi-upload-confuse-binary-each-environment

* GitHub Actions（Ubuntu環境）で ``maturin build`` してPyPIに上げたら、**macOSでは実行できず**

.. code-block:: console

    % uvx --from sampleproject-rs sample
    × No solution found when resolving tool dependencies:
    ╰─▶ Because only sampleproject-rs==0.0.1 is available and
        sampleproject-rs==0.0.1 has no wheels with a matching platform tag
        (e.g., `macosx_14_0_arm64`), we can conclude that all versions of
        sampleproject-rs cannot be used.

2️⃣ **PyO3** でRustプログラムをPythonから呼び出せるようにした
----------------------------------------------------------------------

.. code-block:: rust

    use pyo3::prelude::*;

    #[pyfunction]
    fn add_one(number: i32) -> i32 {
        number + 1
    }

    #[pymodule]
    mod sample {
        use super::*;

        #[pymodule]
        mod simple {
            #[pymodule_export]
            use super::add_one;
        }
    }

合わせて ``sample`` コマンドはPythonスクリプトに変更
------------------------------------------------------------

.. https://nikkie-ftnext.hatenablog.com/entry/rust-maturin-cli-and-import-support-python-library

.. code-block:: toml
    :caption: :file:`pyproject.toml`

    [project.scripts]
    sample = "sample:main"

    [tool.maturin]
    bindings = "pyo3"  # "bin"から変更

まとめ🌯：Rustで作るPythonパッケージの例 sampleproject-rs の紹介
======================================================================

Rustで書いたプログラムは

* **maturin** でバイナリとしてPyPIから配布できる
* **PyO3** でPythonプログラム中で呼び出せる

ご清聴ありがとうございました
--------------------------------------------------

.. https://ftnext.github.io/2025-slides/python-fukuoka/why-we-can-run-rust-package-cli#/1
