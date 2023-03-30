import time
from pyautogui import press , hotkey, typewrite
print(""" 
  _____________________________      _________ .__                __    
 /  _____/\______   \__    ___/      \_   ___ \|  |   _________  |  | __
/   \  ___ |     ___/ |    |  ______ /    \  \/|  |  /  _ \__  \ |  |/ /
\    \_\  \|    |     |    | /_____/ \     \___|  |_(  <_> ) __ \|    < 
 \______  /|____|     |____|          \______  /____/\____(____  /__|_ |
        \/                                   \/                \/     \/

""")

choice = input('press 1 for only typing out (use this if you already have your changed text\npress 2 for the best method (doesnt change text) and typing it\n:')

if choice == '1':
    text = input('paste your text (1 paragraph at a time):')
    print('press enter to start typing')
    input()
    time.sleep(3)
    for letter in text:
        time.sleep(0.12)
        press(letter)
    print('Done')
    input()
    exit()
import random, time
if choice == '2':

    newtext = ''
    text = ''
    text1 = input('input your text to be changed (this text is from chatgpt):')
    for letter in text1:
        if letter in (' '):
                num = random.randint(1,4)
                print(num)
                if num in (0,1):
                    text += '  '
                else:
                    text+= ' '

        else:
            if letter != (' '):
                text += letter


    print('your new text:')
    time.sleep(2)
    print(newtext)

    #newtext = "Quantum  computing is  a type of  computing that uses  quantum bits, or qubits,  to store  and process  information.  Qubits are  different from classical  bits  used in  traditional computing,  which can only be in one of two states - either 0 or 1."
    from pyautogui import press, typewrite, hotkey
    cnt = -1
    ft = ''
    test = ['2','1']
    import time
    print(text)
    tst = '7'
    dbs = []
    newt = ''
    def find_double_spaces(string):
        """
        This function takes a string as input and returns a list of the positions where double spaces occur.
        """
        double_space_positions = []
        for i in range(len(string)-1):
            if string[i:i+2] == "  ":
                double_space_positions.append(i)
        #print(double_space_positions)
        return double_space_positions
    dbs = find_double_spaces(text)

    #print(dbs)
    for letter in text:
        cnt+=1
        #print(cnt)
        if letter == ' ':
            if cnt in dbs:
                #print('2' + ' ' + str(cnt))
                newt += '2'
                time.sleep(0.01)
            else:
                #print('1' + ' '+ str(cnt))
                newt += '1'
                time.sleep(0.01)
        else:
            newt += letter
            #print(letter)
    print('43 wpm')
    res = len(text1.split())
    eta = res / 43
    print('eta for the text (will not be 100% correct):' + str(eta) + 'mins')
    #print(newt)
    change = int(input('whats font:')) -1
    print('will start typing 3 seconds after you click enter')
    input()
    time.sleep(3)

    #add a ETA with word count etc

    for letter in newt:
        if letter == '2':
            #press SHIFT+CTRL+,
            #press " "
            for i in range(change):
                hotkey('SHIFT', 'CTRL', ',')
            press(' ')
            for i in range(change):
                hotkey('CTRL', 'SHIFT', '.')
            ft += ' '
        if letter == '1':
            press(' ')
            ft += ' '
        elif letter not in test:
            ft += letter
            press(letter)
    print(ft)
#find_double_spaces(text)



