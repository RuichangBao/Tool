import os
import xlrd
import pandas as pd

inputPath = '../Excel'
outputPath = '../CSV'
excelHeadCount = 4 #表头数据

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
        rowNum = table.nrows    #行数
        if rowNum<=excelHeadCount:
            print("数据格式不正确："+sheetsName)
            continue
        #表格转csv
        listDatas=[]
        for i in range(excelHeadCount,rowNum):
            rowData = table.row_values(i)
            listDatas.append(rowData)
       
        csv=pd.DataFrame(data=listDatas)#数据有三列，列名分别为one,two,three
        csvName = outputPath+"/"+name+".csv"
        csv.to_csv(csvName,encoding='utf-8',index=False,header=False)
    return


Main(); 

# pyinstaller -F ExcelToCSV.py  打包成exe文件