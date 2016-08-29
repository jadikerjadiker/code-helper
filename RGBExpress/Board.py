class Board():
    def __init__(self, howManyNodes, connectedNodes = False):
        self.nodes = [[] for i in xrange(howManyNodes)] #represents a gr
        if connectedNodes:
            for node, linkedNodeList in enumerate(connectedNodes):
                for linkedNode in linkedNodeList:
                    if (not linkedNode in self.nodes[node]) and linkedNode<len(self.nodes) and (linkedNode!=node): #if it hasn't already been added
                        self.nodes[node].append(linkedNode)
                        self.nodes[linkedNode].append(node)
                    else:
                        print("You typed that {} was connected to {} which is not a possible connection, so I'm ignoring it.".format(node, linkedNode))
        else:
            for node in range(howManyNodes):
                linkedNodeList = None
                while type(linkedNodeList)!=list:
                    try:
                        linkedNodeList = list([int(x) for x in raw_input("What nodes does node {} connect to? ".format(node)).replace(",", " ").split()])
                    except ValueError:
                        print("Sorry, I didn't understand that.")
                
                print(linkedNodeList)
                     
                 #   print("Sorry, I didn't understand that")
                for linkedNode in linkedNodeList:
                    if linkedNode>=len(self.nodes) or (linkedNode==node):
                        print("You typed {} which is not a possible node, so I'm ignoring it.".format(linkedNode))
                    else:
                        if (not linkedNode in self.nodes[node]): #if it hasn't already been added
                            self.nodes[node].append(linkedNode)
                            self.nodes[linkedNode].append(node)
                            
