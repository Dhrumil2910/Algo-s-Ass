
from BWTClass import BWT

class FMIndex(object):

	def __init__(self, text):
		burrowsWheeler = BWT()
		self.bwtString, self.suffixArray = burrowsWheeler.evaluateBWT(text)
		self.charOcc, self.bitVecLen = burrowsWheeler.occAtEachIndex()
		self.totalChars = burrowsWheeler.totalCharacters(self.bwtString)
		self.firstColCount = burrowsWheeler.firstColCounts(self.totalChars)

	#Search function
	def search(self, pattern):
		lenOfPattern = len(pattern)
		if pattern[lenOfPattern-1] not in self.charOcc.keys():
			return ('Pattern Not Found', [-1])
		startPointer = self.firstColCount[pattern[lenOfPattern-1]] + 1
		endPointer = self.firstColCount[pattern[lenOfPattern-1]] + self.totalChars[pattern[lenOfPattern-1]]
		while startPointer <= endPointer and lenOfPattern >=2:
			if pattern[lenOfPattern-2] not in self.charOcc.keys():
				return ('Pattern Not Found', [-1])
			startPointer = self.firstColCount[pattern[lenOfPattern-2]] + self.charOcc[pattern[lenOfPattern-2]][startPointer-2] + 1
			endPointer = self.firstColCount[pattern[lenOfPattern-2]] + self.charOcc[pattern[lenOfPattern-2]][endPointer-1]
			lenOfPattern -= 1
		if (endPointer < startPointer):
			return ('Pattern Not Found', [-1])
		else:
			indexOcc = []
			for lenOfPattern in range(startPointer-1, endPointer):
				indexOcc += [self.suffixArray[lenOfPattern]]
			return(str(endPointer-startPointer+1), indexOcc)