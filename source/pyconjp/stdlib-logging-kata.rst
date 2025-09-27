:ogp_title: 標準ライブラリのlogging、レゴブロックのように組合せてロギングできることを理解しよう！
:ogp_event_name: pyconjp
:ogp_slide_name: stdlib-logging-kata
:ogp_description: PyCon JP 2025
:ogp_image_name: pyconjp

==========================================================================================
標準ライブラリのlogging、レゴブロックのように組合せてロギングできることを理解しよう！
==========================================================================================

標準ライブラリのlogging、レゴブロックのように組合せてロギングできることを理解しよう！
==========================================================================================

:Event: PyCon JP 2025（広島） ``#pyconjp_3``
:Presented: 2025/09/27 nikkie

皆さん、**自信** を持って標準ライブラリのloggingを使えていますか？
----------------------------------------------------------------------

loggingモジュールを理解しましょう！（Takeaway）
--------------------------------------------------

* *ロガー*、*ハンドラ* といった構成要素を理解する
* 構成要素を **組合せ** てロギングできることを理解する

レゴブロックのように組合せて（IMO）
--------------------------------------------------

* easy（理解しやすい）という意味でなく、 **単純** という意味でのsimple
* レゴブロックのように、単純なものを **組合せて複雑なもの** を作れる [#ooc-talk]_
* Pythonに見るsimple：Zen [#zen-of-python-simple]_ 、loggingモジュール、パッケージマネージャ

.. [#ooc-talk] `OOC 2024でもっと話しました <https://ftnext.github.io/2024-slides/ooc/software-lessons.html#/6>`__

.. [#zen-of-python-simple] *Simple is better than complex.* （`The Zen of Python <https://peps.python.org/pep-0020/>`__）

本トークの対象者
--------------------------------------------------

* 前提：**Pythonでロギングを実装した経験** あり
* loggingモジュールの使用経験は問いません
* 「loggingモジュールいまいちわからないんだよな...」、どんぴしゃターゲットです！

お前、誰よ
--------------------------------------------------

* nikkie ／ nikkie ／ :fab:`github` `@ftnext <https://github.com/ftnext>`__ / Python歴8年
* 機械学習エンジニア・LLM・自然言語処理（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）
* LLMアプリケーション開発で、 **LLMの入出力をロギング** してすべてを分かりたい（束縛系）

.. image:: ../_static/uzabase-white-logo.png

5章構成 [#chapter]_
--------------------------------------------------

1. loggingモジュールの構成要素
2. ロガーのレベル
3. ルートロガーへの *伝播* （**組合せたロギング**）
4. 現実世界のライブラリのロギング実装への対処
5. 落穂拾い

.. [#chapter] 章で構成したのは、最近推してる映画『`不思議の国でアリスと <https://sh-anime.shochiku.co.jp/alice-movie/>`__』インスパイアです

.. include:: logging-components.rst.txt

.. include:: logger-level.rst.txt

.. include:: propagate-to-root-logger.rst.txt

.. include:: resistance-against-real-world-logging.rst.txt

.. include:: gleanings.rst.txt

🌯最初の質問：自信を持って標準ライブラリのloggingを使えそうですか？
======================================================================

* ロガーの ``NOTSET`` レベル：**ルートロガーと同じ実効レベル** で使える
* ルートロガーへの伝播（propagate）：**ルートロガーのハンドラで出力**

まとめ🌯：標準ライブラリのlogging、レゴブロックのように組合せてロギングできることを理解しよう！
----------------------------------------------------------------------------------------------------

* ``NOTSET`` とpropagateから導かれる1つの **型** （ルートロガーでロギング）を紹介
* ライブラリの **利用者** が **望むフォーマット、出力先** でロギング

🌯ライブラリの **作者** はロガーの呼び出しのみ
------------------------------------------------------------

* **イベント記録だけ** したい
* ロギングのフォーマットや出力先には関心がない（利用者が自由に設定している前提で）
* ゆえに「ライブラリでルートロガーを触ってはいけません」

HTTPXのようなライブラリではない **手元のスクリプト** でも
------------------------------------------------------------

.. code-block:: python
    :caption: ルートロガーの設定は一箇所で、関数の中ではロガーを呼ぶだけ

    def awesome():
        # logger呼び出し（イベント記録のみ）
    def fabulous():
        # logger呼び出し（イベント記録のみ）
    def main():
        logging.basicConfig(...)  # ルートロガーにレベル、ハンドラ、フォーマッタ
        awesome()
        fabulous()

ご清聴ありがとうございました！
--------------------------------------------------

Happy Python Logging♪

Appendix
======================================================================

元にした先行発表
--------------------------------------------------

* 拙ブログ `Pythonで標準ライブラリloggingを使って自作ライブラリの中でロギングしたい未来の私へ <https://nikkie-ftnext.hatenablog.com/entry/python-logging-developing-library-take-advantage-nullhandler-and-propagate>`__
* 2月のPyCon mini Shizuoka 2024 continue `ライブラリ開発者に贈る「ロギングで NullHandler 以外はいけません」 <https://ftnext.github.io/2025-slides/pyconshizu/logging-with-nullhandler.html#/1>`__

お前、誰よ 補足
--------------------------------------------------

* :fab:`twitter` `@ftnext <https://twitter.com/ftnext>`__ ／ 登壇 `2025 <https://github.com/ftnext/2025-slides>`__ `2024 <https://github.com/ftnext/2024-slides>`__
* `ブログ <https://nikkie-ftnext.hatenablog.com/>`__ を1000日書いてます
* 毎月の `みんなのPython勉強会 <https://startpython.connpass.com/>`__ スタッフ

Special Thanks attakeiさん [#thanks-footnotes]_
------------------------------------------------------------

attakeiさんの `sphinx-revealjs <https://pypi.org/project/sphinx-revealjs/>`__ に以下の **自作拡張** を組み合わせて実現

* 私の代表作： `sphinx-new-tab-link <https://pypi.org/project/sphinx-new-tab-link/>`__
* `sphinx-revealjs-copycode <https://pypi.org/project/sphinx-revealjs-copycode/>`__
* `sphinx-revealjs-ext-codeblock <https://pypi.org/project/sphinx-revealjs-ext-codeblock/>`__

.. [#thanks-footnotes] 脚注の機能追加、誠にありがとうございます！

EOF
===
