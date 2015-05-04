---
layout: post
title:  "List the directory in bash"
date:   2015-04-18 19:30:27
categories: bash
permalink: /list-dir-bash
---

A simple enough problem right?

    ls

Okay but what if you want to parse this as part of a script? You run into problems. `ls` [should never be parsed](http://mywiki.wooledge.org/BashPitfalls#for_i_in_.24.28ls_.2A.mp3.29) as it's output is intended to be read by a human, its can differ from machine to machine and `ls` will cause files with spaces to be iterated per token due to [word splitting](http://mywiki.wooledge.org/WordSplitting). The latter problem is also true of `find`. e.g.

    curdir/
        some file.py
        some other file.py

Runing the following:

    for i in $(find . -iname '*.py'); do echo "$i"; touch "$i"; done

Results in some new files being created (`some`, `file.py`, `other`) and the files we actually wanted to touch were not touched!

A safe way to do this would be to use bash's native [file globbing](http://mywiki.wooledge.org/glob):

    for i in *.py; do echo "$i"; touch "$i"; done

And if you need to do this recursively, there are [several ways](http://stackoverflow.com/questions/7039130/bash-iterate-over-list-of-files-with-spaces) but I like this one best:

    while IFS= read -d $'\0' -r file ; do
            printf 'File found: %s\n' "$file"
    done < <(find . -iname '*.py' -print0)



