:ogp_title: fzfと履歴の話
:ogp_event_name: terminal-night1
:ogp_slide_name: fzf-happy-history
:ogp_description: Terminal Night #1
:ogp_image_name: terminal-night1

======================================================================
fzfと履歴の話
======================================================================

:Event: Terminal Night #1
:Presented: 2025/11/28 nikkie

お前、誰よ（自己紹介）
======================================================================

* macOS 14.5
* Windsurf 1.12.36 (VS Code系)
* zsh 5.9 (x86_64-apple-darwin23.0)
* fzf 0.67.0 (Homebrew)

あなたの履歴は **幸せ** ですか？
======================================================================

私は、幸せ 🎁（デモ）
------------------------------------------------------------

:kbd:`Ctrl` - :kbd:`R`

.. image:: ../_static/terminal-night1/fzf-happy-history.png

※ **個人の感想** です

.. python を入力する例

:file:`~/.zshrc` [#fzf_key_article]_
------------------------------------------------------------

.. code-block:: bash

    source <(fzf --zsh)

https://github.com/junegunn/fzf?tab=readme-ov-file#setting-up-shell-integration

.. [#fzf_key_article] 拙ブログ `Ctrl + R の履歴を fzf で幸せにする（zsh, bash） <https://nikkie-ftnext.hatenablog.com/entry/fzf-makes-developers-happy-ctrl-r-history-example>`__

:kbd:`Ctrl` - :kbd:`R` だけでなく 🎁
------------------------------------------------------------

* :kbd:`Ctrl` - :kbd:`T`
* :kbd:`Alt` - :kbd:`C`

https://github.com/junegunn/fzf?tab=readme-ov-file#key-bindings-for-command-line

fzfはどんな実装をして、:kbd:`Ctrl` - :kbd:`R` で私を幸せにしてくれている？
================================================================================

https://github.com/junegunn/fzf/blob/v0.67.0/shell/key-bindings.zsh

シェルは知らないことが多い身ですが、実装を一部読んできました

:command:`bindkey`
======================================================================

.. code-block:: bash

    bindkey -M emacs '^R' fzf-history-widget
    bindkey -M vicmd '^R' fzf-history-widget
    bindkey -M viins '^R' fzf-history-widget

https://github.com/junegunn/fzf/blob/v0.67.0/shell/key-bindings.zsh#L162-L164

.. revealjs-break::

* 10月の `神楽坂第1ターミナル <https://kagurazaka-terminal.connpass.com/event/370095/>`__ [#second_terminal]_ で、もずますさんに教わった ``bindkey`` だ！
* https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#index-binding-keys
* ``-M`` で `keymap <https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Keymaps>`__ 指定

.. [#second_terminal] 12/15(月) `神楽坂第2ターミナル <https://kagurazaka-terminal.connpass.com/event/377098/>`__ 楽しみですね

``fzf-history-widget`` の実装
======================================================================

.. code-block:: bash

    FZF_DEFAULT_OPTS=$(__fzf_defaults "" "-n2..,.. --scheme=history --bind=ctrl-r:toggle-sort,alt-r:toggle-raw --wrap-sign '\t↳ ' --highlight-line ${FZF_CTRL_R_OPTS-} --query=${(qqq)LBUFFER} +m")

https://github.com/junegunn/fzf/blob/v0.67.0/shell/key-bindings.zsh#L143

``fzf`` :command:`--highlight-line` 🎁
----------------------------------------------------------------------

細かな違い ``fzf`` vs ``fzf --highlight-line``

    Highlight the whole current line

``fzf`` :command:`+m`
----------------------------------------------------------------------

``+m``, ``--no-multi``

    Disable multi-select

``fzf`` :command:`--nth`
------------------------------------------------------------

.. code-block:: bash

    fzf -n2..,..

* FIELD INDEX EXPRESSION

.. revealjs-break::

* ``2..``    From the 2nd field to the last field
* ``..``     All the fields

historyの1列目を検索対象に含めないと思ったが、 *全列含めている* （``-n ..`` だけでよい？）

``fzf`` :command:`--query=${(qqq)LBUFFER}` 🎁 [#zsh_qqq_article]_
--------------------------------------------------------------------------------

* コマンドを打っている途中の :kbd:`Ctrl` - :kbd:`R` もサポート

.. python -> Ctrl + R

.. [#zsh_qqq_article] 拙ブログ `Zsh 向けのスクリプトに見つけた qqq って、何？ <https://nikkie-ftnext.hatenablog.com/entry/what-is-qqq-zsh-parameter-expansion-flag-q>`__

scoring scheme
------------------------------------------------------------

* default
* path
* **history**

    suited for command history or any input where chronological ordering is important.

``--bind`` (KEY/EVENT BINDINGS)
----------------------------------------------------------------------

    Each binding expression is **KEY:ACTION** or **EVENT:ACTION**.

.. code-block:: bash

    --bind=ctrl-r:toggle-sort,alt-r:toggle-raw

``--bind`` (KEY/EVENT BINDINGS) 🎁
----------------------------------------------------------------------

* :kbd:`Ctrl` - :kbd:`R`: toggle-sort（scoringの昇順降順入れ替え）
* :kbd:`Alt` - :kbd:`R`: toggle-raw（queryにマッチしない項目も表示）

    toggle raw mode for displaying non-matching items

まとめ🌯 fzfと履歴の話
======================================================================

* :command:`fzf --zsh` などを使って、あなたの履歴はより幸せになれます！
* Z Shell分からないなりに実装を読むの楽しい。 ``fzf`` のオプションいくつも知れた🙌

ご清聴ありがとうございました [#fzf_special_thanks]_  (**Happy** development!)
------------------------------------------------------------------------------------------

* nikkie（にっきー）・Python使い・:fab:`github` `@ftnext <https://github.com/ftnext>`__ `sphinx-deck <https://github.com/ftnext/sphinx-deck>`__ など
* 機械学習エンジニア。 `Speeda AI Agent <https://www.uzabase.com/jp/info/20250901/>`__ 開発（`We're hiring! <https://hrmos.co/pages/uzabase/jobs/1829077236709650481>`__）

.. image:: ../_static/uzabase-white-logo.png

.. [#fzf_special_thanks] Special thanks: ``fzf --zsh`` を教えてくださった同僚Aさん

.. --wrap-sign
