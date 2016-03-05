# -*- coding: UTF-8 -*-


def mergeDict(dict1, dict2):
    dictMerged=dict1.copy()
    dictMerged.update(dict2)
    return dictMerged

if __name__ == '__main__':
    dict1={"1":"a","2":"b"}
    dict2={"1":"a","3":"c"}
    dict3={"1":"a1","3":"c"}
    dictMerged = mergeDict(dict1,dict2)
    dictMerged2 = mergeDict(dict1,dict3)
    print dictMerged
    print dictMerged2