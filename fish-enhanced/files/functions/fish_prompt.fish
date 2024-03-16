function fish_prompt --description 'Informative prompt'
    #Save the return status of the previous command
    set -l last_pipestatus $pipestatus
    set -lx __fish_last_status $status # Export for __fish_print_pipestatus.

    set -l status_color (set_color $fish_color_status)
    set -l statusb_color (set_color --bold $fish_color_status)
    set -l pipestatus_string (__fish_print_pipestatus "[" "] " "|" "$status_color" "$statusb_color" $last_pipestatus)

    # add empty string if pipestatus_string is empty
    set -l pipestatus_string (test -z "$pipestatus_string"; and echo ""; or echo "$pipestatus_string")

    # If we're running via SSH, change the host color.
    set -l color_host $fish_color_host
    if set -q SSH_TTY; and set -q fish_color_host_remote
        set -l color_host $fish_color_host_remote
        if functions -q fish_is_root_user; and fish_is_root_user; and set -q fish_color_host_remote_root
            set -l color_host $fish_color_host_remote_root
        end
    end

    if functions -q fish_is_root_user; and fish_is_root_user
        printf '%s%s%s %s%s %s%s# ' $pipestatus_string (set_color --bold $color_host) \
            (prompt_hostname) (set_color --bold $fish_color_cwd) (prompt_pwd) \
            (set_color --bold $fish_color_cwd)
    else
        printf '%s%s%s@%s%s %s%s %s%s$ ' $pipestatus_string (set_color --bold green) \
            $USER (set_color --bold $color_host) (prompt_hostname) (set_color --bold $fish_color_cwd) (prompt_pwd) \
            (set_color --bold $fish_color_cwd)
    end
end
