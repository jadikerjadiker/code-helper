'''
So I want this to go through, and everytime it changes something, it updates what thing it should change next in order to actually have an effect.

Can I have it not move pieces into useless positions? This would mean keeping track of every single rotation for a position and making sure that it never touched that piece and never touched the new spot.
That seems pretty useless, tbh.

I think I would be better off if I just skipped useless rotations.

If the laser had to touch every single piece, trying to do positions would make more sense.

Let's just stick with rotations for now.

Each time I do a rotation check, see which things the laser hits. If the laser doesn't hit a certain piece, don't rotate that piece.

Will this actually save time? Yes. For a lot of the fake solutions, I think the laser doesn't touch any of the pieces, or at least very few.

Okay, so when I'm going to start a rotation, first I fire the laser and keep track of all the spaces all of the lasers have gone through. I think the lasers might do this on their own.

Then, I combine all those lists, and each piece that sits on a slot on the list is added to another list of pieces that should be rotated. Then, I run the rotation as normal with those other pieces ignored.

It turns out I actually have something better: the game keeps track of the pieces that were hit, so I can just look at that.

Oh! Looking at the solutionFound() function, it looks like all pieces do have to be hit!

So then I'd also like the game to keep track of each position the lasers cross as they move, so that way for an entire rotation set, if the laser never touches a piece and certain positions,...
then we can skip those positions when moving the piece.

One thing I don't understand is how all the pieces are put in in a different order. I'm going to find that out.

I'm not seeing it, which make me think this program may actually be broken.

But, after doing a lot of testing, it seems that it's there, I just don't know how!

'''