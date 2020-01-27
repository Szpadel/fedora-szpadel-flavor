if ! command -v vim &> /dev/null && command -v nvim &> /dev/null;then
    # we have veovim installed and there is no vim
    alias vim=nvim
fi
