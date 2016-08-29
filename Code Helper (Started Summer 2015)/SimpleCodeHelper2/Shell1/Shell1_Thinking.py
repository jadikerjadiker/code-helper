
'''
5/16/16

What I want from this shell:
Go into the settings and easily change keywords to whatever I want them to be (such as "proj " to "project" in the following example)
Type "proj = python" (which will either respond with a message that says it loaded or that I'm creating a new project)
Type "loop 10" and have it print out a syntactically correct Python loop that would loop 10 times.
Type "proj = java" and then "loop 10" and have it do the same thing for Java - a loop that runs 10 times.

Let's just get that working.
'''

'''
5/16/16
So the weird thing is, is that even across projects, there seem to be certain themes in common.
For example, both the python and the Java way of doing things have the keyword "for" in them and a way to express the looping, and then follow that up with brackets.
There should be some way to code that in, and projects should be able to import this "interface" of how to do something, if you will.

A better example may be printing in Java and in Python.

If you want the languages to print something, they both have their own print function that you then just call on whatever you want it to print.
It's the same for both. So I should be able to say "hey, use the same thing Python does, except for that instead of 'print', use 'System.out.println'"

The second issue with this is then I get into version control. If I change the interface of the Python print, should the Java print interface stay the same?
In other words, does the Java interface point to the Python interface? Or is the Java framwork a copied interface from Python?

I'm going to have it copy it for now. Each project can have interfaces that can be copied into other projects.
Actually, stealing a word from Java: these should be called "interfaces" not "frameworks". I'm going to replace all instances of "frameworks" with "interfaces" except for this line.

So, another issue arises: Obviously snippets of code could implement many more than one interface, and sometimes it will implement an interface more than once.

The deal is, if it implements an interface more than once, you must supply parameters every time the interface is implemented.

For example, a "parentheses" interface might be used to keep track of what symbols are used to include certain variables.
If Java has something it usually uses for these parentheses, it may be able to automatically put them in.

This is seeming to get really complicated really quickly which worries me.

I'm going to see what this interface thing might look like and decide if I want to do it.
'''

'''
5/16/16

Interfaces. Do I want to use them? What would one look like?

Here's a print interface:
it uses the parentheses interface
It also uses the endCommand interface

print(printCommand, value):
    return printCommand+parentheses.open+value+parentheses.close+endCommand
    
So I want to be able to literally copy this in.
Because let's say I do this for something like a for loop, where Java uses the endCommand within the for loop, but Python does not. I want to be able to quickly edit the Python version and take those out.

It may end up that there are many copies of the same interface. So how do you keep track of the names?

If some interfaces use other interfaces, are these all available somewhere within the project? Yes.

So the names can be kept track of because each project has its own set of interfaces that it uses.

How will interfaces actually be implemented? Classes? It seems like the dot notation lends itself well to holding info, though I could also use hash tables.


What exactly are interfaces (in this program)? When exactly should I use them?

Interfaces are a way to set up actions that may be similar across different projects.

So, if for example it's common to have something like parentheses, where two symbols encapsulate some text, an interface for parentheses can be made,...
where you pass the text in the middle to the paretheses interface along with what you're currently using as parentheses.

Unlike what I did above, interfaces should not actually be used to store information.

On second thought, this isn't really an interface. It's more like a method.

But the point is that between programs there are certain elements that should be the same. Oh! But those are just put into place when the interface/method is imported.

So what do I call this thing? Do I call it an interface?

An interface in Java is something that supports certain methods. With that definition, no, I don't think this is an interface.

So what should I call it then? Framework. I think that makes more sense. You can import frameworks from other projects with similar pieces of code.

But this also means some frameworks would rely on other frameworks in order to work. For example, if I wanted to use the parentheses framework within the print framework;...
it just wouldn't work unless it also used the 

So if I wanted to set up a framework for the print function I think it would be:

print(printCommand, value, parenthesesFramework(openParen, closeParen), endLineSymbol):
    return printCommand+parenthesesFramework(openParen, closeParen, value)+endLineSymbol
'''

'''
5/16/16

The whole framework thing is seeming really messy and confusing right now.

I think I'll need some more time to sort it out and figure out what's going on and how to make it easier instead of harder.
'''

