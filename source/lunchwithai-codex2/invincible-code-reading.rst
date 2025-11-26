:ogp_title: Codex CLIで加速するコードリーディング
:ogp_event_name: lunchwithai-codex2
:ogp_slide_name: invincible-code-reading
:ogp_description: 爆速開発LT：Codex編 Vol.2
:ogp_image_name: lunchwithai-codex2

======================================================================
Codex CLIで **加速** するコードリーディング
======================================================================

:Event: 爆速開発LT：Codex編 Vol.2 ``#Lancers_AI_LT``
:Presented: 2025/11/26 nikkie（スライド **スクショOK**）

お前、誰よ？（**Python使い** の自己紹介）
======================================================================

* nikkie（にっきー） @ftnext
* 好きなことは、Python製ライブラリのソースコードを読むこと
* コーディングエージェントに対して強い **思想** を持つ

思想1：コンテキスト、教えて？（10月発表）
------------------------------------------------------------

.. raw:: html

    <iframe width="800" height="480" src="https://ftnext.github.io/2025-slides/aidd-codex1/codex-rs-telemetry.html#/4"
        title="ねぇ、Codex CLI。私だけにあなたのコンテキスト、教えて？"></iframe>

思想2：フックでClaude Code自走（11月発表）
------------------------------------------------------------

.. raw:: html

    <iframe width="800" height="480" src="https://ftnext.github.io/2025-slides/yapc-fukuoka/lt-agent-who-understand-python.html#/4"
        title="Pythonを'理解'しているコーディングエージェントが欲しい！！"></iframe>

お前、誰よ？（続き）
------------------------------------------------------------

* 機械学習エンジニア・LLM・自然言語処理（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）
* `Speeda AI Agent <https://www.uzabase.com/jp/info/20250901/>`__ 開発

.. image:: ../_static/uzabase-white-logo.png

.. _サム・アルトマン: https://publishing.newspicks.com/books/9784910063447

宣伝：書籍『`サム・アルトマン`_』、いかがですか？
------------------------------------------------------------

.. image:: ../_static/sama-book.jpg
    :width: 80%

私とCodex CLI
======================================================================

