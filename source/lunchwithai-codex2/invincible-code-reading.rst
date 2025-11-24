======================================================================
Codex CLIでコードリーディング
======================================================================

:Event: 爆速開発LT：Codex編 Vol.2
:Presented: 2025/11/26 nikkie

お前、誰よ？（**Python使い** の自己紹介）
======================================================================

* nikkie（にっきー）
* 機械学習エンジニア・LLM・自然言語処理（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）
* `Speeda AI Agent <https://www.uzabase.com/jp/info/20250901/>`__ 開発

.. image:: ../_static/uzabase-white-logo.png

.. _サム・アルトマン: https://publishing.newspicks.com/books/9784910063447

宣伝：書籍『`サム・アルトマン`_』、いかがですか？
------------------------------------------------------------

.. image:: ../_static/sama-book.jpg
    :width: 80%

nikkieとCodex CLI
======================================================================

* **コードリーディング** に使っている
* コードはほとんど書かせていない（Windsurfの爆速なSWE-1.5を愛用）
* Codex CLIには（Tier上げで余ってる）APIキー（発表準備で2ドル）

読める、読めるぞ！
------------------------------------------------------------

* 元々Python製ライブラリのソースコードを読んでいた
* Codex CLIを使うとJavaScriptやRustも **Pythonと同じくらい** 読めてる感覚

原体験
------------------------------------------------------------

* codex-rsにOpenTelemetryの計装のためのlogfireを追加してビルドしていた
* ビルドエラーで、Codex CLIがlogfireのソースを読んで解決策を示した
* 「こいつ、ソースコードリーディングできるのでは」

実践：今回codex-rsをいくつか読んできました
======================================================================

    OpenAI Codexのリポジトリです。 codex-rs/ 下からデフォルトのモデルはどう決まっているかまず教えてください

* codex-cli 0.63.0
* gpt-5.1-codex（デフォルトモデル）

調べているときのCodexの表示
------------------------------------------------------------

* List
* Search
* Read

セッション履歴
------------------------------------------------------------

* :file:`~/.codex/sessions` にresumeに使うJSON Linesがある

.. ~/.codex/sessions/2025/11/24/rollout-2025-11-24T08-24-32-019ab308-885d-77d3-859c-7c32c9db9416.jsonl

.. code-block:: json

    {"payload":{"type":"reasoning","summary":[{"type":"summary_text","text":"**Planning search for default model**"}],"content":null}}
    {"payload":{"type":"function_call","name":"shell_command","arguments":"{\"command\":\"ls\",\"workdir\":\"/.../openai-codex\"}","call_id":"call_Twy3ilTyWGpBGYlOS46CmYj6"}}
    {"payload":{"type":"function_call_output","call_id":"call_Twy3ilTyWGpBGYlOS46CmYj6","output":"Exit code: 0\nWall time: 0 seconds\nOutput:\nAGENTS.md\nCHANGELOG.md\nLICENSE\nNOTICE\nPNPM.md\nREADME.md\ncliff.toml\ncodex-cli\ncodex-rs\ndocs\nflake.lock\nflake.nix\npackage.json\npnpm-lock.yaml\npnpm-workspace.yaml\nscripts\nsdk\nshell-tool-mcp\n"}}

実は **シェルコマンドのみ**
------------------------------------------------------------

* 調査では ``shell_command`` ツールしか使っていない

.. code-block:: json

    {"payload":{"type":"function_call","name":"shell_command","arguments":"{\"command\":\"ls\",\"workdir\":\"/.../openai-codex\"}","call_id":"call_Twy3ilTyWGpBGYlOS46CmYj6"}}
    {"payload":{"type":"function_call","name":"shell_command","arguments":"{\"command\":\"rg -n \\\"default model\\\" -n\",\"workdir\":\"/.../openai-codex\"}","call_id":"call_k3OzGR9tqWa8Zs6eG3JkVBCF"}}
    {"payload":{"type":"function_call","name":"shell_command","arguments":"{\"command\":\"sed -n '1,200p' codex-rs/common/src/oss.rs\",\"workdir\":\"/.../openai-codex\"}","call_id":"call_lfIgOhegI4MhHP2B6DgDhe31"}}

