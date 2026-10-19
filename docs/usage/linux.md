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

-   **SSH** [:lucide-external-link:](https://linuxize.com/cheatsheet/ssh/)

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

-   **Change directory** [:lucide-external-link:](https://linuxize.com/cheatsheet/cd/)

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

-   **List view** [:lucide-external-link:](https://linuxize.com/cheatsheet/ls/)

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

-   **Move / rename** [:lucide-external-link:](https://linuxize.com/cheatsheet/mv/)

    ``` sh
    # move file
    mv file.txt /path/to/destination/
    ```

    ``` sh
    # rename file
    mv oldname.txt newname.txt
    ```

-   **Copy** [:lucide-external-link:](https://linuxize.com/cheatsheet/cp/)

    ``` sh
    # copy file
    cp file.txt /path/to/destination/
    ```

-   **Delete** [:lucide-external-link:](https://linuxize.com/cheatsheet/rm/)

    ``` sh
    # remove file
    rm file.txt
    ```

## Text files

-   **File viewer** [:lucide-external-link:](https://linuxize.com/cheatsheet/less/)

    ``` sh
    # view file
    less file.txt
    ```

-   **Text editor**

    ``` sh
    # create/edit file
    micro file.txt
    ```

## Storage

-   **Disk usage**

    ``` sh
    # analyse working directory
    gdu
    ```

    ``` sh
    # analyse given path
    gdu /path/to/destination
    ```

    ``` sh
    # ignore paths
    gdu -i /sys,/proc /path/to/destination
    ```

    <!-- requires gdu v5.30.0
    ``` sh
    # show top 3 largest files
    gdu -t 3 /path/to/destination
    ```
    -->

    ``` sh
    # show all mounted disks
    gdu -d
    ```

    ``` sh { title="Coreutils alternative" }
    # show file or directory disk usage
    du -sh /path/to/destination
    ```

-   **Filesystems**

    ``` sh
    # show filesystems
    duf
    ```

    ``` sh
    # filter by given path
    duf /path/to/destination
    ```

    ``` sh { title="Coreutils alternative" }
    # show filesystems disk usage
    df -h -x tmpfs
    ```

## System

-   **Monitoring**

    ``` sh
    # view system usage
    btop
    ```

-   **Services** [:lucide-external-link:](https://linuxize.com/cheatsheet/systemctl/)

    ``` sh
    # show service status
    sudo systemctl status nftables
    ```

-   **Logs** [:lucide-external-link:](https://linuxize.com/cheatsheet/journalctl/)

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

-   **Ping** [:lucide-external-link:](https://linuxize.com/cheatsheet/ping/)

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

-   **Docker** [:lucide-external-link:](https://linuxize.com/cheatsheet/docker/)

-   **Shortcuts** [:lucide-external-link:](https://github.com/fliptheweb/bash-shortcuts-cheat-sheet)
