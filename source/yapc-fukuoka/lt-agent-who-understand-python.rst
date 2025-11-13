======================================================================
Pythonを"理解"しているコーディングエージェントが欲しい！！
======================================================================

Pythonを"理解"しているコーディングエージェントが欲しい！！
======================================================================

.. https://fortee.jp/yapc-fukuoka-2025/proposal/1a3406b6-1310-44cd-b3c9-edcdc2d94347

:Event: YAPC::Fukuoka 企画LT「あなたが本気で欲しいAI Agent」
:Presented: 2025/11/14 nikkie

お久しぶりです（2022年OnlineのLT）
======================================================================

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/bV8dm4I9148?si=azj1mdtKYf9w-ATR" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

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

ClaudeがPythonを理解しているようには見えないんです

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
    :caption: f-stringの代わりに%-format

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

配布しています
---------------------------------------------------

.. code-block:: shell

    /plugin marketplace add https://github.com/ftnext/claude-code
    /plugin install opinionated-python-hook@nikkie-marketplace

https://github.com/ftnext/claude-code

.. サブエージェントの余地？

まとめ🌯 Pythonを"理解"しているコーディングエージェントが欲しい！！
======================================================================

* 私の名前でコミットするからには、Pythonを理解して書いてもらおう
* Claude Codeのフックにリンタを設定して 逃 が さ な い（*自走* させる）

ご清聴ありがとうございました
--------------------------------------------------

* nikkie（にっきー）・Python使い・:fab:`github` `@ftnext <https://github.com/ftnext>`__
* 機械学習エンジニア。 `Speeda AI Agent <https://www.uzabase.com/jp/info/20250901/>`__ 開発（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）

.. image:: ../_static/uzabase-white-logo.png

.. Appendix 自走について先行発表
