if ! command -v yarn &> /dev/null && command -v yarnpkg &> /dev/null;then
    # nodejs yarn was instralled in system and it uses yarnpkg name
    # we also do not have anything named yarn, therefore we alias it to use yarn command
    alias yarn=yarnpkg
fi