よく見かけるシェルコマンド
------------------------------------------------------------

:``ls``: List
:``rg`` (`ripgrep <https://github.com/BurntSushi/ripgrep>`__): Search
:``sed -n '1,200p'``: Read

Codex CLIに入ってみましょう
======================================================================

* システムプロンプト（後述）
* ユーザから「調査して」とプロンプトを与えられる
* 今いるディレクトリだけは分かる。そこに何があるかすら不明
* シェルでコマンドを実行できる（Tab補完はない）

要は **調べ方を分かっている** ということ
------------------------------------------------------------

* ``ls`` から始めてディレクトリ構造を掴む
* ``rg -n`` で該当する可能性のあるファイル群を掴む
* 中身を確認（``sed -n '1,200p'``）
* List, Search, Readを繰り返す

Listの例
------------------------------------------------------------

.. code-block:: bash

    % ls
    AGENTS.md		cliff.toml		package.json
    CHANGELOG.md		codex-cli		pnpm-lock.yaml
    LICENSE			codex-rs		pnpm-workspace.yaml
    NOTICE			docs			scripts
    PNPM.md			flake.lock		sdk
    README.md		flake.nix		shell-tool-mcp

Searchの例
------------------------------------------------------------

.. code-block:: bash

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

    % sed -n '1,200p' codex-rs/common/src/oss.rs
    //! OSS provider utilities shared between TUI and exec.

    use codex_core::LMSTUDIO_OSS_PROVIDER_ID;
    use codex_core::OLLAMA_OSS_PROVIDER_ID;
    use codex_core::config::Config;

    /// Returns the default model for a given OSS provider.

コンテキストはどうなってる？
======================================================================

* システムプロンプトは？ 他のツールは？
* **Responses API** のリクエストを見る

環境変数 ``RUST_LOG``
------------------------------------------------------------

.. code-block:: bash

    RUST_LOG=codex_core=trace codex exec "print hello" --skip-git-repo-check

`Tracing / verbose logging (Advanced) <https://github.com/openai/codex/blob/rust-v0.63.0/docs/advanced.md#tracing--verbose-logging-tracing-verbose-logging>`__

Responses APIのリクエスト
------------------------------------------------------------

* システムプロンプト `gpt_5_codex_prompt.md <https://github.com/openai/codex/blob/rust-v0.63.0/codex-rs/core/gpt_5_codex_prompt.md>`__
* 他のツールは（MCPの3つを除いて）

    * ``update_plan`` ・ ``apply_patch`` ・ ``view_image``

https://gist.github.com/ftnext/7b0caeec056188da387e8333e30be749

Codex CLIの実装は、想像とはぜんぜん違った
------------------------------------------------------------

* Claude Codeはツールがたくさんあるように見える（List用、Read用、Edit用）
* Codex CLIはツールを絞っている（``shell_command`` や ``apply_patch``）
* 裏のモデル（gpt-5.1-codex）が調査方法を分かっている

もう1つ ``/mention``
======================================================================

* Slash Command の1つ
* ``@`` になるだけ。ファイルパスのヒントが出て入力しやすい
* gpt-5.1-codex たちはファイルパスがあればReadするのだろう

Gemini CLI
------------------------------------------------------------

* ``@`` でファイルパスを指定する機能がある
* 指定したファイルのコンテンツがモデルに渡されていた
* Codex CLIがこれをやっていないのは、きめ細かくReadしたいから？

まとめ🌯 Codex CLIでコードリーディング
======================================================================

* Codex CLIはシェルコマンド（``shell_command`` ツール）を巧みに使って、List・Search・Readを繰り返して調査できる
* ファイルパスを入れて（``/mention``）詳しく依頼しよう（行数も見てくれそう）

ご清聴ありがとうございました
------------------------------------------------------------

Enjoy code reading with Codex!
