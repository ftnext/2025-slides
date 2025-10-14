:ogp_title: ねぇ、Codex CLI。私だけにあなたのコンテキスト、教えて？
:ogp_event_name: aidd-codex1
:ogp_slide_name: codex-rs-telemetry
:ogp_description: Codex Meetup Japan #1
:ogp_image_name: aidd-codex1

======================================================================
ねぇ、Codex CLI。私だけにあなたのコンテキスト、教えて？
======================================================================

デモ準備メモ
======================================================================

* VS Codeでcodex-rs、rust-v0.42.0タグ + ローカルの変更を開く
* VS Codeのターミナルで :file:`.env` 読み込み
* ブラウザは https://logfire-us.pydantic.dev/ftnext/first-time-logfire

.. VS Codeコマンドカンペ (codex-rs/ 下で)
    PS1='%# '
    source .env 

ねぇ、Codex CLI。私だけにあなたのコンテキスト、教えて？
======================================================================

:Event: Codex Meetup Japan #1
:Presented: 2025/10/14 nikkie

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

持論：コーディングエージェントは **全て** 分かりたい
======================================================================

*ねぇ、Codex CLI。私だけにあなたのコンテキスト、教えて？*

.. _codex-rs: https://github.com/openai/codex/tree/main/codex-rs

Codexは **Rust** 実装（`codex-rs`_）
------------------------------------------------------------

    リリース１ヶ月後にはTypeScriptからRustにスクラッチで書き直され

laisoさん `新Codex CLIの使い方 <https://blog.lai.so/codex-rs-intro/>`__

.. _#2103: https://github.com/openai/codex/pull/2103

.. _v0.44.0: https://github.com/openai/codex/releases/tag/rust-v0.44.0

