from FMIndexClass import FMIndex
import time
import matplotlib.pyplot as plt


def read_words(words_file):
        with open(words_file, 'r') as f:
            ret = []
            for line in f:
               ret.append(line.split("\n")[0])
            return ret

if (__name__ == '__main__'):
    inputfile = open("input.txt","r")
    T = inputfile.read()
    
    

    timeList = []
    patternLenList = []
    # start_time = time.time()
    FM = FMIndex(T)
    inLen = len(T)*8
    bitVectorLength = FM.bitVecLen
    print("Bit Vector Length(in bits): ", FM.bitVecLen)
    print("Input text lenght(in bits): ", inLen)
    #pattern file
    pattern_list = (read_words('patternFile.txt'))
    # searching each pattern
    for pattern in pattern_list:
        start_time = time.time()
        patternOcc,index = FM.search(pattern)
        timeList.append((time.time() - start_time)*1000000)
        patternLenList.append(len(pattern))
        print(patternOcc + ' Total pattern occurence(s) inside the text')
        for i in index[::-1]:
    	    print(str(i))
    plt.scatter(patternLenList, timeList)
    plt.xlabel("Pattern Lengths")
    plt.ylabel("Time for searching(micro secs)")
    plt.show()
    print(timeList, patternLenList)
