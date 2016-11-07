'''
Sept 27 2016

So while I did call this "SimpleCodeHelper4", I'm not sure if it will actually be all that simple.

The difference with this one is that it will edit your program as you go.

You trigger it to respond to some keywords or something, and then type your command where you want it,...
and then it goes through and edits it to be how you want.

For example, the classic "for" problem. This time, you type

for(3) #zh

Where #zh is the keyword it looks for, and it replaces all that with

for(int i = 0; i < 3; i++){

}

or something like that, and then adds 

"for(3) #interpreted and edited"

to a log file.

So, main questions:
Does this thing keep track of your past at all and make decisions based on that,...
or is it merely a static compiler that just helps you type faster?

The first version should probably just be a static compiler.

'''