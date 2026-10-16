---
# SPDX-FileCopyrightText: © 2026 hazzuk
#
# SPDX-License-Identifier: AGPL-3.0-only

icon: lucide/folder-git-2
---

# Git changes

## Commit changes

Having made local changes to your `karo-inventory` repo,
you'll need to 'commit' and 'push' the new changes.
Ensuring your server's configuration is synced with your remote GitHub repository.

``` sh
# commit inventory changes
cd /srv/karo/inventory
git add *
git commit -m "update inventory files"
git push
```

!!! info "SSH key prompts"

    Your desktop password manager might prompt you when running git commands.
    Using both your SSH signing key, to sign your git commits.
    And SSH auth key, to authenticate access with your remote repository.

You should repeat these commands after making any new substantial changes to your repository.
