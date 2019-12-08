
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class suffixArray:

  def __init__(self):
    self.string_array = []
    self.suffixArray = []
    self.combine = ''
    self.range = []

  def merge_str(self, str_unicode):
    tail = len(self.combine)
    self.string_array.append(str_unicode)
    if tail != 0:
      self.combine += chr(2)
      self.range.append(tail+1)
    else:
      self.range.append(0)
    self.combine += str_unicode

  def offset_combine2offset_normal(self, offset_combine):
    for id_str, start in enumerate(self.range):
      end = start + len(self.string_array[id_str])
      if(offset_combine >= start and offset_combine < end):
        return offset_combine - start
    return -1

  def offset_sa2id_str(self, offset_sa):
    for i, element in enumerate(self.range):
      end = element + len(self.string_array[i])
      if offset_sa < end and offset_sa >= element:
        return i
    return -1

  def check_suffixArray(self):
    i = 0
    check = []
    while i < len(self.suffixArray) - 4:
      increment = self.suffixArray[i]
      id_string1 = self.offset_sa2id_str(increment)
      string1 = self.string_array[id_string1]
      tail1 = len(string1)
      offset_normal1 = self.offset_combine2offset_normal(increment)

      offset2 = self.suffixArray[i+1]
      id_string2 = self.offset_sa2id_str(offset2)
      string2 = self.string_array[id_string2]
      tail2 = len(string2)
      offset_normal2 = self.offset_combine2offset_normal(offset2)

      if offset_normal2 > -1 and offset_normal1 > -1:
        pstring1 = string1[offset_normal1:tail1]
        pstring2 = string1[offset_normal2:tail2]
        if pstring1 > pstring2:
          pstring1 = pstring1[:20].replace("\n", 'NL')
          pstring2 = pstring2[:20].replace("\n", 'NL')
          check.append((i, i+1))
      i += 1
    return check

  def karkkainen_sort(self):
    length = len(self.combine)
    str1 = self.combine + chr(1) + chr(1) + chr(1)
    b = lst_char(str1)
    str2 = [0]*len(str1)
    kark_sort(str1, str2, length, b)
    self.suffixArray = str2

def CircularSuffixArray(word):
  suffixes = []
  sortedList = word
  SA=[]
  for i in range(0, len(word)):
    suffixes += [(sortedList, i)]
    sortedList = sortedList[1:]+sortedList[0]
  sortedList = sorted(suffixes, key = lambda word: word[0])
  for i in sortedList:
    SA += [i[1]]
  return (suffixes, sortedList, SA)

#!/usr/bin/env python
# -*- coding: utf-8 -*-


def lst_char(str_unicode):
  lst_ch = list(set(str_unicode))
  lst_ch.sort()
  return lst_ch
   
def lesserOrEqual(a1,a2,b1,b2) :
  return (a1 < b1 or (a1 == b1 and a2 <= b2))

def lesserOrEqual1(a1,a2,a3,b1,b2,b3) :
  return (a1 < b1 or (a1 == b1 and lesserOrEqual(a2,a3,b2,b3)))
    
def kark_sort(s, SA, n, alpha) :
  n0 = int((n+2)/3)
  n1 = int((n+1)/3)
  n2 = int(n/3)
  nlen = n0 + n2
  SA12 = [0]*(nlen+3)
  SA0 = [0]*n0
  
  s12 = []
  max = n + n0 - n1
  for i in range(max) :
    if i % 3 != 0:
      s12.append(i)
  s12.extend([0,0,0])

  radixpass(s12, SA12, s[2:], nlen, alpha)
  radixpass(SA12, s12, s[1:], nlen, alpha)
  radixpass(s12, SA12, s, nlen, alpha)
  
  nameLen = 0
  f0, f1, f2 = -1, -1, -1
  arrayName = [0]
  for i in range(nlen) :
    if s[SA12[i]] != f0 or s[SA12[i]+1] != f1 or s[SA12[i]+2] != f2 :
      nameLen += 1
      arrayName.append(nameLen)
      f0 = s[SA12[i]]
      f1 = s[SA12[i]+1]
      f2 = s[SA12[i]+2]
    if SA12[i] % 3 == 1 :
      s12[int(SA12[i]/3)] = nameLen
    else :
      s12[int(SA12[i]/3) + n0] = nameLen
  if nameLen < nlen :
    kark_sort(s12, SA12,nlen,arrayName)
    for i in range(nlen) : 
      s12[SA12[i]] = i+1
  else :
    for i in range(nlen) : 
      SA12[s12[i]-1] = i

  s0 = []
  for i in range(nlen) :
    if SA12[i] < n0 :
      s0.append(SA12[i]*3)

  radixpass(s0,SA0,s,n0,alpha)
  
  p = j = k = 0
  t = n0 - n1
  while k < n :
    if SA12[t] < n0 :
      i = SA12[t] * 3 + 1
    else :
      i = (SA12[t] - n0 ) * 3 + 2

    if p < len(SA0) :
      j = SA0[p]
    else :
      j = 0
 
    if SA12[t] < n0 :
      bool = lesserOrEqual(s[i], s12[SA12[t]+n0],s[j], s12[int(j/3)])
    else :
      bool = lesserOrEqual1(s[i], s[i+1], s12[SA12[t]-n0+1], s[j], s[j+1], s12[int(j/3)+n0])  

    if(bool) :
      SA[k] = i
      t += 1
      if t == nlen : 
        k += 1
        while p < n0 :
          SA[k] = SA0[p]
          p += 1
          k += 1
      
    else : 
      SA[k] = j
      p += 1
      if p == n0 :
        k += 1
        while t < nlen :
          if SA12[t] < n0 :
            SA[k] = (SA12[t] * 3) + 1
          else :
            SA[k] = ((SA12[t] - n0) * 3) + 2
          t += 1
          k += 1
    k += 1


def radixpass(a,b,r,n,k) :
  f_ord = ord(str(k[0])) - 1
  f_new = chr(f_ord)

  c = {f_new : 0}
  list = [f_new]
  for letter in k :
    list.append(letter)
    c[letter] = 0

  for i in range(n) :
    c[r[a[i]]] += 1
  
  sum = 0 
  for letter in list :
    freq , c[letter] = c[letter] , sum
    sum += freq

  for i in range(n) :
    b[c[r[a[i]]]] = a[i]
    c[r[a[i]]] += 1

  return b

def createSuffixArray(T):
	sa1 = suffixArray()
	sa1.merge_str(T)
	sa1.karkkainen_sort()
	sa1.check_suffixArray()
	SA = sa1.suffixArray
	suffixes = []
	sortedList = T
	for i in range(0, len(T)):
		suffixes += [(sortedList, i)]
		sortedList = sortedList[1:]+sortedList[0]
	sortedList = sorted(suffixes, key = lambda T: T[0])
	return (suffixes, sortedList, SA)


