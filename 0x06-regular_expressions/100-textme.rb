#!/usr/bin/env ruby
print ARGV[0].scan(/(?<=from:)(\w+|\+?\d{11})/).join
print ","
print ARGV[0].scan(/(?<=to:)(\w+|\+?\d{11})/).join
print ","
puts ARGV[0].scan(/(?<=flags:)(-?\d:-?\d:-?\d:-?\d:-?\d)/).join
