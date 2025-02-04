:ogp_title: ライブラリ開発者に贈る「ロギングで NullHandler 以外はいけません」
:ogp_event_name: pyconshizu
:ogp_slide_name: logging-with-nullhandler
:ogp_description: PyCon mini Shizuoka 2024 continue
:ogp_image_name: pyconshizu

.. _ライブラリのためのロギングの設定: https://docs.python.org/ja/3/howto/logging.html#configuring-logging-for-a-library
.. _ライブラリ内でロガーに NullHandler 以外のハンドラーを追加する: https://docs.python.org/ja/3/howto/logging-cookbook.html#adding-handlers-other-than-nullhandler-to-a-logger-in-a-library
.. _Logger.setLevel: https://docs.python.org/ja/3/library/logging.html#logging.Logger.setLevel

======================================================================
ライブラリ開発者に贈る「ロギングで ``NullHandler`` 以外はいけません」
======================================================================

ライブラリ開発者に贈る「ロギングで ``NullHandler`` 以外はいけません」
======================================================================

:Event: PyCon mini Shizuoka 2024 continue
:Presented: 2025/02/08 nikkie

お前、誰よ
======================================================================

* nikkie ／ :fab:`github` `@ftnext <https://github.com/ftnext>`__ ／ `ブログ <https://nikkie-ftnext.hatenablog.com/>`__ 連続 **810** 日突破
* 機械学習エンジニア・自然言語処理（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）
* Python歴は7年。PyConで登壇多数

.. image:: ../_static/uzabase-white-logo.png

アンケート（何度でも挙げよう）
--------------------------------------------------

* ``logging.warning()`` や ``logging.error()`` したことある🙋‍♂️
* ``logging.basicConfig()`` したことある🙋‍♀️
* ``logging.getLogger()`` したことある🙋

本トークの対象者
--------------------------------------------------

* Pythonのloggingモジュール **触ったことがある**
* loggingモジュールの中身はよく分からなくて全然OK👌

皆さんに質問です
======================================================================

* あなたはPythonで ``import`` して使いたいコードを書いています（例：ライブラリ）
* その中で **ロギング** 、どう実装しますか？

結論：「``NullHandler`` 以外はいけません」
--------------------------------------------------

.. literalinclude:: ../../samplecode/python-logging/conclusion.py
    :language: python
    :lines: 1-4

公式ドキュメント📄「`ライブラリのためのロギングの設定`_」

すべて公式 **ドキュメント** に書いてあります！
--------------------------------------------------

* しかし、観測範囲ではPython使いに気づかれていない印象...😫
* 📄の付いたリンクは、公式ドキュメントへのリンク
* （別のemoji：🏃‍♂️は本編では飛ばします）

本トークのメッセージ（Takeaway）
--------------------------------------------------

* ライブラリ開発者は *ロガー* を用意し、 *何もしないハンドラ* を設定しよう
* アプリケーション開発者は *ルートロガー* を設定し、 *propagate* を利用してログを表示しよう

斜体はこのトークで解説します

ライブラリではオススメしません（ぶっぶー🙅‍♂️） 🏃‍♂️
--------------------------------------------------

.. code-block:: python

    logging.basicConfig()

.. code-block:: python

    logging.warning()

.. code-block:: python
    :emphasize-lines: 2

    logger = logging.getLogger("mylib")
    logger.addHandler(logging.StreamHandler())

Logging クックブックの「避けるべきパターン」の1つ
======================================================================

* `ライブラリ内でロガーに NullHandler 以外のハンドラーを追加する`_ 📄

    (略) ログ出力をカスタマイズするのはライブラリ開発者ではなく、アプリケーション開発者の責務です。

本トークの構成
--------------------------------------------------

1. ライブラリ開発者へ
2. アプリケーション開発者へ
3. 落ち穂拾い

.. include:: library-logging.rst.txt

.. include:: application-logging.rst.txt

.. include:: gleanings.rst.txt

まとめ🌯 ライブラリ開発者に贈る「ロギングで ``NullHandler`` 以外はいけません」
================================================================================

.. revealjs-break::
    :notitle:

.. literalinclude:: ../../samplecode/python-logging/conclusion.py
    :language: python
    :lines: 1-4

📣ライブラリのユーザが自由にロギングをカスタマイズできるようにしよう

* そのための ``NullHandler``
* propagateを使って、 **ユーザが設定するルートロガーのハンドラでログ出力**

メッセージ（Takeaway）再掲 🏃‍♂️
--------------------------------------------------

* ライブラリ開発者はロガーを用意し、 **何もしないハンドラを設定** しよう
* アプリケーション開発者はルートロガーを設定し、 **propagateを利用してログを表示** しよう

ご清聴ありがとうございました
--------------------------------------------------

Enjoy Python logging❤️

.. include:: appendix.rst.txt

EOF
===
