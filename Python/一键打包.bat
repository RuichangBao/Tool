start pyinstaller -F ExcelToCSV.py --distpath "../Python"
start pyinstaller -F ExcelToCsharp.py --distpath "../Python"
@REM rd/s/q "build"
@REM rd/s/q "__pycache__"