* **コードリーディング** に使っている
* コードはほとんど書かせていない [#swe_15]_
* `Codex Cloud <https://chatgpt.com/codex>`__ でBest-of-Nはごくたまにやる

.. [#swe_15] Windsurfの爆速なSWE-1.5を愛用

こいつ、できる
------------------------------------------------------------

* codex-rsにOTel計装のための `logfire <https://crates.io/crates/logfire>`__ を追加（10月登壇ネタ）したらビルドエラー
* Codex CLIが **インストールされたlogfireのソースを読んで** 解決

読める、読めるぞ！
------------------------------------------------------------

* OSSのライブラリでどう実装してるか気になったら、cloneして :command:`codex` 起動
* Codex CLIと一緒ならJavaScriptやRustも **Pythonと同じくらい** 読めてる感覚

実践：今回codex-rsをいくつか読んできました
======================================================================

* Codex CLIを使ってCodex CLIの実装（codex-rs）を読んだ
* ソースを読んだことで、Codex CLIの仕組みの理解が深まった

環境情報
------------------------------------------------------------

* macOS
* codex-cli 0.63.0 [#brew_codex]_
* gpt-5.1-codex（デフォルトモデル）
* Codex CLIには（Tier上げで余ってる）APIキー（発表準備で2ドル）

.. [#brew_codex] Homebrewでアップデートできなかった際に救われた：`CodexのHomebrewアップグレードが効かない件──原因と対処、そしてnpm版への移行について <https://gri.jp/media/entry/37479>`__

調査依頼例 [#other_prompts]_
------------------------------------------------------------

    OpenAI Codexのリポジトリです。 codex-rs/ 下からデフォルトのモデルはどう決まっているかまず教えてください

.. [#other_prompts] Appendixを参照ください

調査中のCodex CLIの表示
------------------------------------------------------------

.. image:: ../_static/lunchwithai-codex2/codex-screen.png

何をしている？

セッション履歴
------------------------------------------------------------

* :file:`~/.codex/sessions` に `resume <https://developers.openai.com/codex/cli/reference/#codex-resume>`__ に使う **JSON Lines** がある [#session_file_name]_

.. ~/.codex/sessions/2025/11/24/rollout-2025-11-24T08-24-32-019ab308-885d-77d3-859c-7c32c9db9416.jsonl

.. code-block:: json

    {"payload":{"type":"reasoning","summary":[{"type":"summary_text","text":"**Planning search for default model**"}],"content":null}}
    {"payload":{"type":"function_call","name":"shell_command","arguments":"{\"command\":\"ls\",\"workdir\":\"/.../openai-codex\"}","call_id":"call_Twy3ilTyWGpBGYlOS46CmYj6"}}
    {"payload":{"type":"function_call_output","call_id":"call_Twy3ilTyWGpBGYlOS46CmYj6","output":"Exit code: 0\nWall time: 0 seconds\nOutput:\nAGENTS.md\nCHANGELOG.md\nLICENSE\nNOTICE\nPNPM.md\nREADME.md\ncliff.toml\ncodex-cli\ncodex-rs\ndocs\nflake.lock\nflake.nix\npackage.json\npnpm-lock.yaml\npnpm-workspace.yaml\nscripts\nsdk\nshell-tool-mcp\n"}}

.. [#session_file_name] https://github.com/openai/codex/blob/rust-v0.63.0/codex-rs/core/src/rollout/recorder.rs#L315-L333

実は **シェルコマンドのみ**
------------------------------------------------------------

* 調査では ``shell_command`` ツールしか使っていない

.. code-block:: json

    {"payload":{"type":"function_call","name":"shell_command","arguments":"{\"command\":\"ls\",\"workdir\":\"/.../openai-codex\"}","call_id":"call_Twy3ilTyWGpBGYlOS46CmYj6"}}
    {"payload":{"type":"function_call","name":"shell_command","arguments":"{\"command\":\"rg -n \\\"default model\\\" -n\",\"workdir\":\"/.../openai-codex\"}","call_id":"call_k3OzGR9tqWa8Zs6eG3JkVBCF"}}
    {"payload":{"type":"function_call","name":"shell_command","arguments":"{\"command\":\"sed -n '1,200p' codex-rs/common/src/oss.rs\",\"workdir\":\"/.../openai-codex\"}","call_id":"call_lfIgOhegI4MhHP2B6DgDhe31"}}

Codex CLIの中のLLMの気持ち
======================================================================

* ユーザから「調査して」とプロンプトを与えられた
* 今いるディレクトリだけは分かる。そこに何があるかすら不明
* **シェルコマンドを入力すると結果が返ってくるツールだけ** がある

要は **調べ方を分かっている** ということ
------------------------------------------------------------

* :command:`ls` から始めてディレクトリ構造を掴む
* :command:`rg` で該当する可能性のあるファイル群を掴む
* 中身を確認（:command:`sed -n '1,200p'`）
* List, Search, Readを繰り返す

Listの例
------------------------------------------------------------

.. code-block:: bash

    % ls
    AGENTS.md		cliff.toml		package.json
    CHANGELOG.md	codex-cli		pnpm-lock.yaml
    LICENSE		codex-rs		pnpm-workspace.yaml
    NOTICE		docs			scripts
    PNPM.md		flake.lock		sdk
    README.md		flake.nix		shell-tool-mcp

Searchの例
------------------------------------------------------------

.. code-block:: bash
    :caption: `ripgrep <https://github.com/BurntSushi/ripgrep>`__

    % rg -n "default model"
    codex-rs/tui/src/app.rs
    678:                                .add_error_message(format!("Failed to save default model: {err}"));

    codex-rs/core/src/codex.rs
    310:    /// If not specified, server will use its default model.

    codex-rs/common/src/oss.rs
    7:/// Returns the default model for a given OSS provider.

    codex-rs/common/src/model_presets.rs
    42:    /// Whether this is the default model for new users.

Readの例
------------------------------------------------------------

.. code-block:: bash

    % sed -n '300,350p' codex-rs/core/src/codex.rs
                .as_deref()
                .unwrap_or(compact::SUMMARIZATION_PROMPT)
        }
    }

    #[derive(Clone)]
    pub(crate) struct SessionConfiguration {
        /// Provider identifier ("openai", "openrouter", ...).
        provider: ModelProviderInfo,

Codex CLIのコンテキストはどうなってる？
======================================================================

* システムプロンプトは？ 他のツールは？
* 👉 **Responses API** のリクエストを見る [#rust_log_article]_

.. [#rust_log_article] 拙ブログ `【速報】nikkie氏、ついに Codex CLI から Responses API へのリクエストを覗くことに成功！ <https://nikkie-ftnext.hatenablog.com/entry/codex-cli-rust-log-env-var-responses-api-request-json>`__

Responses APIのリクエスト
------------------------------------------------------------

* 全容 https://gist.github.com/ftnext/7b0caeec056188da387e8333e30be749
* システムプロンプト（100行） `gpt_5_codex_prompt.md <https://github.com/openai/codex/blob/rust-v0.63.0/codex-rs/core/gpt_5_codex_prompt.md>`__

    prefer using ``rg`` or ``rg --files`` respectively

Codex CLIのツールは ``shell_command`` に加えて
------------------------------------------------------------

* ``update_plan``
* ``apply_patch``
* ``view_image``
* MCP関連3つ

Gemini CLIと比べると
------------------------------------------------------------

.. code-block:: javascript
    :caption: https://github.com/google-gemini/gemini-cli/blob/v0.17.1/packages/core/src/tools/tool-names.ts#L11-L22
    :linenos:

    export const GLOB_TOOL_NAME = 'glob';
    export const WRITE_TODOS_TOOL_NAME = 'write_todos';
    export const WRITE_FILE_TOOL_NAME = 'write_file';
    export const WEB_SEARCH_TOOL_NAME = 'google_web_search';
    export const WEB_FETCH_TOOL_NAME = 'web_fetch';
    export const EDIT_TOOL_NAME = 'replace';
    export const SHELL_TOOL_NAME = 'run_shell_command';
    export const GREP_TOOL_NAME = 'search_file_content';
    export const READ_MANY_FILES_TOOL_NAME = 'read_many_files';
    export const READ_FILE_TOOL_NAME = 'read_file';
    export const LS_TOOL_NAME = 'list_directory';
    export const MEMORY_TOOL_NAME = 'save_memory';

Codex CLIの実装は、想像とはぜんぜん違った
------------------------------------------------------------

* Codex CLIは **ツールを絞って** いる
* コードベースの調査は ``shell_command`` でやってのける
* 裏のモデル（gpt-5.1-codex）が調査方法を分かっている

.. _/mention: https://developers.openai.com/codex/guides/slash-commands#highlight-files-with-mention

もう1つ `/mention`_
======================================================================

* Slash Command の1つ
* **@になるだけ**。ファイルパスのヒントが出て入力しやすい
* gpt-5.1-codex たちはファイルパスがあればReadするのだろう

Gemini CLI
------------------------------------------------------------

* ``@`` でファイルパスを指定する機能がある
* 指定した **ファイルのコンテンツ** がモデルに **渡されて** いた
* Codex CLIはこれをやっていない（きめ細かくReadしたいから？） [#compare_article]_

.. [#compare_article] 拙ブログ `Codex CLIの@(/mention)、Gemini CLIの@ <https://nikkie-ftnext.hatenablog.com/entry/coding-agent-at-mark-codex-cli-vs-gemini-cli>`__

まとめ🌯 Codex CLIで加速するコードリーディング
======================================================================

* Codex CLIはコードベースを **シェルコマンド** （``shell_command`` ツール）だけで巧みに調査する
* List・Search・Readの繰り返し。gpt-5.1-codexは超優秀なエンジニア感
* ファイルパスや行数を指定してより調べやすく（ファイルに書き出して依頼してます）

ご清聴ありがとうございました
------------------------------------------------------------

Enjoy code reading with Codex!

Appendixが続きます

他の依頼事項
------------------------------------------------------------

* OpenAI Codexのソースコードが codex-rs 下にあります。codexを使うと、$HOME/.codex/sessions/yyyy/mm/dd にJSONLファイルができているのですが、これはどのような処理で作られていますか？
* OpenAIのCodex CLIのリポジトリです。Sessionについて、OpenAIのエンドポイントにどのようなリクエストを送っているかを知りたいです。codex-rs/下にある実装を調査してください
* OpenAI Code CLIの実装が codex-rs/ 下にあります。Slash commandの中の/mentionってどんな実装ですか？

実装を見て同意見です
------------------------------------------------------------

.. raw:: html

    <blockquote class="twitter-tweet" data-lang="ja" data-dnt="true"><p lang="ja" dir="ltr">ここ数日、敢えてGemini 3だけで生活してみたけどまだ同じ感想です。<br>前と比べるとかなり良くなってるのは事実なんだけど、それでもなんか『勢いに任せて玉石混交の情報をぶちまけてるだけ』というのが変わってない。<br>GPTが『賢い』のに対してGeminiは『賢い情報も含んでる』みたいな感じ。… <a href="https://t.co/5hcT1n0XCA">https://t.co/5hcT1n0XCA</a></p>&mdash; 炎鎮🔥 - ₿onochin - (@super_bonochin) <a href="https://twitter.com/super_bonochin/status/1992832807283130798?ref_src=twsrc%5Etfw">2025年11月24日</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

EOF
===
