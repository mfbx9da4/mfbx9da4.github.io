---
layout: post
title:  "Iterating files in bash, the right way"
date:   2015-04-20 19:30:27
categories: bash
permalink: /list-dir-bash
---

Many people might jump to

    ls

Okay but what if you want to parse this as part of a script? You run into problems. The output of `ls` [should never be parsed](http://mywiki.wooledge.org/BashPitfalls#for_i_in_.24.28ls_.2A.mp3.29) as it is intended to be read by a human. The output of `ls` can differ from machine to machine and parsing `ls` can result in files with spaces to be iterated per word token due to [word splitting](http://mywiki.wooledge.org/WordSplitting) on white space. Okay, so parse output of `find`? Well, the latter problem is also true of `find`.

For example, given a directory structure as follows:

    curdir/
        some file.py
        some other file.py

Running the following:

    for file in $(find . -iname '*.py'); do
    	echo "$file"
    	touch "$file"
	done

Results in some new files being created (`some`, `file.py`, `other`) and the files we actually wanted to touch were not touched!

A safe way to do this would be to use bash's native [file globbing](http://mywiki.wooledge.org/glob):

    for file in *.py; do
    	echo "$file"
    	touch "$file"
	done

However, if you need to do this recursively or need to use `find`, simple file globbing cannot be used. Instead, you could just pipe the output of `find`.


	find . -iname "*.py" | while read f
	do
	    echo "$f"
	    touch "$f"
	done


However, in bash each command of a [pipeline is executed in a separate SubShell](http://mywiki.wooledge.org/BashFAQ/024) therefore any variable modification will be lost inside while read. (Btw not the case in [zsh](http://www.zsh.org/)).

For example:

	i=0
	find . -iname "*.py" | while read f
	do
	    echo "$f"
	    touch "$f"
	    i=$(($i + 1))
	done
	echo "$i" # Will output 0

To resolve this we must use [process substitution](http://mywiki.wooledge.org/ProcessSubstitution) as so:

	while read file; do
		echo "$file"
		touch "$file"
	done < <(find . -iname '*.py')

<!-- i=0; while read file; do echo "$file"; touch "$file"; i=$(($i + 1)); done < <(find . -iname '*.py'); echo "$i" -->


As a final edge case, filenames could have new line characters in which case we should [split on the null character](http://stackoverflow.com/questions/7039130/bash-iterate-over-list-of-files-with-spaces) as so:


    while IFS= read -d $'\0' -r file ; do
            echo "$file"
            touch "$file"
    done < <(find . -iname '*.py' -print0)
