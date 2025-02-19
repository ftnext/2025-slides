======================================================================
FastAPIの現場から
======================================================================

ドラフト版

:Event: DjangoCongress JP 2025
:Presented: 2025/02/22🐈 nikkie

お前、誰よ
======================================================================

* 機械学習エンジニア
* 専門は機械学習。プロダクトとして価値を届けるためにAPIの開発もします（今日の話）

.. image:: ../_static/uzabase-white-logo.png

.. privateの自己紹介？

FastAPI、ご存知ですか？
======================================================================

* 聞いたことがある🙋‍♂️
* 使ったことがある🙋‍♀️

私はチームでFastAPIを使っています
--------------------------------------------------

* チュートリアル修了レベルでスタート
* PyConのトークいくつかを手がかりに
* 見聞き -> 作る の中で得た、 **FastAPIの知見を共有** します

.. TODO 手がかり（先人の足跡）

PythonコミュニティにおけるFastAPI
======================================================================

`Python Developers Survey 2023 <https://lp.jetbrains.com/python-developers-survey-2023/#frameworks-and-libraries>`__ より

.. revealjs-break::
    :notitle:

.. TODO 図を持ってこよう

* Flask 33%
* Django 33%
* **FastAPI 29%**
* Django REST Framework 18%

データサイエンスで使われる
--------------------------------------------------

.. TODO 図を持ってこよう

* Flask 36%
* **FastAPI 31%**
* Django 26%

FastAPI
======================================================================

.. code-block:: python
    :caption: Tutorialの `First Steps <https://fastapi.tiangolo.com/tutorial/first-steps/>`__

    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

この延長に機械学習モデルをサーブするAPI

.. 単語としてResNetが登場 https://fastapi.tiangolo.com/tutorial/path-params/

Django REST Framework
--------------------------------------------------

.. code-block:: txt
    :caption: `Quickstart <https://www.django-rest-framework.org/tutorial/quickstart/>`__ にある認証付きAPI

    bash: curl -u admin -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/users/
    Enter host password for user 'admin':
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "url": "http://127.0.0.1:8000/users/1/",
                "username": "admin",
                "email": "admin@example.com",
                "groups": []
            }
        ]
    }

.. _Django vs. FastAPI, An Honest Comparison: https://www.david-dahan.com/blog/comparing-fastapi-and-django

記事 `Django vs. FastAPI, An Honest Comparison`_
------------------------------------------------------------

* Batteries includedか、 **自分で組み合わせる** 必要があるか
* 非同期対応の度合い
* IMO：それぞれ得意分野が異なる

私の現場のFastAPI
======================================================================

.. 技術や組織の前提を最初に紹介しておく

* 社内向けの小さなAPI
* 外部のLLMの **API** を使うアプリケーション
* **非同期IO** が必要ということで、FastAPIを選択（+皆やってみたさ）

XP（eXtreme Programming）
--------------------------------------------------

* アジャイル開発の1手法
* 小さい価値でも届け、そこからの学びを活かすサイクルを何度も何度も回す（**3ヶ月** 経過）
* 最初に全機能設計したわけではない。現場のアプリは小さく始まり、育てている最中（**現時点の最適解**）

デプロイ先はKubernetes
--------------------------------------------------

* FastAPIをコンテナ化
* GKEにデプロイ

非同期IO
======================================================================

* FastAPI
* SQLModel (SQLAlchemy)

.. include:: asynchronous-io/fastapi.rst.txt

クリーンなアーキテクチャを志向する
======================================================================

.. include:: clean-architecture/layers.rst.txt
