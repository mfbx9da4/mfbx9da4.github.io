---
layout: project
title:  "Real Time Scoreboard"
image:  "/assets/img/projects/scoreboard.png"
technologies: [expressjs, angularjs, nodejs, mysql, web-sockets, socket.io]
date:   2016-02-01
categories: project
project_link: http://volleyball-scoreboard.herokuapp.com
permalink: /scoreboard
order: "5.1"
---

My client required a real-time scoreboard platform for a volleyball competition. The scoreboard, timer and buzzer were required to be synchronized across several devices in real-time. The web app development had been started and I was required to finish it off. 

I implemented the following functionality:  

1. CRUD REST api for matches, teams and courts.
2. Deployed and maintained linux server.
3. NTP-like server-browser [clock synchronization library](/ng-server-time). 
4. Cross-device real-time timer functionality. 
5. Cross-device real-time buzzer functionality. 
6. Cross-device real-time scoring system. 
7. Some style changes for responsivity.  


The code was successfully used intensively for several weeks in a large national volleyball competition involving thousands of games.
