'''
Created on 2019/02/14

@author: tom_uda
'''
def search4letters(phrase:str,letters:str) -> set:
    return set(letters).intersection(set(phrase))