'''
5/17/16

So the goal now is to make a simple shell that can load, use, and reload environments.

The next thing will be allowing for them to be edited.

A module may contain more than one environment.

its an AttributeError if a class doesn't have a certain attribute (method or property)

Right now I'm just going to program the shell environment in the same module as the shell itself.

Can the shell reload its own environment? If the shells only methods are available through its environment,...
First, that environment would have to be in a separate module; you can't import yourself
What if the environment sent back the text form of what should be run? And then the shell evaluated it? That seems unnecessarily complicated.
Environments are classes with an instance of them whose methods are then called using that instance.
Environments have access to the shell environment through a property of their own called shellEnv.
Can environments execute code that would cause their module to be reloaded? Looking it up quickly says probably not.

So in other words, the shell needs to be separate from its internal environment.

So let's put all the predefined attributes into the actual shell, and call that entire thing just the "shell"

Then, any user-defined attributes that should be carried across external environments (what used to be called "projects") can be put in the internal enivronment.
This way, the internal shell environment can be reloaded as people make changes, but the shell itself should actually never change (while running).

The module containing the shell class, when run as main, should create an instance of the shell class and just call "run()" on it.
'''

'''
5/18/16

Okay, so what do I want commands to look like? Let's do a couple examples and see if they're consistent and/or doable

loop(10)

So here are the things a certain input string can have:
values from the environment
literal strings
base code that should be run
things that are wrong

How do I want to separate these?

Let's come up with examples of each:

loopThrough(the list of scores) #values from the environment
makeNewClassCalled(Students) #literal string
set(env.percentages, [3]*4) #env.percentages is a value fromt he environment, while [3]*4 is base code that should be run

base code that should be run should be done with a call to eval that is a function in the internal environment

Okay, so now I just have to differentiate between:
values from the environment
literal strings
things that are wrong/need to be defined

values from the environment should be able to just be typed as they are, so signal.

Literal strings I feel like they should be encapsulated by quotes.

Things that are wrong/need to be defined can then be determined.

My issue is with numbers. Technically, they're base code. But I feel like they should be able to just be written on their own like an environment value.

I could also just pass all the arguments to the environment and let the environment handle everything.
But no, that just makes things more complicated and ruins the hierarchy.

So should I treat numbers as an internal environment value? Built-in? Okay then, let's do it.
'''

'''
5/18/16

I think I'm going to abuse Python. And I think I will enjoy it very much.

So it turns out that I can set attributes of something that has whitespace with setattr.
So from now on, all the attributes of an environment will be set using setattr so that any attribute can have whitespace in it.
The hard thing will be to figure out how to set functions with whitespace too.
I'm not sure if it's possible at this point.

Let's see.
setattr(self, "func name", ???) so what if I define the function right beforehand using just an underscore?

def _():
    print("hello")
    
setattr(self, "say hello", _)

Let's try that.

It turns out that does work! I love Python.

So now both functions and items can have spaces in them. The only thing that makes functions actual functions is the parentheses. I like it.
I need to check that the command-matching Regex still works.

Yup! It does. Cool.
'''

'''
5/19/16
(it's technically the 19th because I'm programming past 12:00 AM)

Okay, so the next goals are pretty much the same as they were, I just added some new fun sugar :)

The goal is to figure out how catching numbers will work.
Then, make sure functions can be called from environments (that basic commands with numbers work)
Then, figure out how to tell what's in functions, quotes, base code, and whats an environment value. THIS WILL BE DIFFICULT. DONT GIVE UP.
Then, start writing the stuff that will replace environment values
Then, make it actually useable and try using it.
Then, make it interactive, so most things can be done (easily) using only the shell
'''

'''
5/19/16

How will catching numbers work? It doesn't really seem to fit into how the shell works.

So far, we take a command:
{Command name}({parameters})

Basically, when looking for somthing that's an environment value, the shell always first checks a method that will catch all numbers.
I was thinking about this before, and it might be good to offer every environment a chance to do this.
They could each have a method that everything is sent to. If the environment has a match, it returns (True, theMatch) and if not, (False, None)
The difficult part about this is that it introduces a lot of variablility into the programming of the environments, which is supposed to be written autonomously.

Adding catch-all method to each environment:
Pros:
Shell doesn't have to search through environment; environment does what it wants.
Allows renegade environments that work in special cases and help do odd things (kind of like what Python is letting me do now)
All environments work the same (internal environment isn't a special case)

Cons:
Breaks main structure of environments, that the commands and envirovalues are always attributes of the environment.
Allows renegade environments
May make computer understanding of the code close to impossible later on. 

On this one, I think the pros outweigh the cons right now.
This is one of those big decisions though that I can come back and change my mind on later if thinks don't work out.

My reasoning is that this seems like the smoothest way to implement numbers along with making environments much more powerful.
I think of it as like a metatable for objects in Lua; something that catches all the queries before they actually hit the object.
I think a computer that can edit the code of the object will work well enough for now, and I'll just be responsible for the code of the catch-all.
'''

