import os
import re

def integer_seq(start,step,end):
    start=int(start)
    step = int(step)
    end = int(end)
    integer_list=[]
    for i in range(start,end,step):
        integer_list.append(i)
    return integer_list


def character_seq(start,step,end):
    char_list=[start]
    r=ord(end)-ord(start)
    index=0
    for i in range(step,r,step):
        char_list.append(chr(ord(char_list[index])+i))
    return char_list


def delimtr(start,step,end):
    last_list=[]
    length = len(start)
    for i in range(length):
        if start[i].isnumeric():
            last_list.append(integer_seq(start[i],step[i],end[i]))
        else:
            last_list.append(character_seq(start[i],step[i],end[i]))
    convert_to_text(last_list)

def convert_to_text(last_list):
    for i in range(len(last_list)):
        f = open(f"{i}.txt","w")
        for j in range(len(last_list[i])):
            f.write(f"{last_list[i][j]}\n")
        f.close()

def clear():
    os.system('rm *.seq')
    os.system('rm *.txt')

def concatenate():
    os.system('paste -d"," *.txt > sequence.seq')
    os.system('rm *.txt')

def remove_delimeter():
    f = open("sequence.seq","r")
    result=f"{f.read()}"
    f.close()
    pattern = r','
    result = re.sub(pattern,'',result)
    f = open("sequence.txt","w")
    f.write(result)
    f.close()
    print(result)
    os.system('rm *.seq')

def main():
    clear()
    start_text = input("Enter Start text : ").split(" ")
    step_seq=[]
    for i in range(len(start_text)):
        x=int(input("Enter step: "))
        step_seq.append(x)
    end_text = input("Enter end text : ").split(" ")
    delimtr(start_text,step_seq,end_text)
    concatenate()
    remove_delimeter()
    input("End...")

main()
