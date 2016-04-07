---
layout: project
title:  "Real Time Scoreboard"
image:  "/assets/img/projects/scoreboard-screenshot.png"
technologies: [expressjs, angularjs, nodejs, mysql, web-sockets]
date:   2016-02-01
categories: project
project_link: http://volleyball-scoreboard.herokuapp.com
permalink: /scoreboard
order: "2"
---

My client required a real-time scoreboard platform for a volleyball competition. The web app development had been started and I was required to finish it off. The web app has three main users:  

1. Admin: schedules, starts and pauses volleyball matches to several different courts. 
2. Referee: Linked in real-time to admin manipulation of running matches e.g. starting match, pausing match, playing buzzer, score updates. Referees are also able to update scores. 
3. Public: A public view which is able to view but not update match in real-time.   


The web stack included node, MySQL, socket.io and angular. I implemented the following functionality:  

1. CRUD REST api for matches, teams and courts.
2. Deployed and maintained linux server.
3. NTP-like server-browser clock synchronization for synchronized timers between admin, referee and public views. 
4. Start, stop, timeout, half time timer functionality linked in real-time across. 
5. Cross-device real-time buzzer functionality. 
6. Cross-device real-time scoring system. 
7. Some style changes for responsivity.  


The code was used intensively for several weeks without any major bugs in a large volleyball competition involving thousands of games.