'''
5/19/16

Also, I just want to mention the idea of a verbose command that I came up with today.

If you type a command name without any parentheses or parameters, it will run the command,...
but the computer will prompt you for the different parameters so you don't have to remember them on your own or look them up.
This is almost exactly the type of interactivity I imagined a final product having.
'''

'''
5/19/16

So, what will this catch-all be called, and how will it work?

How do environments work? Originally, the shell would go through and try to get the attribute of the environment class.
If the query failed, it would move up to the next available environment up until it couldn't find one, in which case it can either fail, or ask for help.

Now, the shell will merely run a function of the environment that will act like the environment's fancier version of getattr.
Ooh! What if I made my own error if that fancier version failed?
So it's still querying, and that query will either fail with a specific error...
(or I could just use the exact same error that getattr uses) or return the correct envirovalue for the envirokey

I like this. It totally fits in with the methodology.

Let's do it.

What should this method be called? Can I actually call it getattr? Yes, but it seems like a bad/confusing idea.

What if I called it getenvattr? I like that. Simple. Easy to remember. Mimics Python. Let's use it.

So each environment must have a function called getenvattr that does the exact same thing as getattr except the environment can do what it wants with the parameters.

I just learned I can actually just define __getattr__ which will be used for values that can't be explicitly found in the environment. This is perfect for what I want.

So if an environment wants to, it can define a __getattr__ to help it define stuff that can't or shouldn't be putting into attributes.
'''

'''
5/19/16

Upgrade: There should be a way to add imports to an environment module, such as re, like I added by hand for the Shell1Environment.
'''

'''
5/19/16

Okay then, the shell now supports converting numbers into actual numbers.

Just to clarify the types of things because they're starting to confuse me:

An initial command is always recieved as a string.
getattr is always called with (class, attribute), where class is an instance of a class (in this case, the class is an environment), and attribute is a string.
But, the methods of an environment are always called with obejcts/actual code. So if you have a envrionment method that adds two numbers, that method should expect two actual numbers, not two strings.
The methods of an environment are not expected to return just strings, either. Environment methods can do anything and return anything.

Since I'm using environments right now to print out string responses chances are that most of my functions will output strings.
'''

'''
5/19/16

Let's look back at my list of things to do:

I did figure out how catching numbers will work.
I did make sure functions can be called from environments (that basic commands with numbers work)
Then, figure out how to tell what's in functions, quotes, base code, and whats an environment value. THIS WILL BE DIFFICULT. DONT GIVE UP.
Then, start writing the stuff that will replace environment values
Then, make it actually useable and try using it.
Then, make it interactive, so most things can be done (easily) using only the shell
'''

'''
5/19/16

I just wanted to clear up some more things about the Shell.

The Shell code should only expose functions that should be able to be accessed from the terminal interface.

But wait, shell.run() should not be accessible, yet it needs to be there. So the whole thing of stuff being built into the shell won't work.

The shell needs two internal environments, one that is modifiavble, and one that is not.

The unchangeable one will be called the static internal environment, and the changeable one will be called the dynamic internal environment.

The Shell should be able to access them through self.staticInternalEnva and self.dynamicInternalEnv

Every shell function that should be able to be run from the terminal should be in one of the two interal environments

Every function that should not be accessible via terminal should be in the shell code itself.

So you can figure out where a function should be defined with two questions:

1. Should I be able to access this function from the terminal?
If yes, then continue to question 2
If no, it should go in the shell code

1. Should I be able to modify this function?
If yes, it should go in the dynamic internal environment.
If no, it should go in the static internal environment


In other terms:
Dynamic Internal: terminal-accessible, modifiable
Static Internal: terminal-accessible, not modifiable
Shell code: not terminal-accessible, not modifiable

If unsure, make it modifiable. (Then, you'll probably become sure.)

'''

'''
5/19/16

In terms of finding an envirovalue, it searches in the Static Internal first, then External, then Dynamic Internal.
Shell code is never checked because its not an environment. That's exactly how it's supposed to work; it's unaccesible.

The thing is though, every single environment does have a link to it, should they choose to use it, through self.shellEnv

Wait. That should be a link to the static environment first. Dynamic, even.

So the issue is, I don't really want anything being able to access the shell code other than the static internal shell

What I want is for the methods in the shell to be callable only by the static internal shell, but not be in the static internal shell
(as that would make them available in the teminal)

They should just go in the same module as the static internal shell.

What does the shell code do then? Just recieve commands and pass them on? That seems about right.

So then what type of code goes into the shell? Why wouldn't I just put it in the module of the static internal shell?

Here's what I totally want:
External environments and dynamic internal environment have use, but not write, permission for the static internal environment
The static internal environment has use and write permission for the external environments and the dynamic internal environments, and use permission for shell code
The shell code has use and write permission for everything.

Originally, the shell looked inside its own code for envirovalues; run() would then become an envirovalue

We're pretending that we can compile any modules we want such that the user cannot modify them or import them, but they know the functions that are inside.

Okay, so let's assume I "compile" the static env and the shell.
'''


