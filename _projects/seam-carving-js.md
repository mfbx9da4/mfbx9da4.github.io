---
layout: project
title:  "Seam Carver - Image Processing"
image:  "/assets/img/projects/seam-carving-js.png"
technologies: [nodejs, html5canvas, algorithms, gulp, image-processing]
date:   2015-05-01
categories: project
project_link: /seam-carving-js
github_link:  https://github.com/mfbx9da4/seam-carving-js
permalink: /seam-carver
order: "1.1"
---

[Seam carving](https://en.wikipedia.org/wiki/Seam_carving) is an algorithm which implements content-aware image resizing by removing the "least important" seams in the image. An "unimportant" pixel refers to a pixel which is very similar to its surrounding pixels. A seam is like a one pixel column in the image which can zig-zag between adjancent pixels. A dynamic programming algorithm is uesed to calculate these seams efficiently.

Here I reimplement this famous algorithm in the browser! It is rare to see such a complex and powerful image processing algorithm in the browser and challenging to have it run smoothly. I also altered the original implementation to make my own optimization such that only affected pixels need be recalculated when a seam is removed.


