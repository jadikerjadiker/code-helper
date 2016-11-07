Format 0.0 Definiton (date: around Dec 15th, 2015):
    
The format needs to be in this form (hashtags symbolize a comment that is not a part of the form):
Version 0.0 #the version number to let the computer know what version of a file it's reading. This can be any case with any whitespace as long as it's completely on the first line.
#up until the formatend line, you can have as many newlines as you want between lines.
#for all of these defining symbols things (up until the endformat line) if there is no ending symbol (referred to as "symbol to recognize end of...), the ending symbol is assumed to be a newline.
Item Name Symbol:Item Name:#this is in the form "(whatever you want to call the names for your items(#referred to as A1) Symbol(#uppercase or lowercase):(Symbol to recognize the start of a new item name)(A1)(Symbol to recognize end of new item name)"
Item Symbol:Item#this is in the form "(whatever you want to call your items(#ref A1)) Symbol(#any case):(symbol to recognize a new item)(A1)(symbol to recognize the end of the new item)"

Top Section Title Symbol:$$ Top Section Title $$#this is in the form "(whatever you want to call your top section titles(#ref A1)) Symbol(#any case):(symbol to recognize a new highest-level section title)(A1)(symbol to recognize the end of the new top section title)"
Second-Level Sect Title symbol:!!! Second-Level Sect Title#this is in the form "(whatever you want to call your next-level-down section titles(#ref A1)) Symbol(#any case):(symbol to recognize this new title)(A1)(symbol to recognize the end of the title)"
Third-Level Sect Title symbol:Second-Level Sect Title@@@#this is in the form "(whatever you want to call your next-level-down section titles(#ref A1)) Symbol(#any case):(symbol to recognize this new title)(A1)(symbol to recognize the end of the title)"
#this can be continued on for as many subsections as you want to organize your vaiables and data.
Format End#form:"formatend(#anycase, anyspacing)" so it could be "form AtE  nD"
#anything in between this and the next comment is just ignored
Woohoo! Let us party!
We have some free time here to show our inner selves.
_____________
-------------
_____________ just to show you that this is actually being ignored

Info Start #this line starts the info. Form: "infostart(#anycase, anyspacing)"
$$ The Large Section $$ #created a big section to help divide info
!!!Here is a smaller section#a smaller section to divide it into simpler parts
The Beast:#the name of an item
Jim#the actual item. So if you were to search for "The Beast" you should get back "Jim"
The Cow:
Joe

!!!Here is a more normal section#this is still within the section called "The Large Section"
Other Characters@@@#this is that even smaller section that goes inside the medium-sized one above it
The House:#this is the name of an item
James the House #this is the actual item

The Mouse:
Jason the Mouse

#heres's a better example of how it could be used
$$ Another Large Section $$
!!!Operators
Basic Algebra@@@
Plus:
+
Minus:
-
Divide:
/
Multiply:
*
Comparisons@@@
Less Than:
<

Greater Than:
>

Equal To:
==

#somthing you can't do (which I may make a new format for) is "Title Of Item:\n(start symbol)\n(Item that takes up more than one line)\n(end symbol)" because the newlines will be counted in the item.
#Also can't do "Title Of Item:(start symbol)(item)(end symbol)" (you need the "\n" after the "Title Of Item:\n". The main reason for this is human readability... But I don't think it would hurt that much to allow it. This suffices for now.
