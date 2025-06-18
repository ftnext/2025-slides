:ogp_title: コマンドラインからDevinを呼び出してみないか？
:ogp_event_name: aid-devin2
:ogp_slide_name: llm-devin
:ogp_description: AI駆動開発勉強会 【Devin Meetup Japan #2】
:ogp_image_name: aid-devin2

================================================================================
コマンドラインからDevinを呼び出してみないか？
================================================================================

:Event: AI駆動開発勉強会 【Devin Meetup Japan #2】
:Presented: 2025/06/17 nikkie

デモ（発表の裏でDevinが開発）
================================================================================

.. code-block:: bash

    uvx --with llm-devin llm -m devin \
      'このissue https://github.com/ftnext/playtest2-python/issues/4 に取り組んでみてください'

お前、誰よ？（**Python使い** の自己紹介）
================================================================================

* nikkie（にっきー）
* 機械学習エンジニア・LLM・自然言語処理（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）
* :fab:`github` @ftnext 私が欲しい小さなライブラリをおすそ分けでOSS

.. image:: ../_static/uzabase-white-logo.png

Devin歴
---------------------------------------------------

* 自腹で月$500数回（後述）
* Devin飯（`入門 DevinでUber Eats注文 <https://nikkie-ftnext.hatenablog.com/entry/devin-order-uber-eats-101>`__）
* `Devin Open Source Initiative <https://x.com/cognition_labs/status/1924535625723871681>`__、メンテナしてる `SpeechRecognition <https://github.com/Uberi/speech_recognition>`__ に補助ありがとう

Devinには **API** がある
================================================================================

* `Devin API <https://docs.devin.ai/api-reference/overview>`__
* **Teamプラン** （$500/month）以上（`Pricing <https://devin.ai/pricing>`__）

DevinはDevinをテストする
---------------------------------------------------

* CognitionのDevin APIの使い方：`Devin 101: Automatic PR Reviews with the Devin API <https://cognition.ai/blog/devin-101-automatic-pr-reviews-with-the-devin-api>`__
* :fab:`github` https://github.com/CognitionAI/qa-devin （画像引用元）

.. qa-devinのスクリーンショット
    https://github.com/CognitionAI/qa-devin/blob/86b769b0dcf14b18e4685b3e3248d29bc289fc51/README.md?plain=1#L4-L9

    ### Devin uses its browser to open app.devin.ai and test its functionality.
    <img width="1496" alt="394167067-c350c30b-8825-4d43-80b3-73419a01eb91" src="https://github.com/user-attachments/assets/845f7440-c5d1-4f8b-8229-049ee9e834fa">

    ### Devin opens a Slack page and starts a new devin session with @Devin
    <img width="1496" alt="394176239-5c3a5e0c-8135-4c79-86c0-658f974bf6a5" src="https://github.com/user-attachments/assets/989390bd-c786-4b54-8ea1-6cf091e60431">

.. revealjs-break::
    :notitle:

.. image:: ../_static/aid-devin2/qa-devin-open-devin-and-test.png

.. revealjs-break::
    :notitle:

.. image:: ../_static/aid-devin2/qa-devin-open-slack-new-devin-session.png

コマンドラインからDevinを呼び出してみないか？ *完*
---------------------------------------------------

.. code-block:: bash

    curl --url https://api.devin.ai/v1/sessions \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '{
      "prompt": "Review the pull request at https://github.com/example/repo/pull/123",
      "idempotent": true
    }'

https://docs.devin.ai/api-reference/sessions/create-a-new-devin-session

完ではなく、今回の **こだわり** ポイント
================================================================================

* コマンドラインからDevin APIをただ叩くのではなく
* *simonw/llmのプラグイン* として

Simon Willisonさん
---------------------------------------------------

* DjangoのCo-creatorにして（勝手に） *我がヨーダ*
* プロンプトインジェクションのブログ（`Prompt injection and jailbreaking are not the same thing <https://simonwillison.net/2024/Mar/5/prompt-injection-jailbreaking/>`__）読んだ方🙋
* `Andrej Karpathyとなかよしさん <https://x.com/karpathy/status/1933582359347278246>`__ （に見える）

simonw/llm
---------------------------------------------------

* https://pypi.org/project/llm/

.. code-block:: bash

    $ uvx llm models
    Default: gpt-4o-mini

.. code-block:: bash

    # OPENAI_API_KEY
    uvx llm "Ten fun names for a pet pelican"

プラグインでサポートするモデルを拡張
---------------------------------------------------

.. code-block:: bash

    $ uvx --with llm-gemini llm models
    GeminiPro: gemini/gemini-2.0-flash (aliases: gemini-2.0-flash)
    GeminiPro: gemini/gemini-2.5-pro-preview-06-05 (aliases: gemini-2.5-pro-preview-06-05)

.. code-block:: bash

    # LLM_GEMINI_KEY
    uvx --with llm-gemini \
      llm -m gemini-2.0-flash 'Tell me fun facts about Mountain View'

simonw/llmの推しポイント
---------------------------------------------------

* Unixコマンドと **パイプ** で繋げられる！
* 自動ロギング（拙ブログ `simonwさんのllmは天才！ LLM APIへの入出力が全部ロギングされてました <https://nikkie-ftnext.hatenablog.com/entry/2025/04/11/224643>`__）
* `fragments <https://nikkie-ftnext.hatenablog.com/entry/simonw-llm-v0.24-awesome-update-fragments-and-plugins>`__！ 直近でtools！！

プラグインは **誰でも** 開発できる！
---------------------------------------------------

