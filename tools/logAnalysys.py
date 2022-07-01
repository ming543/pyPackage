#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys, csv

def single():
    files = "./202107/CS040489-CLONE-OS-20210714-162711-PASS.log"
    with open(files, 'r') as fp:
        lines = fp.readlines()
#        lines = str(lines).rstrip('\\n').split(',')
        lines = str(lines).split(',')
        print(lines)

    #with open("./lines.csv", "w", newline='') as csvFile:
    with open("./lines.csv", "w") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(lines)

#single()



def rootb():
    for root, dirs, files in os.walk("./"):
        for f in files:
            fullpath = os.path.join(root, f)
            print(fullpath)
            with open(fullpath, 'r') as fp:
                lines = fp.readlines()
                lines = str(lines).split(',')
                print(lines)
                with open("./lines.csv", "w", newline='') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(lines)
                line = fp.readline()
                while line:
    #                print (line)
                    line = fp.readline()


def root():
    with open("./lines.csv", "w", newline='') as csvFile:
        writer = csv.writer(csvFile)
        for root, dirs, files in os.walk("./"): #遍尋根目錄資料夾檔案
            for d in dirs: #遍尋資料夾
                for root, dirs, files in os.walk(d): #遍尋資料夾內檔案
                    for f in files: #遍尋檔案
                        fullpath = os.path.join(root, f) #建立完整目錄名稱
                        print(fullpath)
                        with open(fullpath, 'r') as fp: #開啟檔案
                            lines = fp.readlines() #讀行
                            lines = str(lines).split(',') #分割
    #                    print(lines)
                            writer.writerow(lines) #寫入CSV

root()







#with open("./test.csv", "w", newline='') as csvFile:
#    fieldnames = ['姓名', '身高', '體重']

    #writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
#    writer = csv.writer(csvFile)
    #writer.writeheader()
#    writer.writerow(lines)

# 打开文件
#path = "/var/www/html/"
#dirs = os.listdir( "./" )

# 输出所有文件和文件夹
#for file in dirs:
#    print (file)
#    with open(file, 'r') as fp:
#        line = fp.readline()
#        while line:
#            print (line)
#            line = fp.readline()
#    fo = open(file, "r")
#    lines = fo.readlines()
#    for line in lines:

#    fo.close
