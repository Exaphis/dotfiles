case `uname` in
Darwin)
    # home systems - Mac or Manjaro
    export ZSH_HOME="yes"

    export GUILE_LOAD_PATH="/opt/homebrew/share/guile/site/3.0"
    export GUILE_LOAD_COMPILED_PATH="/opt/homebrew/lib/guile/3.0/site-ccache"
    export GUILE_SYSTEM_EXTENSIONS_PATH="/opt/homebrew/lib/guile/3.0/extensions"

    alias ipython3=ipython

    . "$HOME/.cargo/env"
    ;;
Linux)
    if cat /etc/os-release | grep 'Manjaro' > /dev/null; then
        export ZSH_HOME="yes"
    fi

    # set PATH so it includes user's private bin if it exists
    if [ -d "$HOME/bin" ] ; then
        PATH="$HOME/bin:$PATH"
    fi
    if [ -d "$HOME/.local/bin" ] ; then
        PATH="$HOME/.local/bin:$PATH"
    fi

    export EDITOR="vim"
    export DEBEMAIL="kevin@kevinniuwu.com"
    ;;
esac

# enable addons if on home system, disable if anywhere else
if [[ -v ZSH_HOME ]]; then
    export VIM_ENABLE_ADDONS="yes"
fi
