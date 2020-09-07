#!/usr/bin/ruby

require 'cgi'
cgi = CGI.new

h = cgi.params
puts cgi.header
puts '<html><body>'
puts '<H1>Work in progress</H1><p>This is a test</p>'


#h.each { |k,v|
#    puts '<p>' << k << '</p>'
#}
if h['name'].to_s.empty?
  puts '<p> I got nothing </p>'
else
  puts '<p> I got ' << h['name'].to_s << ' and ' << h['email'].to_s
  #puts h['name'].to_s << ' ' << h['email'].to_s
  puts '</p>'
end

# unless h['name'].to_s.empty?
#     puts '<p> I got '<< h['name'].to_s <<' </p>'
# end
puts '</body></html>'
