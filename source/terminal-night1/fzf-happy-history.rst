======================================================================
fzfと履歴の話
======================================================================

:Event: Terminal Night #1
:Presented: 2025/11/28 nikkie

お前、誰よ（自己紹介）
======================================================================

* macOS 14.5
* zsh 5.9 (x86_64-apple-darwin23.0)
* fzf 0.67.0 (Homebrew)

.. TODO iterm / Windsurf

あなたの履歴は **幸せ** ですか？
======================================================================

私は、幸せ
------------------------------------------------------------

:kbd:`Ctrl` - :kbd:`R`

.. python を入力する例

:file:`~/.zshrc`
------------------------------------------------------------

.. code-block:: bash

    source <(fzf --zsh)

https://github.com/junegunn/fzf?tab=readme-ov-file#setting-up-shell-integration

:kbd:`Ctrl` - :kbd:`R` だけでなく
------------------------------------------------------------

* :kbd:`Ctrl` - :kbd:`T`
* :kbd:`Alt` - :kbd:`C`

https://github.com/junegunn/fzf?tab=readme-ov-file#key-bindings-for-command-line

fzfはどんな実装をして、私を幸せにしてくれている？
======================================================================

https://github.com/junegunn/fzf/blob/v0.67.0/shell/key-bindings.zsh

シェルは知らないことが多い身ですが、読んできました

:command:`bindkey`
======================================================================

.. code-block:: bash

    bindkey -M emacs '^R' fzf-history-widget
    bindkey -M vicmd '^R' fzf-history-widget
    bindkey -M viins '^R' fzf-history-widget

https://github.com/junegunn/fzf/blob/v0.67.0/shell/key-bindings.zsh#L162-L164

.. revealjs-break::

* `神楽坂第1ターミナル <https://kagurazaka-terminal.connpass.com/event/370095/>`__ [#second_terminal]_ で、もずますさんに教わった ``bindkey`` だ！
* https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#index-binding-keys
* ``-M`` で `keymap <https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Keymaps>`__ 指定

.. [#second_terminal] 12/15(月) `神楽坂第2ターミナル <https://kagurazaka-terminal.connpass.com/event/377098/>`__ 楽しみですね

``fzf-history-widget`` の実装
======================================================================

.. code-block:: bash

    FZF_DEFAULT_OPTS=$(__fzf_defaults "" "-n2..,.. --scheme=history --bind=ctrl-r:toggle-sort,alt-r:toggle-raw --wrap-sign '\t↳ ' --highlight-line ${FZF_CTRL_R_OPTS-} --query=${(qqq)LBUFFER} +m")

https://github.com/junegunn/fzf/blob/v0.67.0/shell/key-bindings.zsh#L143

``fzf`` :command:`--highlight-line`
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

historyの1列目を検索対象に含めないと思ったが、 *全列含めている* （``-n ..`` でよい？）

``fzf`` :command:`--query=${(qqq)LBUFFER}`
----------------------------------------------------------------------

* コマンドを打っている途中の :kbd:`Ctrl` - :kbd:`R` もサポート

.. python -> Ctrl + R

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

.. revealjs-break::

* :kbd:`Ctrl` - :kbd:`R`: toggle-sort（scoringの昇順降順入れ替え）
* :kbd:`Alt` - :kbd:`R`: toggle-raw（queryにマッチしない項目も表示）

    toggle raw mode for displaying non-matching items

.. デモで見せる

まとめ🌯 fzfと履歴の話
======================================================================

* :command:`fzf --zsh` などを使って、あなたの履歴はより幸せになれます！
* Z Shell分からないなりに実装を読むの楽しい。 ``fzf`` のオプションいくつも知れた🙌

ご清聴ありがとうございました
------------------------------------------------------------

Happy development!
