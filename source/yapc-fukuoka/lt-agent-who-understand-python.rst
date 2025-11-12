======================================================================
Pythonを"理解"しているコーディングエージェントが欲しい！！
======================================================================

Pythonを"理解"しているコーディングエージェントが欲しい！！
======================================================================

.. https://fortee.jp/yapc-fukuoka-2025/proposal/1a3406b6-1310-44cd-b3c9-edcdc2d94347

:Event: YAPC::Fukuoka 企画LT
:Presented: 2025/11/14 nikkie

コーディングエージェント
======================================================================

* Claude Code
* Codex CLI
* Gemini CLI
* etc. etc. [#other_code_agents]_

.. Claude Code で話しますが、他のコーディングエージェントへも考え方の展開は可能だと思います

.. [#other_code_agents] Cursor, Windsurf, GitHub Copilot CLI などなどカキキレナイヨー

圧倒的に速い🚄、そして、人力より安い💰
------------------------------------------------------------

（私は Python を書かせることが多いです）

あなた、Python分かってます？
---------------------------------------------------

* 私の目にはClaudeがPythonを理解しているようには見えない
* 私が決して書かないPythonを、私の名前でコミットしないで！

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

💡そうだ、リンタで指摘しよう
---------------------------------------------------

* `logging-f-string (G004) <https://docs.astral.sh/ruff/rules/logging-f-string/>`__

    ``G004`` Logging statements should not use ``f"..."`` for their first argument

.. Ruff

Claude Codeの **フック** を設定
======================================================================

* Pythonを書いたときにリンタを実行する（``hatch fmt``）
* リンタのエラー出力を繰り返しClaudeに見せる（逃 し ま せ ん）

デモ
---------------------------------------------------

    エラトステネスの篩をPythonで書いて

.. 配布？ TODO

.. サブエージェントの余地？

まとめ🌯 Pythonを"理解"しているコーディングエージェントが欲しい！！
======================================================================

* 私の名前でコミットするからには、Pythonを理解して書いてもらおう
* Claude Codeのフックにリンタを設定して 逃 が さ な い

ご清聴ありがとうございました
--------------------------------------------------

Happy AI-assisted development🤖

.. Appendix 自走について先行発表
