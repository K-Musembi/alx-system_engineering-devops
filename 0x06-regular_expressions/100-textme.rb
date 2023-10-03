#!/usr/bin/env ruby
#puts ARGV[0].scan(/\[from:(.*?)\],\[to:(.*?)\],\[flags:(.*?)\]/).join

sender = ARGV[0].match(/\[from:(.*?)\]/)[1]
receiver = ARGV[0].match(/\[to:(.*?)\]/)[1]
flags = ARGV[0].match(/\[flags:(.*?)\]/)[1]

puts "#{sender},#{receiver},#{flags}"
