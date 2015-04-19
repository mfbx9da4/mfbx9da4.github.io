---
layout: post
title:  "My javascript sublime snippets"
date:   2015-04-07 15:30:27
categories: javascript sublime-snippets sublime snippets
permalink: /javascript-sublime-snippets
---


I use these constantly and they really speed me up! In order of most used


#### console.log()

    <snippet>
        <content><![CDATA[console.log(${1});]]>
        </content>
        <tabTrigger>cons</tabTrigger>
        <scope>source.js</scope>
    </snippet>


####for loop

    <snippet>
        <content><![CDATA[
    for (var ${1:i} = 0; $1 < ${2:array}.length; $1 ++) {
        var $3 = $2[$1];
    }
    ]]></content>
        <!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
        <tabTrigger>for</tabTrigger>
        <!-- Optional: Set a scope to limit where the snippet will trigger -->
        <scope>source.js</scope>
    </snippet>

### closure

    <snippet>
        <content><![CDATA[
    function ($1) {$2}
    ]]></content>
        <!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
        <tabTrigger>f</tabTrigger>
        <!-- Optional: Set a scope to limit where the snippet will trigger -->
        <scope>source.js</scope>
    </snippet>


### for in

    <snippet>
        <content><![CDATA[
    for (var ${1:k} in ${2:obj}) {
        var $3 = $2[$1];
    }
    ]]></content>
        <!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
        <tabTrigger>in</tabTrigger>
        <!-- Optional: Set a scope to limit where the snippet will trigger -->
        <scope>source.js</scope>
    </snippet>


