'''
I've realized that changing entire layers will not work in this current mechanism because it has to reinit stuff randomly,...
which will most likely make the ones with the layers changed be horrible right away, making it so they're immediately deleted.

The only way that would work is if there was a nursery or hospital for the ones with major mutations...
that would have them quickly play against ones like themselves...
and come up with a decent version that might stand a chance of getting into the top however many.

The hope is that a new neuron may stand a chance of actually helping the net even though it is random, just because it's a small change.

On the other hand, if we initialize a neuron with 0, it will have no effect on the net at first.
This will mean that the net will play a round with no change (just an extra neuron), and hopefully still make it to the next round.
That would probably the best way to do it, making it more likely that it will have many chances to become one of the really good nets.

Actually, it will be best if it initializes with weights coming in, but nothing coming out,...
so that as soon as a mutation causes a weight coming into the next layer to not be 0, it will actually have an effect,...
rather than needing two miracles.
'''