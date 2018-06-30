---
layout: project_phantom
title:  Email Scraper
technologies: [javascript]
date:   2016-12-01
image: "/assets/img/projects/email-scraper.png"
categories: project
permalink: /email-scraper
project_link: http://ec2-18-130-131-194.eu-west-2.compute.amazonaws.com/
github_link: https://github.com/mfbx9da4/scrape_email
order: "0.2"
---

## What?
Given a query or a spreadsheet of queries returns possible email addresses. The tool works by googling for the given query, opening the first 10 results and scraping the web pages for email addresses.
## Why?
While building an outbound B2B email marketing campaign I needed to find email addresses for a list of leads. Instead of googling each individual query I decided to automate the process. As this is a common use case I decided to automate the process.
## How?
The scraper runs on AWS EC2 as a docker container with a nodeJS backend written with ES6+ syntax. The backend makes requests to google and sub pages in parallel and updates the progress of the query using websockets to the frontend.
