:ogp_title: Claude CodeでVibe codingして作った、Claude Codeをコマンドラインから呼ぶためのsimonw/llmプラグイン
:ogp_event_name: aidd-cc1
:ogp_slide_name: llm-claude-code
:ogp_description: Claude Code Meetup Japan #1（Claude Code祭り！）
:ogp_image_name: aidd-cc1

====================================================================================================
Claude CodeでVibe codingして作った、Claude Codeをコマンドラインから呼ぶためのsimonw/llmプラグイン
====================================================================================================

Claude CodeでVibe codingして作った、Claude Codeをコマンドラインから呼ぶためのsimonw/llmプラグイン
====================================================================================================

:Event: Claude Code Meetup Japan #1（Claude Code祭り！）
:Presented: 2025/07/08 nikkie

お前、誰よ？（**Python使い** の自己紹介）
================================================================================

* nikkie（にっきー）
* 機械学習エンジニア・LLM・自然言語処理（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）
* `Speeda AI Agent <https://www.uzabase.com/jp/info/20250630/>`__ 開発

.. image:: ../_static/uzabase-white-logo.png

Simon Willison-sanによる :command:`llm` が好き
------------------------------------------------------------

.. code-block:: bash

    uvx --with llm-gemini \
      llm -m gemini-2.0-flash 'Tell me fun facts about Mountain View'

* :command:`llm` を他のUnixコマンドと **パイプ** で繋げられる！
* 自動ロギング（など）

simonw/llmのプラグインを **自作**
---------------------------------------------------

.. code-block:: bash

    uvx --with llm-devin llm -m devin \
      'このissue https://github.com/ftnext/playtest2-python/issues/4 に取り組んでみてください'

.. code-block:: bash

    uvx --with llm-devin \
      llm -m deepwiki -o repository simonw/llm \
      "llmの主要な機能を教えて"

`先日のDevin Meetup Japan #2 <https://www.youtube.com/live/hRqZN6YTLGA?si=1SC828p4w3HtN8mO&t=5827>`__

さて、Claude Codeには **SDK** がある
---------------------------------------------------

* `Claude Code SDK <https://docs.anthropic.com/en/docs/claude-code/sdk>`__
* TypeScript
* Python https://pypi.org/project/claude-code-sdk/

Claude Codeをコマンドラインから呼ぶためのsimonw/llmプラグインを作ろう！
================================================================================

`ftnext/llm-claude-code <https://github.com/ftnext/llm-claude-code>`__

デモ
---------------------------------------------------

.. code-block:: bash

    uvx --with llm-claude-code llm -m cc \
      '3月18日を1日目として今日が何日目かを数えるPythonスクリプトを書いてください'

結論：「それってClaude Codeでよくない？」
---------------------------------------------------

.. code-block:: bash

    claude -p '3月18日を1日目として今日が何日目かを数えるPythonスクリプトを書いてください'

* 反論のしようがございません！🎯🎯🎯
* simonw/llmの多くの機能は **Claude Codeにもある** （他のコマンドとパイプ、自動ロギング）

本発表の意義：**Claude CodeでVibe codingして作った**
================================================================================

* Vibe codingしての学びの共有
* ProプランのClaude 4 Sonnet

.. https://nikkie-ftnext.hatenablog.com/entry/claude-code-vibe-coding-simonw-llm-claude-code-0.0.1

:file:`CLAUDE.md`
---------------------------------------------------

* 大いに参考にした `Claude Codeで実用的なWebサービスを作る <https://note.com/himaratsu/n/nddf0efa67d42>`__
* Claude 4 Opusに用意してもらう
* vibe coding中はきりがよいところで更新をお願い

🏃‍♂️Claude 4 Opusへのプロンプト
---------------------------------------------------

.. code-block:: text
    
    simonw/llm のプラグインとして Claude Code SDK を使ってClaude Codeにpromptを送ってみたいです。
    実装方法について調査し、仕様の不明点は私に質問して、CLAUDE.mdをまず作ってください

E2Eテストを用意する
---------------------------------------------------

* コンテキストに必要なものは入れ、基本的にEnterを押し続ける
* 作業が一区切りしたら **コマンドを叩いて** やりたいことが実現されたか確認だけした

.. code-block:: bash

    uv run llm -m cc こんにちは

便利だったコマンド
---------------------------------------------------

* ``!``: E2Eのコマンド実行。シェルのコマンド打てる！！
* :kbd:`Ctrl + R`：出力展開。エラーの確認など

人間の経験と噛み合った
---------------------------------------------------

* simonw/llmの ``prompt`` 変数が `Prompt <https://github.com/simonw/llm/blob/0.26/llm/models.py#L271>`__ 型と分かっていない様子のClaude Code
* プラグイン開発経験から「``prompt.prompt`` が文字列」と伝えたことで完成！

機能拡張には私がボトルネック
---------------------------------------------------

* Claude Code SDKで **何ができるか** 分かってない
* 追加でやりたいこと、出てこない...（時間もないのでDevinに代わりにSDK触ってレポートしてもらってる）

まとめ🌯：Claude CodeでVibe codingしての学び
---------------------------------------------------

* :file:`CLAUDE.md`
* E2Eテスト :command:`uv run llm -m cc こんにちは`
* ``!`` と :kbd:`Ctrl + R` を体得

ご清聴ありがとうございました
--------------------------------------------------

Enjoy vibe coding!

https://github.com/ftnext/llm-claude-code
