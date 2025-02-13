:ogp_title: Pythonの組み込み例外の小話
:ogp_event_name: stapy-lt
:ogp_slide_name: february-repr-exception
:ogp_description: みんなのPython勉強会#112
:ogp_image_name: stapy-lt-february

======================================================================
Pythonの組み込み例外の小話
======================================================================

:Event: みんなのPython勉強会#112
:Presented: 2025/02/13 nikkie

お前、誰よ
======================================================================

* nikkie ／ みんなのPython勉強会 スタッフ・4代目LT王子
* 機械学習エンジニア・LLM・自然言語処理（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）
* `ブログ <https://nikkie-ftnext.hatenablog.com/>`__ 連続 **810** 日突破

.. image:: ../_static/uzabase-white-logo.png

Pythonの **組み込み例外** の小話
--------------------------------------------------

毎日書いてるブログ記事からご紹介

例外を出力するように実装
======================================================================

.. code-block:: python

    try:
        外部との通信処理()
    except Exception as ex:
        print(f"エラー発生: {ex}")

どのような具体の例外が送出されるか不明なので様子を見ていた

よっしゃ、どんなエラーか知るぞ！
--------------------------------------------------

.. code-block:: txt

    エラー発生: 

* エラーの情報が分からない😱
* 俺みたいになるな！というLTです

📌 ``{ex!r}`` にしています
--------------------------------------------------

.. code-block:: python
    :emphasize-lines: 4

    try:
        外部との通信処理()
    except Exception as ex:
        print(f"エラー発生: {ex!r}")

例外におすすめ！

``{ex!r}`` とはなにか
======================================================================

* **変換** （Conversion）なるもの（`2.4.3. f-strings <https://docs.python.org/ja/3/reference/lexical_analysis.html#formatted-string-literals>`__）

    変換 ``'!s'`` は ``str()`` を、 ``'!r'`` は ``repr()`` を、(略) 呼び出します。

* 変換を書かないときは ``!s``

返す文字列には違いがある
--------------------------------------------------

:``str()``: 人間が読める表現
:``repr()``: **Python処理系** が読める表現

参考 `7.1. 出力を見やすくフォーマットする <https://docs.python.org/ja/3/tutorial/inputoutput.html#fancier-output-formatting>`__

引数を渡さない例外とf-strings
--------------------------------------------------

.. code-block:: pycon

    >>> ex = Exception()
    >>> print(f"{ex}")
    <BLANKLINE>
    >>> print(f"{ex!r}")
    Exception()

.. _BaseException: https://docs.python.org/ja/3/library/exceptions.html#BaseException

基底クラス `BaseException`_
--------------------------------------------------

    このクラスのインスタンスに ``str()`` が呼ばれた場合、インスタンスへの引数の表現か、 **引数が無い場合には空文字列** が返されます。

（強調は引用者による）

HTTPクライアント HTTPX にて
--------------------------------------------------

.. code-block:: python
    :caption: https://github.com/encode/httpx/blob/0.28.1/httpx/_exceptions.py#L146

    class ReadTimeout(TimeoutException):
        """
        Timed out while receiving data from the host.
        """

参考： ``ReadTimeout`` の継承関係
--------------------------------------------------

.. code-block:: txt
    :caption: https://github.com/encode/httpx/blob/0.28.1/httpx/_exceptions.py#L4-L9

    * HTTPError
      x RequestError
        + TransportError
          - TimeoutException
            · ReadTimeout

元のブログ記事
--------------------------------------------------

`Pythonで例外を文字列中に出力するときは、str()ではなくてrepr()に渡すのがオススメです <https://nikkie-ftnext.hatenablog.com/entry/python-exception-with-repr-recommendation>`__

まとめ🌯 f-stringsでは ``{ex!r}``
======================================================================

* ``try ... except`` で例外を捕捉し出力するような場合
* 例外は引数がないと ``f"{ex}"`` すなわち ``str()`` は空文字列
* ``f"{ex!r}"`` で ``repr()`` を呼び出すことで、 **引数がない例外でもクラス名が表示される**

One more 小話： ``except Exception:``
--------------------------------------------------

`Pythonで例外を捕捉するときに、except:やexcept BaseException:と書いてはいけません。except Exception:またはもっと具体な例外クラスを指定しましょう <https://nikkie-ftnext.hatenablog.com/entry/python-except-specify-exception-or-more-concrete-one>`__

その2までLTには盛り込めませんでした🙏

ご清聴ありがとうございました
--------------------------------------------------

Happy `ショコラブル＊イブ <https://youtu.be/jrXRStmE-to?si=Ihjnf6PwXc8g5bT2>`__ 🍫🔵
