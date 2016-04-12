---
layout: project
title:  "Language tool / Anagram solver"
image:  "/assets/img/projects/language-tool-screenshot.png"
technologies: [angularjs, python]
date:   2015-05-01
categories: project
project_link: http://mfbx9da4.github.io/projects/Word-tree/static/
github_link:  https://github.com/mfbx9da4/Word-tree
permalink: /language-tool
---

Often people learning a foreign language have problems remembering the difference between similarly spelt or similarly sounding words.
This project aims to help people disambiguate similarly spelt words via two main functions.  

Firstly, it organizes the dictionary by word prefix and displays it in a tree format. Technically known as a [Trie data structure](https://en.wikipedia.org/wiki/Trie). Navigating the tree to a leaf word will fetch the wikipedia page for that particular word.  

Secondly, it efficiently computes all anagrams for all words in linear time and space to the number of words.  

The project uses python for the word analysis and angularjs on the frontend.  It was used successfully by my girlfriend in several private english lessons that she taught.  


