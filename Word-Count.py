#-*- coding: utf-8 -*-：
'''
Author: BobWang
'''
import collections
try:
    fname = raw_input('Enter the file name: ')
    fhand = open(fname)
    inp = fhand.read()
    word1=inp.strip()
    print len(word1)
    times = collections.Counter(word1)
    print times

    lines = 0
    words = 0
    characters = 0

    with open('file.txt, 'r'') as i: #请在括号里输入你的文件名称如'随笔'.txt或note.txt。Please enter the your file name instead of file.txt
        for line in i:
            words1 = line.split()
            lines += 1
            words += len(words1)
            characters += len(line)

            print'line_count', lines
            print'words_count', words
            print'character_counts', characters

except:
    print 'File Not Found'

'''
注意：这个Python文件需与你想查询的文件放在同一个文件夹。
Please Put this python file and your file in one folder.
'''
