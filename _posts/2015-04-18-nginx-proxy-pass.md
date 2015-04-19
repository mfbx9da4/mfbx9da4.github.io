---
layout: post
title:  "Nginx proxy pass"
date:   2015-04-18 19:30:27
categories: nginx proxy
permalink: /nginx-proxy-pass
---

A common problem when debugging a client site is being able to load a specific javascript file locally and leave other scripts from that remote host to be loaded from the remote address.

For example:

- I am debugging `client.site.com` which loads some scripts `a.js`, `b.js`, `c.js`, `d.js` amongst other resources.
- I need to debug file `a.js`, therefore I want to modify it locally and serve it locally.
- I could just change my `/etc/hosts` to point to local but then everything including the page itself would have to be downloaded and served locally.
- To avoid this I changed my ngnix config to put a little proxy-pass to redirect all requests back to the remote hose apart from that file, as shown below.




        server {
             listen 80;
             server_name client.site.com;

             location /a.js {
                     # your local server
                     proxy_pass http://localhost:80/;
                     proxy_set_header Host      $host;
                     proxy_set_header X-Real-IP $remote_addr;
             }

             location / {
                     # everything else back to the IP of client.site.com
                     proxy_pass http://<REMOTE_IP>/;
                     proxy_set_header Host      $host;
                     proxy_set_header X-Real-IP $remote_addr;
             }
        }
