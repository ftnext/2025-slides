:ogp_title: AIにPythonを理解したコードを書かせる試行錯誤
:ogp_event_name: wingarc-yumemi-ai
:ogp_slide_name: claude-understand-python
:ogp_description: AIを“相棒”にするための勉強会
:ogp_image_name: wingarc-yumemi-ai

======================================================================
AIにPythonを理解したコードを書かせる試行錯誤
======================================================================

:Event: AIを“相棒”にするための勉強会
:Presented: 2025/10/29 nikkie

お前、誰よ
======================================================================

* nikkie（にっきー）・Python使い
* :fab:`github` `@ftnext <https://github.com/ftnext>`__ 私が欲しい小さなライブラリをおすそ分けでOSS（`llm-claude-code <https://github.com/ftnext/llm-claude-code>`__）
* 機械学習エンジニア。 `Speeda AI Agent <https://www.uzabase.com/jp/info/20250901/>`__ 開発（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__） [#ai_agent_meetup]_

.. image:: ../_static/uzabase-white-logo.png

.. [#ai_agent_meetup] 今週末31日(金)夜にオンライン勉強会やります！`UB Tech vol.21 AIエージェントって何から始める？ソフトウェアエンジニアによる挑戦 <https://connpass.com/event/370935/>`__

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

    <blockquote class="twitter-tweet" data-lang="ja" data-align="center" data-dnt="true"><p lang="ja" dir="ltr">言語を少し深く知ってる開発者なら、いまのAIよりは自分のほうが（速くはないけど）詳しいって感覚なんですかねぇ <a href="https://twitter.com/hashtag/kichijojipm?src=hash&amp;ref_src=twsrc%5Etfw">#kichijojipm</a><br>私にとってはPythonがそうで、Claude Codeが書いてくるコード、Pythonを理解してないので、リンタが怒るようなコードをいつも書くんですよね（リンタを設定して渡さなきゃ</p>&mdash; nikkie(にっきー) / にっP (@ftnext) <a href="https://twitter.com/ftnext/status/1964228096263094311?ref_src=twsrc%5Etfw">September 6, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

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
    >>> print(f"2 + 3 = {2 + 3}")
    2 + 3 = 5

ロギングにf-stringは使わない [#fstring_logging_article]_
----------------------------------------------------------------------

.. code-block:: python
    :caption: f-stringの代わりに%-format

    logger.info("%s - Something happened", user)
    logger.error("Python version: %s", sys.version)

.. [#fstring_logging_article] 拙ブログ `Pythonのログメッセージにf-stringはいけません。そこのClaude、私はあなたに言っているんですよ <https://nikkie-ftnext.hatenablog.com/entry/hey-claude-dont-use-f-string-in-logging-messages>`__

しかしClaudeは平気でf-stringを使う
---------------------------------------------------

.. code-block:: python
    :caption: f-stringでロギングしてはいけません [#why_no_fstring_logging]_

    logger.info(f"{user} - Something happened")
    logger.error(f"Python version: {sys.version}")

.. [#why_no_fstring_logging] f-stringはその場で評価されるためです。%-formatならログレベルが有効なときのみ評価されます

💡リンタで指摘しよう
======================================================================

* `logging-f-string (G004) <https://docs.astral.sh/ruff/rules/logging-f-string/>`__
* `flake8-logging-format <https://github.com/globality-corp/flake8-logging-format/tree/0.9.0?tab=readme-ov-file#violations-detected>`__

    ``G004`` Logging statements should not use ``f"..."`` for their first argument

.. _Ruff: https://github.com/astral-sh/ruff

`Ruff`_
---------------------------------------------------

* Rustで書かれたPythonのリンタ兼フォーマッタ。速い [#ruff_command]_
* flake8やpylint（リンタ）・black（フォーマッタ）からRuffへの置き換えが進む

.. code-block:: console

    $ uvx ruff check --fix --extend-select I && uvx ruff format

.. [#ruff_command] 拙ブログ `Ruffは format と check --fix の2つのコマンドでフォーマットする (Ruff 0.7.2) <https://nikkie-ftnext.hatenablog.com/entry/ruff-as-python-formatter-two-commands>`__

:command:`hatch fmt`
---------------------------------------------------

* Ruffのリントとフォーマットは現状別々のコマンド
* Pythonプロジェクト管理ツール `Hatch <https://github.com/pypa/hatch>`__ は、Ruffのリントとフォーマットを1コマンドで流せる [#hatch_fmt_reference]_
* 普通にRuffを流すよりも **厳しいルール**

.. [#hatch_fmt_reference] https://hatch.pypa.io/latest/cli/reference/#hatch-fmt

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

.. literalinclude:: ../../samplecode/claude-code-harness/.claude/hooks/python_format_v0.sh
    :language: bash

フックのエラーメッセージをClaudeに見せるために
---------------------------------------------------

* :file:`python_format.sh` の終了コードを **2** にする（Claude Codeをブロック）
* ``hatch fmt`` の出力を **stderr** へ（Claudeが見る）

リファレンスの「`Hook出力 <https://docs.claude.com/ja/docs/claude-code/hooks#hook%E5%87%BA%E5%8A%9B>`__」参照 [#claude_code_hook_article]_

.. [#claude_code_hook_article] 拙ブログ `フックでリンタ（hatch fmt）のエラーを Claude Code に見せて、Python を理解している実装をさせる <https://nikkie-ftnext.hatenablog.com/entry/claude-code-hooks-run-hatch-fmt-good-python-code>`__

デモ
======================================================================

    エラトステネスの篩をPythonで書いて

.. revealjs-break::
    :notitle:

.. code-block:: console

    ⎿ PostToolUse:Write hook returned blocking error: [jq -r 
        '.tool_input.file_path' | { read file_path; if echo "$file_path"
        | grep -q '\.py$'; then 
        "$CLAUDE_PROJECT_DIR"/.claude/hooks/python_format.sh 
        "$file_path"; fi; }]: cmd [1] | ruff check --config 
        '/.../hatch/env/.internal/
        hatch-static-analysis/.config/ukmfGEkg/ruff_defaults.toml' --fix
        /.../claude-code-harness
        /sieve_of_eratosthenes.py
        sieve_of_eratosthenes.py:11:12: PLR2004 Magic value used in 
        comparison, consider replacing `2` with a constant variable
        sieve_of_eratosthenes.py:27:12: RET504 Unnecessary assignment to
        `primes` before `return` statement
        sieve_of_eratosthenes.py:35:5: T201 `print` found
        sieve_of_eratosthenes.py:36:5: T201 `print` found
        sieve_of_eratosthenes.py:37:5: T201 `print` found
        Found 5 errors.
        No fixes available (4 hidden fixes can be enabled with the 
        `--unsafe-fixes` option).


    ⏺ Pythonのlintエラーが  08:24 PM  claude-sonnet-4-5-20250929
    検出されました。修正
    します。

.. revealjs-break::
    :notitle:

.. code-block:: python
    :caption: 当日生成された :file:`sieve_of_eratosthenes.py`

    MINIMUM_PRIME = 2


    def sieve_of_eratosthenes(n):
        """
        エラトステネスの篩を使って、n以下の素数を全て求める

        Args:
            n: 上限値

        Returns:
            n以下の素数のリスト
        """
        if n < MINIMUM_PRIME:
            return []

        # 最初は全ての数を素数候補とする
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0と1は素数ではない

        # 2からsqrt(n)まで処理
        for i in range(MINIMUM_PRIME, int(n**0.5) + 1):
            if is_prime[i]:
                # iの倍数を全て合成数としてマーク
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        # 素数のリストを作成して返す
        return [i for i in range(n + 1) if is_prime[i]]


    # 使用例
    def main():
        # 100以下の素数を求める
        n = 100
        primes = sieve_of_eratosthenes(n)
        print(f"{n}以下の素数:")  # noqa: T201
        print(primes)  # noqa: T201
        print(f"\n素数の個数: {len(primes)}")  # noqa: T201


    if __name__ == "__main__":
        main()

時間があったら話すコンテンツ
======================================================================

* Pythonでフックを書く
* プラグインで配布

1️⃣ cchooks
---------------------------------------------------

* https://github.com/GowayLee/cchooks
* `hesreallyhim/awesome-claude-code <https://github.com/hesreallyhim/awesome-claude-code>`__ 掲載
* Pythonスクリプトでフックを書ける [#cchooks_article]_

.. [#cchooks_article] 拙ブログ `Claude Code のフックを Python スクリプトで書ける cchooks で hatch fmt を実行するフックを書く <https://nikkie-ftnext.hatenablog.com/entry/claude-code-hooks-cchooks-first-step-hatch-fmt>`__

inline script metadataと奇跡的相性🫶
---------------------------------------------------

.. code-block:: python

    #!/usr/bin/env -S uv run
    # /// script
    # requires-python = ">=3.11"
    # dependencies = [
    #     "cchooks",
    # ]
    # ///
    import subprocess

    import cchooks

    c = cchooks.create_context()

    if c.tool_input.get("file_path", "").endswith(".py"):
        file_path = c.tool_input["file_path"]
        result = subprocess.run(["uvx", "hatch", "fmt", file_path], capture_output=True, text=True)
        if result.returncode == 1:  # Need to fix formatting
            cchooks.exit_block(f"Fix `hatch fmt` issues:\n{result.stdout}")
        else:
            cchooks.exit_success()

2️⃣ プラグイン
---------------------------------------------------

* `Plugins <https://docs.claude.com/en/docs/claude-code/plugins>`__
* https://github.com/ftnext/claude-code を作った
* インストールできるが、PostToolUseの終了コード2で *止まって* しまう（v2.0.27で観測）

まとめ🌯 AIにPythonを理解したコードを書かせる試行錯誤
======================================================================

* Claude Code、Pythonを理解してないよなあ
* :command:`hatch fmt` をPostToolUseフックに設定して逃さない
* 引き続き磨き込んでいくぞ（コメント多い、型チェック）

ご清聴ありがとうございました
--------------------------------------------------

Happy AI-assisted development🤖

宣伝：`10/30(木)31(金)AI駆動開発カンファレンス <https://aid.connpass.com/event/367697/>`__ オンライン無料です！！

.. revealjs-break::
    :notitle:

.. raw:: html

    <blockquote class="twitter-tweet" data-lang="ja" data-align="center" data-dnt="true"><p lang="ja" dir="ltr">学マスの秦谷美鈴さんが言ったとされる<br>「わたしが上で、あなたが下です」<a href="https://t.co/tMEWieYG3i">https://t.co/tMEWieYG3i</a><br>ChatGPTとかClaudeを使うときのマインドセットに通じるものがあるかもしれません。LLMが下</p>&mdash; nikkie(にっきー) / にっP (@ftnext) <a href="https://twitter.com/ftnext/status/1949106210122391956?ref_src=twsrc%5Etfw">2025年7月26日</a></blockquote>
