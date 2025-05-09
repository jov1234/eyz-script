import codeinstructions

tonken = []
# token variable for all tokenized inputs

def tokeniser():
    # breaks down input 
    global tonken
    code = input(">")
    token = code.split()
    tonken = token  # assign token to global tonken
    return token
    
def interpreter():
    global tonken
    # runs input
    paramiter = tonken[0]
    codeinstructions.RunCode(paramiter, tonken)  # uses code library to run

while True:
    tokeniser()
    interpreter()
