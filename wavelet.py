# Wavelet tree implementation
import time
import os
import sys

#Wavelet Node class
class SingleNode(object):
    # Initilization function
    # Will contain all the required features of the node of a Wavelet tree
    def __init__(self):
        self.bitVector = []
        self.leftChild = None
        self.rightChild = None
        self.characters = {}
        self.differentChars = []
        self.leftNodeText = ""
        self.rightNodeText = ""
        self.text = ""
        self.pointerLeftRight = {}

#Wavelet Tree class
class WaveletTree(object):
    def __init__(self, refText):
        self.refText = refText
        self.bitVectorlength = 0
        self.rootNode = SingleNode()
        self.createTree(self.rootNode, self.refText)
        

    def findDifferentChars(self, refText):
        differentChars = []
        for character in refText:
            if character not in differentChars:
                differentChars.append(character)
        
        return differentChars
    
    def createTree(self, rootNode, refText):
        rootNode.text = refText

        rootNode.differentChars = self.findDifferentChars(rootNode.text)

        rootNode.differentChars.sort()

        if(len(rootNode.differentChars) > 2):
            pivot = ((len(rootNode.differentChars) + 1) / 2)
        else:
            pivot = 1
            
        for character in rootNode.differentChars[0 : pivot]:
            rootNode.characters[character] = 0
            
        for character in rootNode.differentChars[pivot : ]:
            rootNode.characters[character] = 1

        if len(rootNode.differentChars) > 2:
            for character in rootNode.text:
                rootNode.bitVector.append(rootNode.characters[character])
                
                
                if rootNode.characters[character] is 0:
                    rootNode.leftNodeText += character
                else:
                    rootNode.rightNodeText += character

            self.bitVectorlength += len(rootNode.bitVector)
            # Creating new nodes and recursively calling create_tree method
            rootNode.left = SingleNode()
            rootNode.pointerLeftRight[0] = rootNode.left
            self.createTree(rootNode.left, rootNode.leftNodeText)

            rootNode.right = SingleNode()
            rootNode.pointerLeftRight[1] = rootNode.right
            self.createTree(rootNode.right, rootNode.rightNodeText)

        else:
            # This is a leaf
            for character in rootNode.text:
                rootNode.bitVector.append(rootNode.characters[character])
            self.bitVectorlength += len(rootNode.bitVector)

    def rank(self, node, position, character):
        bit = node.characters[character]
        counter = 0
         # Counting the number of the same bit values as the character's bit
        for char in node.bitVector[0 : position + 1]:
            if char == bit:
                counter += 1
        
        # Recursively traversing child nodes
        if len(node.differentChars) > 2:
            return self.rank(node.pointerLeftRight[bit], counter - 1, character)
        else:
            # This is a leaf, we're done
            return counter

