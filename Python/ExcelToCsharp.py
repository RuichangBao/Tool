import os
import xlrd
import pandas as pd
from enum import Enum

inputPath = '../Excel'
outputPath = '../UnityProject/Assets/Ref'

#模拟Main方法
def Main():
    print(cSharpType.int.name)
    CreateFolder(outputPath)
    ReadFile()
    return


#创建不存在的文件夹
def CreateFolder(folderPath):
    if(not os.path.exists(folderPath)):
        os.makedirs(folderPath)
    return


#读取所有文件
def ReadFile():
    fileList=os.listdir(inputPath)
    for filename in fileList:
        GetSheetFiles(inputPath,filename)
    return

#读取该文件的所有表格
def GetSheetFiles(path,sFileName):
    data = xlrd.open_workbook(path+'/'+sFileName)
    sheetsNames = data.sheet_names()
    for sheetName in sheetsNames:
        table = data.sheet_by_name(sheetName)
        name = table.name
        rowNum = table.nrows    #行数
        if rowNum<3:
            print("数据格式不正确："+sheetName)
            continue
        #生成C#类
        cSharpName = outputPath+"/"+name+".cs"
        fo = open(cSharpName, "w")
        cSharpClass = "/*\n* 自动生成文件，请勿编辑\n*/\npublic class "+name+'\n{\n'
        listName = table.row_values(1)
        listType = table.row_values(2)

        if len(listName)<=len(listType):
            listCount=len(listName)
        else:
            listCount=len(listType)
        print(str(listName))
        print(str(listType))
        for i in range(listCount):
            print(i,listName[i],listType[i])
            if listName[i]!=None and listType[i]!=None:
                strVariable = GetCSharpVariable(listType[i],listName[i])
                if(strVariable!=None):
                    cSharpClass = cSharpClass+strVariable
        cSharpClass = cSharpClass+"}"  
        print(cSharpClass)
        fo.write(cSharpClass)
        # 关闭打开的文件
        fo.close()
    return

class cSharpType(Enum):
    int = 1
    string = 2

#获取C#变量
def GetCSharpVariable(variableType,variableName):
    for cSType in cSharpType:     # 遍历
        if variableType.lower()==cSType.name:
            return "\tpublic "+cSType.name+" "+variableName+";\n"
    return

def Test():
    print("Test函数")
    return
Main(); 
Test();

print("Hello python")

# pyinstaller -F ExcelToCsharp.py  打包成exe文件