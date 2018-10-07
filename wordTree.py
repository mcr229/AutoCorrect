import levenshtein
"""
wordTree data structure is a tree whose node values are string words. The edges
connecting the nodes is the levenshtein distance between the words, and there
are no duplicate words in the tree. Capital letter do not change/affect the words
so a word such as "AUTO" is equivalent to "auto." The point of this tree is to
create word trees such that similar words can easily be searched and accessed

variables:
self.root = string variable that is the word of this node

self.closeness = the edit/levenshtein distance value that is considered close

self._children = dictionary with key being distance and value being word Tree

Functions:
__init__()           -> initializes a wordTree object with default word None
getWord()            -> returns the word of this node
getChildren()        -> returns the direct children of this node
addChild()           -> adds a wordTree edge pair as a child
insert()             -> inserts a word to the wordTree
get_similar_words()  -> gets a list of words from wordTree to a word
"""
class wordTree():

    """
    Initializer/Constructor for our tree data structure. It contains a 
    root word [firstWord], a [closeFactor] for how children words are compared, 
    and a dict of children trees [_children].
    """
    def __init__(self, closeFactor, firstWord = None):
        self.root = firstWord
        self.closeness = closeFactor
        self._children = {}
    
    """
    [getWord] is a getter method that returns the root word of the wordTree
    data structure
    """
    def getWord(self):
        return self.root
    
    """
    [getChildren] is a getter method that returns the dictionary of children
    trees
    """
    def getChildren(self):
        return self._children
        
    """
    [addChild node edge] adds a key value pair to the dict of the children of
    wordTree self. The added wordTree object has root word [node], and the edge
    is the distance between the word [node] and its parent word self.root.  
    """
    def addChild(self, node, edge):
        self._children[edge] = wordTree(self.closeness, node)
    
    """
    [insert word] inserts a word [word] into the wordTree self. If none of the
    children nodes have the same distance metric then the word is added as a 
    child, otherwise, we recursively call insert for the child with the same
    distance metric and repeat until the word is added. No two equal keys will
    be overridden because if the key and distance are equal then we recursively 
    insert at the next node
    """
    def insert(self, word):
        word = word.lower()
        #Nothing in tree then root becomes word
        if self.root == None:
            self.root = word
            return "none"
        #if the root and word check are the same then don't insert
        if(self.root == word):
            return "not_inserted"
        #distance is computed
        distance = levenshtein.compareWords(self.root, word)

        try:
            #if dicitionary has key with same distance then insert at that node
            return wordTree.getChildren(self)[distance].insert(word)
        except KeyError:
            #insert at root if no child have equal distances
            wordTree.addChild(self, word, distance)
        
        #return the parent word
        return self.root  
    
    """
    [get_similar_words word] returns a list of the words in our tree that are
    similar to the word [word]. If the distance metric is within our closeness
    factor (self.closeness) then we add it to our list. Otherwise we recursively
    travely to nodes that are within a +-self.closeness threshold.
    """
    def get_similar_words(self, word):
        distance = levenshtein.compareWords(self.root, word)
        acc = []
        #if the word is considered close, then add to the acc list
        if distance <= self.closeness:
            acc = acc + [self.root]
        #iterates through distance - closeness to distance + closeness
        for x in range(distance-self.closeness, distance+self.closeness+ 1):
            try:
                #goes through children whos distance lies in the right range
                #and recursively goes to them if they exist
                acc = acc + self.getChildren()[x].get_similar_words(word)
            except KeyError:
                #if the dictionary key distance doesn't exist then pass 
                pass
        return acc
            
        
        
                
        

    
    
            
        