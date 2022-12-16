from Trie import Trie
tree = Trie()
def app():

    print('================MENU==================')
    print('1-Read From File')
    print('2-Add New Word')
    print('3-Search Word')
    print('4-Change Meaning')
    print('5-Delete Word')
    print('6-Search With PreFix')
    print('0-Exit')
    inp = int(input('please Enter Your option : '))
    if inp == 1:
       tree.ReadFromFile()
       print('=============DONE===========')
       app()
    elif inp == 2:
        word = input('please enter word :')
        meaning = input('please enter meaning :')
        ans = tree.Insert(word,meaning)
        if ans is True:
            print('============ADDED===========')
        else:
            print('=============FAILED===========')
        app()
    elif inp == 3 :
        word = input()
        node = tree.Search(word)
        if node is not None:
            if node.wordlist[0] is not None:
                print(f'meaning is : {node.wordlist[0].meaning}')
            else:
                print('there is no word like that')
        else:
            print('there is no word like that')
        app()
    elif inp == 4 :
        word = input('please enter your word : ')
        newmeaning = input('please enter new meaning : ')
        tree.ChangeMeaning(word,newmeaning)
        app()
    elif inp == 5:
        word = input('please enter your word')
        tree.DeleteWord(word)
        app()
    elif inp == 6:
        word = input('please enter your word prefix : ')
        tree.FindWithPreFix(word)
        app()
    elif inp == 0:
        exit(0)


if __name__ == '__main__':
    app()