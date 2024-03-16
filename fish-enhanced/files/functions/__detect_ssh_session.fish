function __detect_ssh_session
    if set -q SESSION_TYPE
        return 0
    end
    if [ -n "$SSH_CLIENT" ] || [ -n "$SSH_TTY" ]
        set -g SESSION_TYPE remote/ssh
    else
        # Traverse the process tree to determine the session type
        # We might be using ssh but, we lost environment variables
        # This might happen when using sudo/su
        set -l fish_ppid $fish_pid
        while test $fish_ppid -gt 1
            set fish_ppid (ps -o ppid= -p $fish_ppid | string trim)
            echo (ps -o comm= -p $fish_ppid)
            switch (ps -o comm= -p $fish_ppid)
                case sshd
                case '*/sshd'
                    set -g SESSION_TYPE remote/ssh
                    return 0
                case 'systemd'
                    set -g SESSION_TYPE local
                    return 0
            end
        end
        set -g SESSION_TYPE local
    end
end
