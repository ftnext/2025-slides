slide:
	@uvx --from sphinx \
		--with sphinx-revealjs \
        --with sphinx-design \
		--with sphinx-new-tab-link \
		--with sphinxcontrib-budoux \
		--with sphinxcontrib-mermaid \
		--with sphinx-revealjs-copycode \
		--with sphinx-revealjs-ext-codeblock \
        sphinx-build -M revealjs source build --fail-on-warning

clean:
	@uvx --from sphinx sphinx-build -M clean source build
