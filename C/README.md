# catloc

***cat** file from specific **loc**ation within the file*

As I wanted to analyse huge log files once per minute, I needed a way 
to read the newly appended data quickly. 

I wrote this small C program to use the seek fucntion to seek to the end of a file, then captured that location, and then 'cat' the log file from this location on the next invocation one minute later.



