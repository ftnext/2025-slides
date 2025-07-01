====================================================================================================
Claude CodeでVibe codingして作った、Claude Codeをコマンドラインから呼ぶためのsimonw/llmプラグイン
====================================================================================================

Claude CodeでVibe codingして作った、Claude Codeをコマンドラインから呼ぶためのsimonw/llmプラグイン
====================================================================================================

:Event: AI駆動開発勉強会【Claude Code Meetup Japan #1】
:Presented: 2025/07/08 nikkie

お前、誰よ？（**Python使い** の自己紹介）
================================================================================

* nikkie（にっきー）
* 機械学習エンジニア・LLM・自然言語処理（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）
* :fab:`github` @ftnext 私が欲しい小さなライブラリをおすそ分けでOSS

.. image:: ../_static/uzabase-white-logo.png

simonw/llm が好き
---------------------------------------------------

* 勝手に師匠認定したSimon Willisonさん
* :command:`llm` を他のUnixコマンドと **パイプ** で繋げられる！
* 自動ロギング（など）

.. コマンド？

simonw/llmのプラグインを開発
---------------------------------------------------

.. code-block:: bash

    uvx --with llm-devin llm -m devin \
      'このissue https://github.com/ftnext/playtest2-python/issues/4 に取り組んでみてください'

.. code-block:: bash

    uvx --with llm-devin \
      llm -m deepwiki -o repository simonw/llm \
      "llmの主要な機能を教えて"

Claude CodeにはSDKがある
---------------------------------------------------

Claude Codeをコマンドラインから呼ぶためのsimonw/llmプラグインを作ろう！
================================================================================

`ftnext/llm-claude-code <https://github.com/ftnext/llm-claude-code>`__

.. コマンド例

結論：「それってClaude Codeでよくない？」
---------------------------------------------------

反論のしようがございません！

本発表の意義：**Claude CodeでVibe codingして作った**
================================================================================

Vibe codingしての学びの共有

.. https://nikkie-ftnext.hatenablog.com/entry/claude-code-vibe-coding-simonw-llm-claude-code-0.0.1

.. CLAUDE.md

E2Eを用意する
---------------------------------------------------

* コンテキストに必要なものは入れ、基本的にEnterを押し続ける
* 作業が一区切りしたらEnd to Endで確認だけするようにした

.. code-block:: bash

    uv run llm -m cc こんにちは

便利だったコマンド
---------------------------------------------------

* ``!``: E2Eのコマンド実行。シェルのコマンド打てる！！
* :kbd:`Ctrl + R`：出力展開。エラーの確認など

人間の経験と噛み合った
---------------------------------------------------

* simonw/llmのpromptの型が分かっていない様子のClaude Code
* 「``prompt.prompt`` が文字列」と伝えたことで完成！

.. 機能拡張に理解を深める必要があると感じた
