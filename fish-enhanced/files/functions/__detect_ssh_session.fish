function __detect_ssh_session
    if set -q SESSION_TYPE
        return 0
    end
    if [ -n "$SSH_CLIENT" ] || [ -n "$SSH_TTY" ]
        set -g SESSION_TYPE remote/ssh
    else
        set -l fish_ppid (ps -o ppid= -p $fish_pid | string trim)
        switch (ps -o comm= -p $fish_ppid)
            case sshd
            case '*/sshd'
                set -g SESSION_TYPE remote/ssh
            case '*'
                set -g SESSION_TYPE local
        end
    end
end
