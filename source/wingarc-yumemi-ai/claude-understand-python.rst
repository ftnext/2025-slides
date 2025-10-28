======================================================================
AIにPythonを理解したコードを書かせる試行錯誤
======================================================================

:Event: AIを“相棒”にするための勉強会
:Presented: 2025/10/29 nikkie

お前、誰よ
======================================================================

* nikkie（にっきー）・Python使い
* :fab:`github` `@ftnext <https://github.com/ftnext>`__ 私が欲しい小さなライブラリをおすそ分けでOSS
* 機械学習エンジニア。 `Speeda AI Agent <https://www.uzabase.com/jp/info/20250901/>`__ 開発（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）

.. image:: ../_static/uzabase-white-logo.png

.. _サム・アルトマン: https://publishing.newspicks.com/books/9784910063447

宣伝：書籍『`サム・アルトマン`_』、いかがですか？
------------------------------------------------------------

.. image:: ../_static/sama-book.jpg
    :width: 80%

今回は Claude Code の話
======================================================================

Codex CLI にゴリゴリOSSのソース読ませもしています（DeepWikiの代わりに）

.. revealjs-break::
    :notitle:

.. raw:: html

    <blockquote class="twitter-tweet" data-dnt="true"><p lang="ja" dir="ltr">言語を少し深く知ってる開発者なら、いまのAIよりは自分のほうが（速くはないけど）詳しいって感覚なんですかねぇ <a href="https://twitter.com/hashtag/kichijojipm?src=hash&amp;ref_src=twsrc%5Etfw">#kichijojipm</a><br>私にとってはPythonがそうで、Claude Codeが書いてくるコード、Pythonを理解してないので、リンタが怒るようなコードをいつも書くんですよね（リンタを設定して渡さなきゃ</p>&mdash; nikkie(にっきー) / にっP (@ftnext) <a href="https://twitter.com/ftnext/status/1964228096263094311?ref_src=twsrc%5Etfw">September 6, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

あなた Python 分かってます？
---------------------------------------------------

* Claudeは人類に比べて速く、安くPythonを書く
* ただ私からはPythonを **理解しているとは言えない**
* Pythonを理解しているなら書かないコードを頻繁に書くため

例：f-string
---------------------------------------------------

* フォーマット済み文字列リテラル
* **式** を含められる

.. code-block:: pycon

    >>> name = "りせ"
    >>> f"こんにちは、{name}さん！"
    'こんにちは、りせさん！'

ロギングにf-stringは使わない
---------------------------------------------------

.. code-block:: python
    :caption: f-stringの代わりに%-format

    logger.info("%s - Something happened", user)
    logger.error("Python version: %s", sys.version)

.. https://nikkie-ftnext.hatenablog.com/entry/hey-claude-dont-use-f-string-in-logging-messages

しかしClaudeは平気でf-stringを使う
---------------------------------------------------

.. code-block:: python
    :caption: f-stringでロギングしてはいけません

    logger.info(f"{user} - Something happened")
    logger.error(f"Python version: {sys.version}")

.. f-stringはその場で評価されるためです。%-formatならログレベルが有効なときのみ評価されます

💡リンタで指摘しよう
======================================================================

* `logging-f-string (G004) <https://docs.astral.sh/ruff/rules/logging-f-string/>`__
* `flake8-logging-format <https://github.com/globality-corp/flake8-logging-format/tree/0.9.0?tab=readme-ov-file#violations-detected>`__

    ``G004`` Logging statements should not use ``f"..."`` for their first argument

.. _Ruff: https://github.com/astral-sh/ruff

`Ruff`_
---------------------------------------------------

* Rustで書かれたPythonのリンタ兼フォーマッタ。速い
* flake8（リンタ）・black（フォーマッタ）からRuffへの置き換えが進む

.. code-block:: console

    $ uvx ruff check --fix --extend-select I && uvx ruff format

:command:`hatch fmt`
---------------------------------------------------

* Ruffのリントとフォーマットは現状別々のコマンド
* Pythonプロジェクト管理ツール `Hatch <https://github.com/pypa/hatch>`__ は、Ruffのリントとフォーマットを1コマンドで流せる
* 普通にRuffを流すよりも **厳しいルール**

Claude Codeの **フック** を設定
======================================================================

* Pythonを書いたときに ``hatch fmt`` を実行する
* ``hatch fmt`` の出力を繰り返しClaudeに見せる（逃 し ま せ ん）

ローカルのプロジェクトに設定
---------------------------------------------------

.. code-block:: text

    .claude/
    ├── hooks/
    │   └── python_format.sh
    └── settings.local.json

PostToolUseフック
---------------------------------------------------

EditまたはWriteでPythonファイルを書いたら

.. literalinclude:: ../../samplecode/claude-code-harness/.claude/settings.local.json
    :language: json

:file:`python_format.sh`
---------------------------------------------------

.. literalinclude:: ../../samplecode/claude-code-harness/.claude/hooks/python_format.sh
    :language: bash

フックのエラーメッセージをClaudeに見せるために
---------------------------------------------------

* :file:`python_format.sh` の終了コードを **2** にする（Claude Codeをブロック）
* ``hatch fmt`` の出力を **stderr** へ（Claudeが見る）

.. https://nikkie-ftnext.hatenablog.com/entry/claude-code-hooks-run-hatch-fmt-good-python-code

デモ
======================================================================
