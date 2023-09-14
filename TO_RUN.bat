@echo off
setlocal enabledelayedexpansion
set "batch_dir=%~dp0\data"
cd /d "%batch_dir%"



:extension
for /f "tokens=*" %%a in ('dir /b /a-d *.xlsx *.xlsm') do (
    set "filename=%%~na"
    set "extension=%%~xa"
    if "!extension!"==".xlsx" (
        ren "%%a" "!filename!.csv"
    )
    if "!extension!"==".xlsm" (
        ren "%%a" "!filename!.csv"
    )
    goto :increment
)

:increment
set "increment=0"
:: Find the largest increment value in existing files
for /f "tokens=*" %%a in ('dir /b /a-d *.csv') do (
    set "filename=%%~na"
    set "extension=%%~xa"
    if "!filename:~0,7!"=="Export_" (
        set "file_increment=%%~na"
        set "file_increment=!file_increment:~7!"
        if !file_increment! gtr !increment! (
            set /a "increment=!file_increment!"
        )
    )
)
:: Increment the value for the next file
set /a "increment+=1"
for /f "tokens=*" %%a in ('dir /b /a-d /od /t:w *.csv') do (
    set "filename=%%~na"
    set "extension=%%~xa"
    if "!filename:~0,7!"=="Export_" (
        echo Keeping the existing name: "%%a"
    ) else (
        set "timestamp=%%~ta"
        ren "%%a" "Export_!increment!_!timestamp:~0,2!.!timestamp:~3,2!.!timestamp:~6,4!_!timestamp:~11,2!h!timestamp:~14,2!!timestamp:~17,2!%%~xa"
        set /a "increment+=1"
    )
)
    :: Add an extra second of loading
timeout /t 1 > nul
:: Close the loading window

echo Renaming complete successfully

set "user_python_dir=%LOCALAPPDATA%\Programs\Python"
"%user_python_dir%\python.exe" "Main.py" %*