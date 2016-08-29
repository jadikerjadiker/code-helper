import re

'''
Takes the weights and biases and uses regex to turn it into a copiable form that actually creates a net.
'''
#*args is in the form [stringToModify, (regex1, sub1), (regex2, sub2), (regex3, sub3), ....]
def multisub(*args):
    args = list(args)
    ans = args.pop(0) #the first argument is the string
    
    for i, rAndS in enumerate(args):
        ans = re.sub(rAndS[0], rAndS[1], ans)
        
    return ans

sentinel = '...'
myInput = '\n'.join(iter(raw_input, sentinel))
print('\n'*7)
print(multisub(myInput, (r'^.*?Weights:\s*', 'weights = \n['), (r']\s*Biases:\s*', ']],\nbiases = \n['), (r'(?<=[0-9])(?P<space>\s+)(?=[\-0-9])', ",\g<space>"), (r'(?<=\])(?P<space>\s+)(?=\[)', ",\g<space>"), (r'\]\s*$', ']]')))
