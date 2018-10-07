import unittest
import wordTree
import levenshtein
"""
Unit Tests for the class wordTree and levenshtein.
"""
class Tests(unittest.TestCase):
    
    """Tests for the levenshtein algorithim calculating the edit distance 
    between two words"""
    def testDistance(self):
        self.assertEqual(levenshtein.compareWords("hi", "h"), 1)
        self.assertEqual(levenshtein.compareWords("kittens", "sitting"), 3)
        self.assertEqual(levenshtein.compareWords("A", "a"), 0)
        self.assertEqual(levenshtein.compareWords("cuair", "fair"), 2)
        self.assertEqual(levenshtein.compareWords("cuair", "plane"), 4)
        self.assertEqual(levenshtein.compareWords("cuair", "place"), 4)
        self.assertEqual(levenshtein.compareWords("plane", "place"), 1)

        self.assertEqual(levenshtein.compareWords('hi', 'ha'), 1)
        self.assertEqual(levenshtein.compareWords('he', 'ha'), 1)

    """Tests the insert function for our word Tree, makes sure that that the
    children list is correctly modified, and that the word is accessible."""
    def testInsert(self):
        root = wordTree.wordTree(2)
        self.assertEqual(root.getWord(), None)
        self.assertEqual(root.insert("cuair"), "none")
        
        root = wordTree.wordTree(2, "cuair")
        self.assertEqual(root.getWord(), "cuair")
        
        self.assertEqual(root.insert("fair"), "cuair")
        self.assertEqual(root.getChildren()[2].getWord(), "fair")
        self.assertEqual(len(root.getChildren()), 1)
        
        self.assertEqual(root.insert("plane"), "cuair")
        self.assertEqual(root.getChildren()[4].getWord(), "plane")
        self.assertEqual(len(root.getChildren()), 2)
        
        planeTree = root.getChildren()[4]
        #root.insert("place")
        self.assertEqual(root.insert("place"), "plane")
        self.assertEqual(planeTree.getChildren()[1].getWord(), "place")
        self.assertEqual(len(planeTree.getChildren()), 1)
        self.assertEqual(len(root.getChildren()), 2)
        
        self.assertEqual(root.insert("cuair"), "not_inserted")
        self.assertEqual(len(planeTree.getChildren()), 1)
        self.assertEqual(len(root.getChildren()), 2)

        
    
    """Tests the function get_similar_words from our wordTree object. It
    makes sure that all similar words are outputted as a list."""
    def test_similar_words(self):
        root = wordTree.wordTree(2, "cuair")
        root.insert("fair")
        root.insert("plane")
        root.insert("place")
        self.assertEqual(root.get_similar_words("cuaid"), ["cuair"])
        self.assertEqual(root.get_similar_words("plade"), ["plane", "place"])

        #Testing very far closeness factor i.e. how two words are compared
        root = wordTree.wordTree(5, "cuair")
        root.insert("fair")
        root.insert("plane")
        root.insert("place")
        self.assertEqual(root.get_similar_words("cuaid"), 
                                            ["cuair", "fair", "plane", "place"])
        self.assertEqual(root.get_similar_words("plade"),
                                            ["cuair", "fair", "plane", "place"])

        #Testing larger trees with varying word lengths
        root = wordTree.wordTree(3, "hello")
        root.insert("hi")
        root.insert("hello")
        root.insert("hi man")
        root.insert("goodbye")
        root.insert("helo")
        root.insert("godby")
        root.insert("gooye")
        root.insert("your")
        root.insert("you're")
        root.insert("yous")

        self.assertEqual(root.get_similar_words("hellos"), ["hello", "helo"])
        self.assertEqual(root.get_similar_words("goodbyes"), 
                                        ["godby", "gooye", "goodbye"])
        self.assertEqual(root.get_similar_words("you"), ["hi", "your", "yous", 
                                                                    "you're"])
        #Testing some edge cases
        root = wordTree.wordTree(3, "CUAIR")
        self.assertEqual(root.get_similar_words("hellos"), [])
        self.assertEqual(root.get_similar_words("fair"), ["CUAIR"])
        self.assertEqual(root.get_similar_words("cuair"), ["CUAIR"])

        similarWords = wordTree.wordTree(2, 'he')
        similarWords.insert('ha')
        self.assertEqual(similarWords.get_similar_words("hi"), ["he", "ha"])


    if __name__ == "__main__":
        unittest.main()
        