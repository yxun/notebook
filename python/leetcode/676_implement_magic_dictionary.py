#%%
"""
- Implement Magic Dictionary
- https://leetcode.com/problems/implement-magic-dictionary/
- Medium

Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:

Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:

You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.
"""

#%%

class S1:

    def __init__(self):
        self.dict = {}
                
    def buildDict(self, dict):
        """
        :type dict: List[str]
        :rtype: None
        """
        for i in dict:
            self.dict[i] = list(i)
        
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        for arr in self.dict.values():
            count = 0
            if len(word) == len(arr):
                for i in range(len(word)):
                    if word[i] != arr[i]:
                        count += 1
            if count == 1:
                return True
        return False


#%%
# trie

class S2:

    def __init__(self):
        self.trie = {}

    def buildDict(self, dict):
        for word in dict:
            node = self.trie
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node[None] = None

    def search(self, word):
        def find(node, i, mistakeAllowed):
            if i == len(word):
                if None in node and not mistakeAllowed:
                    return True
                return False
            if word[i] not in node:
                return any(find(node[letter], i+1, False) for letter in node if letter) if mistakeAllowed else False
            
            if mistakeAllowed:
                return find(node[word[i]], i+1, True) or any(find(node[letter], i+1, False) for letter in node if letter and letter != word[i])
            return find(node[word[i]], i+1, False)
        
        return find(self.trie, 0, True)