'''
5/20/16 and 5/21/16

Couldn't I just have the shell contain all the static internal environment stuff?

What if the static environment was inside the same module as the shell? The dynamic and external environments have a link to the static environment,...
and the static environment just uses the code inside the module.

What is the goal of the shell? The shell takes commands and runs them and then gets more commands. And I think that's about it.

So nothing really needs to have a link to the shell, right?

Ugh. I'm just confusing myself.

Here are examples of methods I want in each category:

Shell: #things that are used to actually run the shell and what's going on behind it.
run()
runCommand()
getEnvirovalue()

Static: #things that should be accessible through the terminal
#question: do these functions need to be able to access the shell? I don't think so.
loadExternalEnvironment()
removeExternalEnvironment()
addMethod()
addCommand()

So then if those functions don't need to be able to access the shell, then the static internal environment doesn't need a link to the shell.
In fact, everything should just link to the static. Everything, including the shell should have access to the static internal environment.
And the internal environment is what should actually be keeping track of the loaded environments and everything else.
So the static internal is basically the hub for everything.

'''

'''
May 24 2016

This issue of what can call what actually kind of made me not want to work on the project
So, I'm just going to ignore it for now.

Since I'm going to be the only one using the product right now, if I want to make it easily breakable for myself, so be it.

In other words, we're back to the static, dynamic and shell environment model.
I'm going to recopy the "how to tell the difference" things down here.

1. Should I be able to access this function from the terminal?
If yes, then continue to question 2
If no, it should go in the shell code

1. Should I be able to modify this function?
If yes, it should go in the dynamic internal environment.
If no, it should go in the static internal environment


In other terms:
Dynamic Internal: terminal-accessible, modifiable
Static Internal: terminal-accessible, not modifiable
Shell code: not terminal-accessible, not modifiable
'''

'''
5/28/2016

Well, I thought that maybe private variables would be an option, but after some research...
I learned that python doesn't really have private variables.

So this is probably the best way to go about doing it right now :)
'''

'''
5/28/2016

I want to come up with a couple more examples of what I want things to look like too,...
just to make sure I'm on the right path with the whole environment thing.

Also, do I have a way of doing what the interfaces were supposed to do yet? Allow different structures to be replicated across methods?
I don't see how environments would be made to do this. But let's see if I can figure out a way.

Let's go back to the print function idea.
Both Python and Java have a way to print stuff that's just a function name followed by what you want to print in the parentheses afterwards.
So naturally, I should have a way of recreating this structure when I make a new function.

So first, how sould I be able to define a new function in the Python environment?
Then, how would I be able to use that same structure when making the Java environment?

"define new method(Python)" #define a new method for the Python environment
"function and parameters structure (name, params):
    return name+"
Hmm. I looks like I need typing of some sort, because these functions require very spectial things, and may need different versions based on what the different objects are.
On second thought, people can always just do the typing on their own, and the function will always work, provided it's used correctly.

How would I define the Python print method without the structure?

"define new method (Python)" #define a new method for the Python environment
"def print(something):
    return "print("+something+)"
    
So here's how you could do it.

"def new property (Python)"
"open parenthesis = '('"
"def new property (Python)"
"closed parenthesis = ')'"
"def new property (Python)"
"print statement = 'print'"

"define new method (DynamicEnvironment)"
"def printStructure(somethings):
    return self.shell.getEnvirovalue('print statement')+self.shell.getEnvirovalue('open parenthesis')+somethings+self.shell.getEnvirovalue('closed parenthesis)"
    
In this case, it looks like there should just be an easy way to tell that's it's supposed to be an environment command.
In addition, how is it supposed to know which environment to get it from? What if I want it to help me write a new method specifically for Python?

Another idea to add to the mix: what if you could temporarily overwrite some properties, and then just delete the temporary stuff.
'''

'''
5/28/2016

So how would I use the above method when writing the print for Java?

"def new method (Java)"
"def print(somethings):
    printStructure(somethings)"
    
Agh! This is so confusing! I need to look at my old notes and figure out how I can make this work.

Or, I can decide that this is actually unnecessary.
'''

