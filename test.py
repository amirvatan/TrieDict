from Trie import Trie

p = Trie()

list = ['hello', 'salam', 'cat', 'gorbe', 'dog', 'sag']
list2 = ['cat', 'hello', 'dog',"hector",'friend']
k = 0
z = 1
# p.Insert('hello', 'salam')
# p.Insert('cat', 'gorbe')
# p.Insert('dog', 'sag')
# p.Insert('friend', 'doost')
#
p.ReadFromFile()
# node = p.wordlist[9].wordlist[6].wordlist[13].wordlist[13].wordlist[16].wordlist[0]
# node2 = p.wordlist[5].wordlist[16].wordlist[8].wordlist[0]
# node3 = p.wordlist[4].wordlist[1].wordlist[21].wordlist[0]
# for i in range(5):
#     node = p.Search(list2[i])
#     if node is not None:
#         print(node.wordlist[0].meaning)
#     else:
#         print('NULL')
# p.DeleteWord('dog')
#
# for i in range(5):
#     node = p.Search(list2[i])
#     if node is not None:
#         if node.wordlist[0] is not None:
#             print(node.wordlist[0].meaning)
#     else:
#         print('NULL')
#
p.ChangeMeaning('nisst','mikhambfhmm')
#
# for i in range(5):
#     node = p.Search(list2[i])
#     if node is not None:
#         print(node.wordlist[0].meaning)
#     else:
#         print('NULL')

p.FindWithPreFix('doo')