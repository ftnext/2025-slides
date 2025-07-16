======================================================================
Pythonで Agent2Agent Protocol
======================================================================

:Event: みんなのPython勉強会#116
:Presented: 2025/07/17 nikkie

AI Agent **どうし** の話
======================================================================

    (略) Agentic AI systems represent a paradigmatic shift marked by multi-agent collaboration, (略)

論文「`AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges <https://arxiv.org/abs/2505.10468>`__」によれば、単体のエージェントをAgentic AIとは呼びません

.. _Announcing the Agent2Agent Protocol (A2A): https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/

A2A、ご存知ですか？🙋
------------------------------------------------------------

* この **4月** のGoogle Cloud Next ‘25で発表
* `Announcing the Agent2Agent Protocol (A2A)`_

.. https://cloud.google.com/blog/products/ai-machine-learning/build-and-manage-multi-system-agents-with-vertex-ai

.. _A2Aのページ: https://a2aproject.github.io/A2A/latest/

`A2Aのページ`_ より
------------------------------------------------------------

    Build with ADK (or any framework), equip with MCP (or any tool), and communicate with A2A, to remote agents, local agents, and humans.

A2Aのコンセプト🏃‍♂️
------------------------------------------------------------

* フレームワーク（`ADK <https://google.github.io/adk-docs/>`__ など）を使って、エージェントを構築
* エージェントに **ツール** を持たせる（MCP）
* A2Aでリモートエージェント、ローカルエージェント、 *人類* が **やりとり**

**リモート** エージェントと **ローカル** エージェント
======================================================================

.. image:: ../_static/stapy-july/Agent2Agent-announcement-how-works.png
    :scale: 25%

`Announcing the Agent2Agent Protocol (A2A)`_ より引用

サーバとクライアント
------------------------------------------------------------

:リモートエージェント: A2Aサーバ
:ローカルエージェント: A2Aクライアント

**HTTP** でやり取り

A2Aサーバの実装
------------------------------------------------------------

* `GET /.well-known/agent.json`

    * `Agent Card <https://a2aproject.github.io/A2A/latest/specification/#5-agent-discovery-the-agent-card>`__ 公開

* `POST /` （※Agent Cardに記載）

    * JSON RPCでクライアントから呼び出す

a2a-sdk
======================================================================

* https://pypi.org/project/a2a-sdk/
* PythonでA2Aサーバ・クライアントの実装例（フレームワーク非依存）
* Hello World サンプル：https://github.com/a2aproject/a2a-samples/tree/main/samples/python/agents/helloworld

Agent Development Kitを例に
------------------------------------------------------------

    Add A2A support as experimental features (`1.6.1 <https://github.com/google/adk-python/releases/tag/v1.6.1>`__)

.. code-block:: python

    root_agent = RemoteA2aAgent(
        name="Hello_World_Agent",
        agent_card="http://0.0.0.0:9999/.well-known/agent.json",
    )

デモ：ローカル（人）からリモートにメッセージを送信
------------------------------------------------------------

* 注：発表の範囲外ですが、*タスク* という概念があります（時間のかかる処理。たぶんメッセージよりも大事）

**プロトコル** ということは
======================================================================

* フレームワークによらない
* プログラミング言語によらない（Python以外）

a2a-sdkを使わない例（**FastAPI** 実装）
------------------------------------------------------------

これでもメッセージをやり取りできます！

まとめ🌯：Pythonで Agent2Agent Protocol
======================================================================

* A2Aは **リモートエージェント** と **ローカルエージェント** のやり取りのためのプロトコル
* Pythonには a2a-sdk がある
* ADKなどフレームワークでもサポートが進む（`PydanticAI <https://ai.pydantic.dev/a2a/>`__）

以上、nikkie（にっきー）でした！
======================================================================

* 機械学習エンジニア・`Speeda AI Agent <https://www.uzabase.com/jp/info/20250630/>`__ 開発（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）
* みんなのPython勉強会 スタッフ・4代目LT王子

.. image:: ../_static/uzabase-white-logo.png

Thank you for your attention!

Appendix（拙ブログ記事）
======================================================================

* `a2a-samplesのPython Hello World Exampleを動かす <https://nikkie-ftnext.hatenablog.com/entry/agent2agent-protocol-sample-hello-world-python-server-and-client>`__
* `Hello World Example相当のA2AサーバをFastAPIで再現する <https://nikkie-ftnext.hatenablog.com/entry/a2a-hello-world-sample-try-compatible-fastapi-implementation>`__
* `Agent Development Kit 1.6.1 でA2Aが実験的にサポートされました！その中の RemoteA2AAgent を触る <https://nikkie-ftnext.hatenablog.com/entry/google-adk-161-experimental-a2a-support-remotea2aagent-practice>`__
