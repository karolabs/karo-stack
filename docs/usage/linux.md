---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: simple/linux
---

# Linux

The following is a list of essential commands and shortcuts for using a Linux server.

!!! info "Note for Windows users"

    File and directory name are case-sensitive on Linux. It's highly recommended to adopt the habit of using lowercase letters for file and directory names.

    - `NewFile.txt` :lucide-circle-x:
    - `newfile.txt` :lucide-circle-check:

## Terminal

-   **Copy** selected terminal text

    ++ctrl+shift+c++

-   **Paste** clipboard into the terminal

    ++ctrl+shift+v++

-   **Recall** commands from shell history

    ++arrow-up++ or ++arrow-down++

-   **Autocomplete** file, directory, and command names

    ++tab++

## Remote Access

-   **SSH** [:lucide-sticky-note:](https://linuxize.com/cheatsheet/ssh/)

    ``` sh
    # connect to a remote server
    ssh -A karo@homeserver.example.com
    ```

## Shell session

-   **Exit**

    ``` sh
    # close shell session
    exit
    ```

-   **History**

    ``` sh
    # show previous commands
    history
    ```

## Files and directories

-   **Change directory** [:lucide-sticky-note:](https://linuxize.com/cheatsheet/cd/)

    ``` sh
    # to specific directory
    cd /srv/karo/roles
    ```

    ``` sh
    # to parent directory
    cd ..
    ```

    ``` sh
    # to previous directory
    cd -
    ```

-   **List view** [:lucide-sticky-note:](https://linuxize.com/cheatsheet/ls/)

    ``` sh
    # show directory contents
    ls -a
    ```

-   **Tree view**

    ``` sh
    # show contents of multiple directories
    tree -L 2
    ```

-   **Metadata**

    ``` sh
    # show file info
    stat file.txt
    ```

-   **Create directories**

    ``` sh
    # create directory
    mkdir newdir
    ```

    ``` sh
    # create parent directories
    mkdir -p path/to/newdir
    ```

-   **Move / rename** [:lucide-sticky-note:](https://linuxize.com/cheatsheet/mv/)

    ``` sh
    # move file
    mv file.txt /path/to/destination/
    ```

    ``` sh
    # rename file
    mv oldname.txt newname.txt
    ```

-   **Copy** [:lucide-sticky-note:](https://linuxize.com/cheatsheet/cp/)

    ``` sh
    # copy file
    cp file.txt /path/to/destination/
    ```

-   **Delete** [:lucide-sticky-note:](https://linuxize.com/cheatsheet/rm/)

    ``` sh
    # remove file
    rm file.txt
    ```

## Text files

-   **File viewer** [:lucide-sticky-note:](https://linuxize.com/cheatsheet/less/)

    ``` sh
    # view file
    less file.txt
    ```

-   **Text editor**

    ``` sh
    # create/edit file
    micro file.txt
    ```

## System

-   **Monitoring**

    ``` sh
    # view system usage
    btop
    ```

-   **Disk Usage** [:lucide-sticky-note:](https://linuxize.com/cheatsheet/df/)

    ``` sh
    # show disk usage
    df -h -x tmpfs
    ```

-   **Services** [:lucide-sticky-note:](https://linuxize.com/cheatsheet/systemctl/)

    ``` sh
    # show service status
    sudo systemctl status nftables
    ```

-   **Logs** [:lucide-sticky-note:](https://linuxize.com/cheatsheet/journalctl/)

    ``` sh
    # view system logs
    sudo journalctl
    ```

-   **Shutdown**

    ``` sh
    # power off system
    sudo shutdown now
    ```

-   **Reboot**

    ``` sh
    # restart system
    sudo reboot
    ```

## Networking

-   **Ping** [:lucide-sticky-note:](https://linuxize.com/cheatsheet/ping/)

    ``` sh
    # ping network host
    ping example.com
    ```

    ``` sh
    # ping ip address
    ping 192.168.0.1
    ```

## More help

-   **Manuals**

    ``` sh
    # view command manual
    man micro
    ```


-   **Docker** [:lucide-sticky-note:](https://linuxize.com/cheatsheet/docker/)
-   **Shortcuts** [:lucide-sticky-note:](https://github.com/fliptheweb/bash-shortcuts-cheat-sheet)
