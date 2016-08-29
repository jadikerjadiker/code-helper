'''
I want to make a bunch of neural nets where each one plays against all the others and gets a score (certain points for wins, ties, and losses)
The top x go on to the next training session, and are tested to see if they pass a certain threshold against random players (net or otherwise)
If so, we're done training. If not, a small mutation is made to them, changing a couple weights or (seldomly) adding a new neuron (or even more seldomly) a new layer.
Make sure that about 20% of these new ones are completely random too though so that it still comes up against bizzare play (like it would against random)
Repeat until it passes or until a certain amount of rounds of training (epochs?) have occurred.
Then, print out all the weights and biases so I can remake it if I need to, and hopefully the program will then let the human play against it.

First thing to do: make random player and see how common it is to beat it; what you want the net to improve to.
'''

'''
Having them all play against eachother in a giant tournament will take forever, especially if I'm planning on having more than 9 different nets (which I am)

So, when I have them play, I either have to have them play against random nets within the pool (so that the pool is still better), or against random.

After I see how well this works, I may want to try another method such as having everyone play their random games only...
against the nets that have shown that they're good. (But then that takes out the chance that a random net will show up an older net.)

What if whenever the nets play against eachother, it keeps track of both of their score and how many games they've played (even if it's random so the amount is unequal)?
Then we can do something like what's described above, just using the average fitness score, so that if a random net shows up a big guy, it does lower the big guy's score.
(Though maybe not enough to really make a difference...)
'''

'''
My main worry at this point is how slow this method would be. I think that just doing a genetic algorithm on a lookup table would probably work out better.
I'm going to do a little more research on how genetic algorithm are used with neural nets and then still see if I want to do this.
'''

'''
So after I've done that research, I've basically learned that I was right and this is a terrible idea.
But I'm going to do it anyway.
'''

