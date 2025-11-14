:ogp_title: Pythonを"理解"しているコーディングエージェントが欲しい！！
:ogp_event_name: yapc-fukuoka
:ogp_slide_name: lt-agent-who-understand-python
:ogp_description: YAPC::Fukuoka 2025 企画LT「あなたが本気で欲しいAI Agent」
:ogp_image_name: yapc-fukuoka

======================================================================
Pythonを"理解"しているコーディングエージェントが欲しい！！
======================================================================

デモ準備
======================================================================

* /plugin disable （/hooks ローカルだけに）
* 過去に作ったスクリプトは消す
* PS1
* tree -a

Pythonを"理解"しているコーディングエージェントが欲しい！！
======================================================================

.. https://fortee.jp/yapc-fukuoka-2025/proposal/1a3406b6-1310-44cd-b3c9-edcdc2d94347

:Event: YAPC::Fukuoka 企画LT「あなたが本気で欲しいAI Agent」
:Presented: 2025/11/14 nikkie

コーディングエージェント
======================================================================

* Claude Code（本LTの主役）
* Codex CLI
* Gemini CLI
* etc. etc. [#other_code_agents]_

.. Claude Code で話しますが、他のコーディングエージェントへも考え方の展開は可能だと思います

.. [#other_code_agents] Cursor, Windsurf, GitHub Copilot CLI などなどカキキレナイヨー

君たちは圧倒的に **速い** 🚄
---------------------------------------------------

人件費に比べて **安い** 💰

私は Python を書かせることが多いです

でも、Pythonのこと分かってます？
---------------------------------------------------

ClaudeがPythonを **理解しているようには見えない** んです

分かっていない一例：f-string
---------------------------------------------------

* フォーマット済み文字列リテラル
* **式** を含められる

.. code-block:: pycon

    >>> name = "りせ"
    >>> f"こんにちは、{name}さん！"
    'こんにちは、りせさん！'
    >>> print(f"2 + 3 = {2 + 3}")
    2 + 3 = 5

🤖「全部f-stringでええやろ！」
---------------------------------------------------

.. code-block:: python
    :caption: Claudeが書いたロギング

    logger.info(f"{user} - Something happened")
    logger.error(f"Python version: {sys.version}")

違う、そうじゃない
---------------------------------------------------

.. code-block:: python
    :caption: f-stringの代わりに%-formatと **使い分け**

    logger.info("%s - Something happened", user)
    logger.error("Python version: %s", sys.version)

📣私が決して書かないPythonを、私の名前でコミットしないで！

💡そうだ、リンタで指摘しよう
---------------------------------------------------

* 例：Ruff
* `logging-f-string (G004) <https://docs.astral.sh/ruff/rules/logging-f-string/>`__

    Logging statement uses f-string

Claude Codeの **フック** を設定
======================================================================

* Pythonを書いたときにリンタを実行する（ロギングのf-stringを含む **600超** のルール）
* リンタのエラー出力を繰り返しClaudeに見せる（逃 し ま せ ん）

デモ
---------------------------------------------------

    エラトステネスの篩をPythonで書いて

Claude Code v2.0.37

追記：応援ありがとうございました
---------------------------------------------------

.. code-block:: txt
    :caption: 本番アドリブの3往復

    > エラトステネスの篩をPythonで書いて
    ⏺ エラトステネスの篩をPythonで実装します。

    > いいね、ファイルに書いてみよっか
    ⏺ ファイルに書き込みます。どのファイル名にしますか？例えば sieve_of_eratosthenes.py などでしょうか？

    > それで
    ⏺ わかりました。sieve_of_eratosthenes.py として保存します。

セッション全体 https://gist.github.com/ftnext/58d17133b3b282831f136864ac770c28

追記：フックの様子
---------------------------------------------------

.. code-block:: txt

    ⎿ PostToolUse:Write hook returned blocking error: [jq -r '.tool_input.file_path' | { read file_path; if echo "$file_path" | grep -q 
        '\.py$'; then "$CLAUDE_PROJECT_DIR"/.claude/hooks/python_format.sh "$file_path"; fi; }]: cmd [1] | ruff check --config 
        '/.../hatch/env/.internal/hatch-static-analysis/.config/ukmfGEkg/ruff_defaults.toml' --fix 
        /.../2025-slides/samplecode/claude-code-harness/sieve_of_eratosthenes.py
        sieve_of_eratosthenes.py:11:12: PLR2004 Magic value used in comparison, consider replacing `2` with a constant variable
        sieve_of_eratosthenes.py:14:20: RUF003 Comment contains ambiguous `（` (FULLWIDTH LEFT PARENTHESIS). Did you mean `(` (LEFT 
        PARENTHESIS)?
        sieve_of_eratosthenes.py:14:25: RUF003 Comment contains ambiguous `）` (FULLWIDTH RIGHT PARENTHESIS). Did you mean `)` (RIGHT 
        PARENTHESIS)?
        sieve_of_eratosthenes.py:27:12: RET504 Unnecessary assignment to `primes` before `return` statement
        sieve_of_eratosthenes.py:34:5: T201 `print` found
        sieve_of_eratosthenes.py:35:5: T201 `print` found
        Found 6 errors.
        No fixes available (3 hidden fixes can be enabled with the `--unsafe-fixes` option).

    ⏺ ruffのチェックでいくつかエラーが出ているので、修正します。

追記：リントをパスしたエラトステネスの篩
---------------------------------------------------

.. code-block:: python

    MIN_PRIME = 2


    def sieve_of_eratosthenes(n):
        """
        エラトステネスの篩を使ってn以下の素数を求める

        Args:
            n: 素数を求める上限値

        Returns:
            n以下の素数のリスト
        """
        if n < MIN_PRIME:
            return []

        # 最初は全てTrueで初期化(素数候補)
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0と1は素数ではない

        # 2からsqrt(n)まで処理
        for i in range(MIN_PRIME, int(n**0.5) + 1):
            if is_prime[i]:
                # iの倍数を全て合成数としてマーク
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        # 素数のリストを生成
        return [i for i in range(n + 1) if is_prime[i]]


    # 使用例
    if __name__ == "__main__":
        import sys

        n = 100
        primes = sieve_of_eratosthenes(n)
        sys.stdout.write(f"{n}以下の素数: {primes}\n")
        sys.stdout.write(f"個数: {len(primes)}\n")

配布しています [#prerequisite]_
---------------------------------------------------

.. code-block:: shell

    /plugin marketplace add https://github.com/ftnext/claude-code
    /plugin install opinionated-python-hook@nikkie-marketplace

https://github.com/ftnext/claude-code

.. [#prerequisite] uvが必要です https://docs.astral.sh/uv/getting-started/installation/

💡サブエージェントの出番では
---------------------------------------------------

* **Pythonを書くサブエージェント** を用意した（`設定例 <https://github.com/ftnext/2025-slides/tree/5341f0021698527deea5195184aa69ebc9765a87/samplecode/claude-code-harness-v2/.claude>`__）
* メインの Claude Code のコンテキストにリントエラーとその修正過程は不要
* サブエージェントがPythonを書いた後、フックのリントエラーを見て修正していって *そう* [#apologies]_

.. [#apologies] 動作の様子からの判断です。ドキュメントの裏とり間に合わず🙏

まとめ🌯 Pythonを"理解"しているコーディングエージェントが欲しい！！
======================================================================

* 私の名前でコミットするからには、Pythonを理解して書いてもらおう
* Claude Codeのフックにリンタを設定して 逃 が さ な い（*自走* させる）

ご清聴ありがとうございました
--------------------------------------------------

* nikkie（にっきー）・Python使い・:fab:`github` `@ftnext <https://github.com/ftnext>`__ `sphinx-deck <https://github.com/ftnext/sphinx-deck>`__ など
* 機械学習エンジニア。 `Speeda AI Agent <https://www.uzabase.com/jp/info/20250901/>`__ 開発（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）

.. image:: ../_static/uzabase-white-logo.png

Appendix
======================================================================

* 逃がさないフック設定詳細
* 自走について先行発表

Claude Codeのフック設定
======================================================================

概要

* Pythonを書いたら＝PostToolUse
* フックの終了コードは2、標準エラー出力へ

**ローカル** のプロジェクトに設定
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

リファレンスの「`Hook出力 <https://docs.claude.com/ja/docs/claude-code/hooks#hook%E5%87%BA%E5%8A%9B>`__」参照 [#claude_code_hook_article]_

.. [#claude_code_hook_article] 拙ブログ `フックでリンタ（hatch fmt）のエラーを Claude Code に見せて、Python を理解している実装をさせる <https://nikkie-ftnext.hatenablog.com/entry/claude-code-hooks-run-hatch-fmt-good-python-code>`__

コーディングエージェントの自走
======================================================================

先行する発表

AI Coding Agent Enablement in TypeScript
--------------------------------------------------

.. raw:: html

    <iframe class="speakerdeck-iframe" style="border: 0px; background: rgba(0, 0, 0, 0.1) padding-box; margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 100%; height: auto; aspect-ratio: 560 / 315;" frameborder="0" src="https://speakerdeck.com/player/1b717ecfee8a4833a8ac0999900753d5?slide=29" title="AI Coding Agent Enablement in TypeScript" allowfullscreen="true" data-ratio="1.7777777777777777"></iframe>

.. https://nikkie-ftnext.hatenablog.com/entry/generative-ai-programming-with-fast-linter-python-case-ruff-ast-grep

関数型でTypeScriptを書かせる試み
--------------------------------------------------

.. raw:: html

    <iframe class="speakerdeck-iframe" style="border: 0px; background: rgba(0, 0, 0, 0.1) padding-box; margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 100%; height: auto; aspect-ratio: 560 / 315;" frameborder="0" src="https://speakerdeck.com/player/baf1965843b549f49f31703cc697b5b6?slide=1" title="LintのみでAIに開発スタイルを叩き込めるのか？" allowfullscreen="true" data-ratio="1.7777777777777777"></iframe>

EOF
===