`v0.44.0`_ で **OpenTelemetry** [#otel]_ の実装が入った
------------------------------------------------------------

    `#2103`_ OpenTelemetry events

.. [#otel] OpenTelemetryは、可観測性（システムの出力から内部状態を理解する能力）を得る手段

OpenTelemetry events (`#2103`_ v0.44.0)
======================================================================

.. code-block:: toml
    :caption: デフォルト設定（:file:`~/.codex/config.toml`）

    [otel]
    environment = "staging"
    exporter = "none"
    log_user_prompt = false

``otel.exporter`` を指定して起動
------------------------------------------------------------

.. code-block:: bash

    codex -c 'otel.log_user_prompt=true' \
      -c "otel.exporter={otlp-http={endpoint=\"https://logfire-us.pydantic.dev/v1/logs\",headers={Authorization=\"Bearer $LOGFIRE_TOKEN\"},protocol=\"json\"}}"

今回は *Logfire* で観測します
------------------------------------------------------------

.. image:: ../_static/aidd-codex1/codex-rs-otel-export.png

Codex CLIのコンテキスト、もっと見たい！
======================================================================

システムプロンプトなど、 **どんなコンテキストエンジニアリングをしているか** を見たい、分かりたい

Using OpenAI Codex & Pydantic Logfire to Debug Rust Code
----------------------------------------------------------------------

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/hr6pFn46pKk?si=7XzOcKTj2wMiwnEI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

.. revealjs-break::

* Pydantic社による配信のアーカイブ
* `Logfire <https://pydantic.dev/logfire>`__ という可観測性サービス。`Rust向けのSDK <https://github.com/pydantic/logfire-rust>`__ も提供
* **codex-rsにLogfire Rust SDKを組み込んで**、Codexの挙動を観測

Codex CLIは手元でビルドできる！
------------------------------------------------------------

* v0.44.0 の前の **v0.42.0** (`rust-v0.42.0 <https://github.com/openai/codex/tree/rust-v0.42.0/codex-rs>`__)
* :command:`cargo run --bin codex`
* ⚠️v0.44.0 で入ったOpenTelemetryの実装とLogfireを一緒に動かせてないです

デモ：手元でビルド〜Logfireに記録
------------------------------------------------------------

.. image:: ../_static/aidd-codex1/codex-rs-logfire1.png

.. revealjs-break::

.. image:: ../_static/aidd-codex1/codex-rs-logfire2.png

まとめ🌯：ねぇ、Codex CLI。私だけにあなたのコンテキスト、教えて？
======================================================================

* 持論：コーディングエージェントは全て分かりたい -> **可観測性**
* :command:`codex -c` でOpenTelemetryのexporterを指定できる
* Logfire Rust SDKを組み込む動画に沿ってローカルでビルドし、コンテキストを覗いてみた

ご清聴ありがとうございました
------------------------------------------------------------

Enjoy coding with Codex!

Appendixが続きます

OpenTelemetryの補足
======================================================================

* `OpenTelemetry <https://opentelemetry.io/ja/docs/what-is-opentelemetry/>`__ は、テレメトリの送出・処理・受信のオープンソース
* ベンダー・ツール非依存
* 今回テレメトリの保存と表示は *Logfire* に任せた（他のツールに差し替え可能）

Logfire Rust SDK を入れた箇所
------------------------------------------------------------

.. code-block:: diff
    :caption: :file:`codex-rs/tui/src/lib.rs`

    -    let _ = tracing_subscriber::registry().with(file_layer).try_init();
    +    let logfire = logfire::configure()
    +        .local()
    +        .with_service_name("codex")
    +        .finish()
    +        .expect("Failed to configure Logfire");
    +
    +    let _ = tracing_subscriber::registry().with(file_layer).with(logfire.tracing_layer()).try_init();

拙ブログ `Pydantic 社の動画アーカイブに沿って Logfire Rust SDK を追加し、Codex CLI 動作中の情報を Logfire に記録する <https://nikkie-ftnext.hatenablog.com/entry/try-using-openai-codex-and-pydantic-logfire-to-debug-rust-code>`__

Claude Code で可観測性
------------------------------------------------------------

.. code-block:: bash
    :caption: これだけでコンソールに出ます

    export CLAUDE_CODE_ENABLE_TELEMETRY=1
    export OTEL_LOGS_EXPORTER=console

拙ブログ `Claude Code が OpenTelemetry をサポートしていました <https://nikkie-ftnext.hatenablog.com/entry/claude-code-supports-opentelemetry>`__

Gemini CLI で可観測性
------------------------------------------------------------

.. code-block:: bash
    :caption: これだけでファイルに出ます

    export GEMINI_TELEMETRY_ENABLED=true
    export GEMINI_TELEMETRY_OUTFILE='gemini-telemetry.log'

**システムプロンプトまで** 見えます

拙ブログ `テレメトリを有効にして、Gemini CLI から Gemini API へのリクエスト・レスポンスを覗けるようにする <https://nikkie-ftnext.hatenablog.com/entry/gemini-cli-observability-with-opentelemetry-get-started>`__

準備は **Codex CLIにコードを読ませて** 進めた
------------------------------------------------------------

* 試しにcodexに質問したら、Logfire SDKのソースコードまで読みに行っていた
* そこからはガンガン読ませていった（ただv0.44.0で動かすまではいけてません）
* 1回で数万〜10万トークン使うので、Proゆえの富豪アプローチかも（Pulseを体験したくて）

過去のAI駆動開発勉強会LT
------------------------------------------------------------

* Devin Meetup Japan #2 `コマンドラインからDevinを呼び出してみないか？ <https://ftnext.github.io/2025-slides/aid-devin2/llm-devin.html>`__
* Claude Code Meetup Japan #1 `Claude CodeでVibe codingして作った、Claude Codeをコマンドラインから呼ぶためのsimonw/llmプラグイン <https://ftnext.github.io/2025-slides/aidd-cc1/llm-claude-code.html#1>`__

EOF
===
