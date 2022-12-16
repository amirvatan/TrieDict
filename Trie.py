import Trie


class Node:
    child = None
    wordlist = [None] * 27

    def __init__(self):
        self.wordlist = [None] * 27


class TrieNode:
    word = ''
    meaning = ''

    def __init__(self, w, m):
        self.word = w
        self.meaning = m


class Trie:
    context = {'a': 1, 'b': 2, 'c': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'h': 9, 'i': 10, 'j': 11, 'k': 12, 'l': 13,
               'm': 14, 'n': 15, 'o': 16, 'p': 17, 'q': 18, 'r': 19, 's': 20, 't': 21, 'u': 22, 'v': 23, 'w': 24,
               'x': 25, 'y': 26, 'z': 27}
    wordlist = [None] * 27

    def Insert(self, w, m):

        newword = TrieNode(w, m)
        cur = self.wordlist
        for num, i in enumerate(w, start=1):
            index = self.context[i]

            if cur[index] is None:
                node = Node()
                cur[index] = node
                cur = cur[index].wordlist
                continue
            else:
                cur = cur[index].wordlist
                continue
        cur[0] = newword
        return True

    def Search(self, w):
        try:
            for z, i in enumerate(w):

                    index = self.context[i]
                    if z == 0:
                        node = self.wordlist[index]
                        continue
                    node = node.wordlist[index]
            return node
        except:
            return None
    def DeleteWord(self,w):
        node = self.Search(w)
        if node is not None:
            node.wordlist[0] = None
        else :
            print('there is no word like this in dictunery')

    def ReadFromFile(self):
        list = []
        file = open('test.txt','r')
        for i in file:
            list.append(i.rstrip())
        while(True):
            if len(list) == 0:
                break
            w = list[0]
            m = list[1]
            self.Insert(w,m)
            list.pop(0)
            list.pop(0)

    def ChangeMeaning(self,w,newm):
        node = self.Search(w)
        if node is not None:
            word = node.wordlist[0]
            if word is not None:
                word.meaning = newm
            else :
                print('there is no word like this')
        else:
            print('there is no word like this')

    def FindWithPreFix(self,w):
        list = []
        node = self.Search(w)
        list.append(node)
        if node is not None:
            for item in list:
                try:
                    for i in item.wordlist:
                        if i is not None:
                            list.append(i)
                except:
                    continue
        for i in list:
            try:
                word = i.wordlist[0]
                if word is not None:
                    print(word.word)
            except:
                continue