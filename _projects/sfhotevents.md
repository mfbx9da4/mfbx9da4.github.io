---
layout: project_phantom
title:  "San Francisco Hot Events"
technologies: [javascript, algolia, meetup.com]
date:   2018-02-01
image: "/assets/img/projects/sfhotevents.png"
categories: project
permalink: /sfhotevents
project_link: http://sfhotevents.ml
github_link: https://github.com/mfbx9da4/hotevents
order: "0.2"
---

## What?
Lists events in San Francisco using meetup.com API. Allows filtering by events which are almost full, are popular, have food, have drinks or are of a particular category.

## Why?
While in San Francisco I found that I missed out on a bunch of great events as they were already at full capacity. I found meetup.com to be quite noisy and lacking features so I implemented a better interface.

## How?
A periodic lambda job on AWS polls the meetup.com API and updates an index on Algolia. The frontend to the webapp is hosted on AWS cloudfront / S3 and connects to algolia.