'''
I feel like structures are a wholly separate thing from methods of environments.

Methods are things the computer knows how to do. They've been explained in terms of base code.
Well, wouldn't a structure also be something the computer can know how to do? How to put together certain elements in the same pattern?

Ah! What if I wrote the print function structure like this:

"def printFunctionStructure(printFuncName, openParen, closeParen, stuffToPrint):
    return printFuncName + openParen + stuffToPrint + closeParen"
    
Then, the Python one can be done as 
"def print(something):
    return printFunctionStructure('print', open parenthesis, closed parenthesis, something)"
    
So the main issue here is that open parenthesis (and closed parenthesis) is an envirovalue.

In other words, structures are used to write methods. Are methods allowed to be used to write each other?
They should be, but I'm not sure if it's possible.
'''

'''
5/29/2016

So how should new methods be defined?
Eventually I want to be able to do something like

define new method (MyGame)
hard check player has lost ()
return players lives + less than + 5 + or + game timer + more than + 30

where players lives, less than, or, game time, and more than are all envirovalues that should be evaluated right then.

So sometimes when putting things into the shell, I want the envirovalues to be determined right then,
and other times I want them to be saved and evaluated later.
When I say saved and evaluated later, I mean that I want the method in the environment to look for the values when it runs.

But somewhere, that behavior has to be defined by base code, right? Right now, that base code would look like
"self.shell.getEnvirovalue(thing)" which is quite a handful to write out.

So let's say I want the envirovalue to be evaluated right then. What can envirovalues evaluate to?
Methods (not a call to a method, but the method itself)
Strings
Numbers
Objects? Let's see... Yup! someProperty = eval('class Yup():\n\tpass\n\nreturn Yup()')

But I guess the same things holds true for eval as it does for envirovalues. Sometimes I want it to evaluate before its saved, other times I want it to be evaluated later. How should I tell the difference?

Let's come up with a small program I'd like to be able to create with the aid of the Code Helper, and see what sorts of things I need to be able to do.

Let's use an example of something I've already done: the lasermaze solver. It should be able to help with something like that.

I'm going to put the example in a new file.
'''

'''
6/1/16

So I keep on running into this issue where I have info that I feel like it should be hidden from the user,...
but I still want the user to be able to access it through other functions that do know how to use the info correctly.

Before, I split this up into the dynamic and static shells as opposed to the shell code.

So, should this be a thing for every environment? If so, what are the catergories? (It would be easiest if it also extended to the shell code split)

1. Accessible through other methods within the environment, but inaccessible from outside a method in the environment
2. Accessible as a property in general (open to any other environment, terminal, etc.)
3. Not accessible

For 3, you can just use variables within the one method that is being run.
It's number 1 that makes me think that every environment Should have something like this.

So there's also a difference between readibility and writability that I did not address.

1. Read and write from anywhere
2. Read-only from anywhere
3. Read and write from enviromethods
4. Read-only from enviromethods
5. Not accessible

How often do I need these?
(1) Is like the dynamic environment
(2) Is like the static 
(3) Is like nothing I've done before
(4) is like the shell code
(5) Is just variables inside a method

Is it even possible to do read-only? I think it would be good to try to implement in practice, even if it can't be made a reality yet;...
I'm hoping I can sandbox stuff later.

What are cases when I would need to use these?

When making a class and having an environment set up for that class, things like the way that class should be initialized would be nice...
if they were stored in something separate from an envirovalue, but maybe still writable and readable.

When would I ever want something to not be readable or writeable? Never! I'm all about costumizeability and access.
Except for maybe when it comes to the static envrionment and the shell code; I don't want people breaking it.

In fact, the point of the static class is just to do what I'm doing here; make it so that the terms aren't easily accessible by the terminal.

So maybe the only thing I put inside the static environment is code that will reset parts of the dynamic environment in case someone messes something up.

In other words, how customizeable do I want this to be? Do I want to present programmers with so much power they can destroy themselves?
I wouldn't mind that. At the same time, I do want to have some hidden stuff; I don't want to have people easily do something like moving the bin folder in Linux.
So the idea is to give people enough power that they could destroy themselves, but also make sure there's a restore option in case you really mess up.

So, the issue is, some functions want to store information that should only be accessible when a certain environment is loaded,
but should not be easily accessible as a envirovalue.

So, each environment should have a property or method that allows people to access these other values...
that you have to use if you want to access the values from the terminal...
unless you set up an envirovalue that links to that property.


'''