'''
5/16/2016

Okay, so I have a lot of different thoughts on this project, and I just wanted to get them out in a form where it can be referenced later.

The whole idea of this is that all tasks can be broken down into subtasks which can then be broken down and so on into tasks that a computer does know how to do.
The hard part is breaking them down, so we have the human do that part until it gets to something the computer understands.

This "something" is what I call "base code". It's whatever language the computer can understand - it can inherently execute base code without any ambiguity.

The issue with this that I just realized, is that certain patterns, such as loops, cannot be "broken down". This goes for any flow control, really.

Also, humans tend to talk in a form that has actions operating on objects.
If the computer learns how to do an action, it seems normal that it should be able to apply that action to any object, just like a function with parameters.

Just breaking down tasks also does not take that into account.
So, I'm going to do some more brainstorming in order to try to come up with a way that can be programmed easily to do all of this: functions with parameters, break down tasks, and understand flow.
'''

'''
5/16/16

Just wrote out in pencil and paper my new thoughts.
Overall:
Python can already do all of this. What it doesn't do is interact with the user or have a shell (a place where you can just type commands and have them excecuted within the environment)

So I'm just going to build a shell that will actually help me use the power of Python.
I'm also going to switch to Python 3, just because it seems like it's actually becoming popular and being picked up.
And there are some more elegant solutions to problems I've researched if you are using Python 3.


OOHHH There was something big I was missing: customizeability. Code Helper is huge on being able to write whatever you want and having it conform.
What if I don't like parentheses for functions. Well then, I just change it to brackets. No biggie.

That's what I want to change: how the code is intepreted depends on a settings file that can be easily accessed.
I'm going to try to incorporate this idea into how I code the shell (probably by making a bunch of variables at the top), but if it's too complicated I'm going to drop it.
'''

'''
5/17/16

Okay, now I at least have an idea as to how everything will be set up.

I'm going to define environments, which is basically a box of commands and properties that can be loaded.
The Shell will have its own environment with pre-defined commands and the ability for users to define new commands for the shell environment.
What was previously called "projects" is now actually just an external environment.
Methods from external environments only have read access, but they can access both info from the shell environment and their own.
Certain unmodifiable pre-defined commands in the shell will have write access to environments.
When you type something into the shell, it will first check its own pre-defined commands, then its external environment, then its internal user-defined commands.
If it sees one that matches, it will run it. Otherwise, it will print an error message or something like that.

As for coding these environments, they're just classes. Whenever an environment is modified, its reloaded by the shell.
This has already been tested and it works.

So I'm not going to deal with frameworks right now, just make a shell that allows me to load external environments, use them, and reload them.
Then, I'll add functions to have the shell edit those environmnets from within the GUI

One module may hold many environments.
'''