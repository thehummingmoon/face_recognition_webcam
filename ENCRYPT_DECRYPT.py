#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pyDES ')


# In[3]:


def encryptBlock(inputBlock):
    """Encrypt an 8-byte block with already defined key"""
    inputData = permByteList(inputBlock,IPtable)
    leftPart,rightPart = inputData[:4],inputData[4:]
    for round in range(16):
        expRightPart = permByteList(rightPart,EPtable)
        key = subKeyList[round]
        indexList = byte2Bit([i^j for i,j in zip(key,expRightPart)])
        sBoxOutput = 4*[0]
        for nBox in range(4):
            nBox12 = 12*nBox
            leftIndex = getIndex(indexList[nBox12:nBox12+6])
            rightIndex = getIndex(indexList[nBox12+6:nBox12+12])
            sBoxOutput[nBox] = (sBox[nBox<<1][leftIndex]<<4)+                                 sBox[(nBox<<1)+1][rightIndex]
        aux = permByteList(sBoxOutput,PFtable)
        newRightPart = [i^j for i,j in zip(aux,leftPart)]
        leftPart = rightPart
        rightPart = newRightPart
    return permByteList(rightPart+leftPart,FPtable)


def decryptBlock(inputBlock):
    """Decrypt an 8-byte block with already defined key"""
    inputData = permByteList(inputBlock, IPtable)
    leftPart, rightPart = inputData[:4], inputData[4:]
    for round in range(16):
        expRightPart = permByteList(rightPart, EPtable)
        key = subKeyList[15 - round]
        indexList = byte2Bit([i ^ j for i, j in zip(key, expRightPart)])
        sBoxOutput = 4 * [0]
        for nBox in range(4):
            nBox12 = 12 * nBox
            leftIndex = getIndex(indexList[nBox12:nBox12 + 6])
            rightIndex = getIndex(indexList[nBox12 + 6:nBox12 + 12])
            sBoxOutput[nBox] = (sBox[nBox * 2][leftIndex] << 4) +                                sBox[nBox * 2 + 1][rightIndex]
        aux = permByteList(sBoxOutput, PFtable)
        newRightPart = [i ^ j for i, j in zip(aux, leftPart)]
        leftPart = rightPart
        rightPart = newRightPart
    return permByteList(rightPart + leftPart, FPtable)


def encrypt(key, inString):
    """Encrypt plaintext with given key"""
    setKey(key)
    inByteList, outByteList = padData(inString), []
    for i in range(0, len(inByteList), 8):
        outByteList += encryptBlock(inByteList[i:i + 8])
    return outByteList


def decrypt(key, inByteList):
    """Decrypt ciphertext with given key"""
    setKey(key)
    outByteList = []
    for i in range(0, len(inByteList), 8):
        outByteList += decryptBlock(inByteList[i:i + 8])
    return unpadData(outByteList)


# In[ ]:




