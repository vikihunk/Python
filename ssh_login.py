''' This script can be used to login to a remote host
    and if the host is unreachable an error can be reported.
    With python ssh package it is easy to handle this scenario but many things are hindden in that pkg implementation
    This function returns the spawned child process' ID and the status whether the ssh was successful or not'''

def ssh_login(hostname):
    #login to the remote machine
    SSH_CMD = 'ssh ' + USER + '@' + hostname
    print 'ssh_cmd: ', SSH_CMD
    child = pexpect.spawn(SSH_CMD)
    try:
        i = child.expect(["password:","continue connecting (yes/no)?"], timeout = 10)
        if i == 0:
            child.sendline (PASSWRD)
        elif i == 1:
            child.sendline ('yes')
            child.expect ('password:')
            child.sendline (PASSWRD)
    except pexpect.EOF:
        print 'EOF'
        print 'Unable to login to ', hostname
        return child, FAILED
    except pexpect.TIMEOUT:
        print 'timeout'
        print 'Unable to login to ', hostname
        return child, FAILED

    child.expect(BASH_PROMPT)
    return child, PASSED
