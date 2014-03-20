#!/usr/bin/env ruby
 
unless ARGV[0]
  puts "Usage: newpost post-title"
  exit(-1)
end
 
date_prefix = Time.now.strftime("%Y-%m-%d")
postname = ARGV[0].strip.downcase.gsub(/ /, '-')
 
header = <<-END
---
layout: post
title: "#{ARGV[0]}"
---
 
h1. {{ page.title }}
 
END
 
f = File.open("/Users/al3x/src/al3x.github.com/_posts/#{date_prefix}-#{postname}.textile", 'w+')
f << header
f.close
 
system("#{ENV['VISUAL']} #{f.path}")
exit(0)
