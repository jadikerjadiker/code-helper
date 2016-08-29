'''
The top line should start with "Protocol" or "protocol" with a code afterwards (it will strip all whitespaces in the first line first)
The protocal code tells the SymbolPageReader how to read (or if it even can) read the page.

Then, for Format 0.0 (this first format I'm making) it will look for the symbols that represtent sections and subsections.
It will keep on searching for more sections and subsections until reaching "formatend" (lowercased and whitespace-stripped)
And then it will mark that line as the end of format line (in an attribute) so that searches can start from there.

Might add a bit of caching in the reader, not sure exactly how much speed it will add though... I don't exactly expect these files to be huge.

Decided to call it "format" instead of "protocol"; it's simpler to type, easier to remember, and makes more sense...
This was edited in most of the above writing.

Now (11/23/2015) I'm going to add in another line that is "infostart" (lowercased and whitespace-stripped)...
to mark the start of the info. It should come after format end and any other symbols like...
"--------------" that humans want to use to space out the format from the info.
'''