import os
import time
pic_1='''
    ________
    | /
    |/
    |
    |
    |
    |

'''

pic_2='''
    _________
    | /     |
    |/
    |
    |
    |
    |

'''

pic_3='''
    _________
    | /     |
    |/      O
    |
    |
    |
    |

'''

pic_4='''
    _________
    | /     |
    |/      O
    |       |
    |
    |
    |

'''

pic_5='''
    _________
    | /     |
    |/      O
    |       |
    |       |
    |
    |

'''

pic_6='''
    _________
    | /     |
    |/      O
    |      \|
    |       |
    |
    |

'''

pic_7='''
    _________
    | /     |
    |/      O
    |      \|/
    |       |
    |
    |

'''

pic_8='''
    _________
    | /     |
    |/      O
    |      \|/
    |       |
    |      /
    |

'''

pic_9='''
    _________
    | /     |
    |/      O
    |      \|/
    |       |
    |      / \ 
    |

'''

temp={}
temp[1]=pic_1
temp[2]=pic_2
temp[3]=pic_3
temp[4]=pic_4
temp[5]=pic_5
temp[5]=pic_5
temp[6]=pic_6
temp[7]=pic_7
temp[8]=pic_8
temp[9]=pic_9


def FillUP(blank,OriginalWord,x):
    for i in range(len(OriginalWord)):
        if OriginalWord[i] == x:
            blank[i] = x;
    return blank

def ShowBlank(blank):
    for i in blank:
        print(i,end=" ")
    print()

def check(blank):
    for i in blank:
        if i == '_':
            return True
    return False

def main():
    WrongCount = 1
    OriginalWord = 'APPLE'
    blank = ['_'for _ in range(len(OriginalWord))]
    maxWrongCount = 9
    
    while True :
        os.system('cls')
        print(temp[WrongCount])
        ShowBlank(blank)
        x = input("Enter The latter: ")[0].upper()
        if x in OriginalWord:
            blank = FillUP(blank,OriginalWord,x)
        else:
            WrongCount+=1
        if WrongCount == maxWrongCount or not check(blank):
            os.system('cls')
            print(temp[WrongCount])
            ShowBlank(blank)
            for i in OriginalWord:
                print(i,end=" ")
            break


if __name__ == '__main__':
    main()
