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

:Event: PyCon mini Shizuoka 2024 **continue**
:Presented: 2025/02/08 nikkie

振替開催、誠にありがとうございます🫶
--------------------------------------------------

引き続き盛り上がって参りましょう！

お前、誰よ（👉Appendix）
======================================================================

* nikkie ／ :fab:`github` `@ftnext <https://github.com/ftnext>`__ ／ `ブログ <https://nikkie-ftnext.hatenablog.com/>`__ 連続 **810** 日突破
* 機械学習エンジニア・LLM・自然言語処理（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）
* Python歴は7年。PyConで登壇多数

.. image:: ../_static/uzabase-white-logo.png

アンケート（何度でも挙げよう）
--------------------------------------------------

* ``logging.warning()`` や ``logging.error()`` したことある🙋‍♂️
* ``logging.basicConfig()`` したことある🙋‍♀️
* ``logging.getLogger()`` したことある🙋

本トークの対象者
--------------------------------------------------

* Python標準ライブラリのloggingモジュールを **触ったことがある**
* loggingモジュールの中身はよく分からなくて全然OK👌

皆さんに質問です
======================================================================

* あなたはPythonで ``import`` して使いたいコードを書いています（例：ライブラリ）
* その中で **ロギング** 、どう実装しますか？

``import`` する予定のコードの中でのロギング
--------------------------------------------------

* ``logging.warning()`` （など）❓
* ``logging.basicConfig()`` ❓
* ``logging.getLogger()`` ❓

結論：「``NullHandler`` 以外はいけません」
--------------------------------------------------

.. literalinclude:: ../../samplecode/python-logging/conclusion/mylib.py
    :language: python
    :lines: 1-4

公式ドキュメント📄「`ライブラリのためのロギングの設定`_」

すべて **公式ドキュメント** に書いてあります！
--------------------------------------------------

* しかし、観測範囲ではライブラリ作成者に気づかれていない印象...😫
* 📄の付いたリンクは、公式ドキュメントへのリンク
* （別のemoji：🏃‍♂️は本編では飛ばします）

Logging クックブックの「避けるべきパターン」にも
--------------------------------------------------

* `ライブラリ内でロガーに NullHandler 以外のハンドラーを追加する`_ 📄

    (略) ログ出力をカスタマイズするのはライブラリ開発者ではなく、アプリケーション開発者の責務です。

ライブラリではオススメしません（ぶっぶー🙅‍♂️）🏃‍♂️
------------------------------------------------------------

.. code-block:: python

    logging.basicConfig()

.. code-block:: python

    logging.warning()

.. code-block:: python
    :emphasize-lines: 2

    logger = logging.getLogger(__name__)
    logger.addHandler(logging.StreamHandler())

本トークのメッセージ（**Takeaway**）
======================================================================

* ライブラリ開発者は *ロガー* を用意し、 *何もしないハンドラ* を設定しよう
* アプリケーション開発者は *ルートロガー* を設定し、 *propagate* を利用してログを表示しよう

斜体を解説していきます

本トークの構成
--------------------------------------------------

1. ライブラリ開発者へ
2. アプリケーション開発者へ
3. 落ち穂拾い

本トークで扱うloggingモジュール
--------------------------------------------------

* *ロガー*
* *ハンドラ*
* *フォーマッタ*
* フィルタ（Appendixのみ）

先行発表：loggingの構成要素（:icon-link:`🎥 <https://youtu.be/ahaslerbm_g?si=uymzSa4NdoeyqRcU>`）🏃‍♂️
--------------------------------------------------------------------------------------------------------------

.. https://2021.pycon.jp/time-table/?id=272259

.. raw:: html

    <iframe class="speakerdeck-iframe" style="border: 0px; background: rgba(0, 0, 0, 0.1) padding-box; margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 100%; height: auto; aspect-ratio: 560 / 315;" frameborder="0" src="https://speakerdeck.com/player/645f81e8b8144b1ba894a9bf5e78263e?slide=16" title="Loggingモジュールではじめるログ出力入門 / Introduction to Python Logging" allowfullscreen="true" data-ratio="1.7777777777777777"></iframe>

.. include:: library-logging.rst.txt

.. include:: application-logging.rst.txt

.. include:: gleanings.rst.txt

まとめ🌯 ライブラリ開発者に贈る「ロギングで ``NullHandler`` 以外はいけません」
================================================================================

.. revealjs-break::
    :notitle:

.. literalinclude:: ../../samplecode/python-logging/conclusion/mylib.py
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
