from SuffixArrayClass import createSuffixArray
from wavelet import WaveletTree


class BWT(object):

    def __init__(self):
        self.bitVectLen = 0
        self.BWTString = ""
        self.BWTArray = []
        self.sortedSuffices = []
        self.suffixArray = []

    ## just evaluate it from the suffix array
    def evaluateBWT(self, text):
        allSuffices, self.sortedSuffices, self.suffixArray = createSuffixArray(text)
        index = -1
        for i in range(0, len(self.sortedSuffices)):
            if self.sortedSuffices[i][1] == 0:
                index = i
            self.BWTArray += self.sortedSuffices[i][0][-1]
        self.BWTString = ''.join(self.BWTArray)
        return (self.BWTString, self.suffixArray)

	# Character counts in the first column
    def firstColCounts(self, totalChars):
    	firstCol = {}
    	chars = 0
    	for c, count in sorted(totalChars.items()):
    		firstCol[c] = (chars, chars + count)
    		chars += count
    	c = {}
    	for i in sorted("".join(set(self.BWTString))):
    		c[i] = firstCol[i][0]
    	return c

    # Find the character occurences at each index using wavelet tree
    def occAtEachIndex(self):
		tree = WaveletTree(self.BWTString)
		charOccurances = {}
		# The set of characters of BWTString
		setBWT = "".join(set(self.BWTString))

		for i in "".join(set(self.BWTString)):
			charOccurances[i] = []    

		for i in range(0, len(self.BWTString)):
			for c in charOccurances.keys():
				charOccurances[c] += [tree.rank(tree.rootNode, i, c)]
		
		self.bitVectLen = tree.bitVectorlength
		return (charOccurances, self.bitVectLen)

    
     #Find the total number of each character inside the text
    def totalCharacters(self, text):
    	totalChars = {}
    	for character in text:
    		if character not in totalChars:
    			totalChars[character] = 0
    		totalChars[character] += 1
    	return totalChars


