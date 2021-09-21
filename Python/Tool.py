import os
import os.path
import xlrd

inputPath = '../Excel'
outputPath = '../Res'

#模拟Main方法
def Main():
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
    for sheetsName in sheetsNames:
        table = data.sheet_by_name(sheetsName)
        name = table.name
        rowNum = table.nrows
        colNum = table.ncols
        print(name,rowNum,colNum)
        for i in range(rowNum):
            for j in range(colNum):
                print(i,j,table.cell_value(i,j))

    
    
    
    return


Main(); 

print("Hello python")