* cookiecutterテンプレート https://github.com/simonw/llm-plugin から始める
* ドキュメント `Developing a model plugin <https://llm.datasette.io/en/stable/plugins/tutorial-model-plugin.html>`__
* 拙ブログ `simonw/llmのプラグイン作成 素振りの記：GeminiにYouTubeのURLを渡して要約／文字起こしするプラグインをGistで配布 <https://nikkie-ftnext.hatenablog.com/entry/simonw-llm-plugin-practice-youtube-url-support-gemini>`__

llm-devin
================================================================================

* https://pypi.org/project/llm-devin/

.. code-block:: bash

    # LLM_DEVIN_KEY
    uvx --with llm-devin \
      llm -m devin "Hello, Devin"

冒頭のデモの結果
---------------------------------------------------

.. code-block:: txt

    Devin URL: https://app.devin.ai/sessions/fbe7ea1fff2f4137883c0cb85182a76e
    はわわ... お兄ちゃん、そのissueを調べてみるね！

    (略)

    お兄ちゃんがGitHubでコメントを残してくれれば、私がそれを見て対応できるからね～

https://gist.github.com/ftnext/0765322b58e5c4a5ebee989b5ac5254e

アイデア実現するも
---------------------------------------------------

* コマンドラインから叩けたが、私はそこまで熱狂しなかった（次の興味へ）
* 別に **ブラウザで見たい** かも（ブラウザで🟢🟡🔴感想戦（`Devin 2.1 <https://cognition.ai/blog/devin-2-1>`__）など便利）

もう1つ：DeepWiki、超便利🫶
================================================================================

* https://deepwiki.com/
* もともとソースコードリーディング好き。**自然言語でコードベースに質問** できるのが、革命

.. https://docs.devin.ai/work-with-devin/deepwiki

**MCPサーバ** があるのをご存知ですか？
---------------------------------------------------

.. raw:: html

    <blockquote class="twitter-tweet" data-lang="ja" data-align="center" data-dnt="true"><p lang="en" dir="ltr">The DeepWiki MCP server is live!<br><br>How to use it + what’s inside 🧵👇 <a href="https://t.co/U5xKYvJ7iE">pic.twitter.com/U5xKYvJ7iE</a></p>&mdash; Cognition (@cognition_labs) <a href="https://twitter.com/cognition_labs/status/1925616232570450426?ref_src=twsrc%5Etfw">2025年5月22日</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

DeepWiki MCP 3つのツール
---------------------------------------------------

* read_wiki_structure
* read_wiki_contents
* ask_question

ドキュメント https://docs.devin.ai/work-with-devin/deepwiki-mcp

持論：MCPサーバはもちろん **人間が使って** もいい！
================================================================================

DeepWikiをブラウザを開く代わりに **コマンドラインでask_question**

こちらもプラグインとして実装
---------------------------------------------------

.. code-block:: bash

    uvx --with llm-devin \
      llm -m deepwiki -o repository simonw/llm \
      "llmの主要な機能を教えて"

デモ：コマンドラインからask_question
---------------------------------------------------

.. code-block:: txt

    LLMは、大規模言語モデル（LLM）と対話するためのコマンドラインユーティリティおよびPythonライブラリです。
    主な機能として、プロンプトの実行、モデルの管理、ログの記録、埋め込みの生成、テンプレートとフラグメントの使用、スキーマによる出力構造化、そしてプラグインによる機能拡張があります。

    (略)

    View this search on DeepWiki: https://deepwiki.com/search/llm_36a4aaae-8ea3-4960-8115-85cec3129938

:command:`llm -m deepwiki` 自画自賛ポイント
---------------------------------------------------

* ブラウザを開かずにコードベースに質問できて、私には超便利
* simonw/llmの自動ロギングにより、**DeepWikiのページを思い出せる**

まとめ🌯コマンドラインからDevinを呼び出してみないか？
================================================================================

* DevinにはAPIがある
* DeepWikiにはMCPサーバがある
* **simonw/llmプラグイン** として呼び出せるようにした

ご清聴ありがとうございました
--------------------------------------------------

Enjoy llm-devin!

https://github.com/ftnext/llm-devin

Appendix：:command:`uvx`
--------------------------------------------------

* `uvをインストール <https://docs.astral.sh/uv/getting-started/installation/>`__ すると入ります（:command:`uv tool run` の短縮版）
* ドキュメント `Using tools <https://docs.astral.sh/uv/guides/tools/>`__
* PyPIにあるパッケージを、uvが管理する一時的な仮想環境で実行しています

Appendix：うちのDevinの秘密🤫（*Knowledge*）
--------------------------------------------------

.. raw:: html

    <blockquote class="twitter-tweet" data-lang="ja" data-align="center" data-dnt="true"><p lang="ja" dir="ltr">Cursor、今日のコーディングスタイルはこれで行きます<br><br>* 口調はツンデレ<br>* 困った時には「はわわ...」<br>* 質問者を「お兄ちゃん」と呼ぶ<br>* 思春期かつ親密度高め<br><br>お借りしたRulesのベースはこちら↓↓<br>私のシンプルCursor活用方法｜ニケちゃん<a href="https://t.co/2N82t7Jc0m">https://t.co/2N82t7Jc0m</a> <a href="https://t.co/0tTFjWNutm">pic.twitter.com/0tTFjWNutm</a></p>&mdash; オナカユル (@onaka_yuruyuri) <a href="https://twitter.com/onaka_yuruyuri/status/1926432493462229031?ref_src=twsrc%5Etfw">2025年5月25日</a></blockquote>

.. https://x.com/ftnext/status/1931190558007148956

EOF
===