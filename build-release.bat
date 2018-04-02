@echo off

color c
mode con cols=50 lines=20
title='OGT PyTuExe Builder'

set cur_path=%~dp0
set filename=mpl.py
set build_path=%cur_path%lib
set iconname=python_iconn.ico
set icon=%cur_path%assets\icon\%iconname%

echo Building...
pyinstaller -w -F -i %icon% %build_path%\%filename%

mkdir %cur_path%release-build
mkdir %cur_path%release-build\bin
mkdir %cur_path%release-build\assets
mkdir %cur_path%release-build\uninstall
mkdir %cur_path%release-build\assets\icon

xcopy /y /q %cur_path%readme.txt %cur_path%release-build
xcopy /y /q %cur_path%dist\mpl.exe %cur_path%release-build\bin
xcopy /y /q %cur_path%uninstall\uninstall.bat %cur_path%release-build\uninstall
xcopy /y /q %cur_path%assets\icon\HPControl.ico %cur_path%release-build\assets\icon
xcopy /y /q %cur_path%assets\icon\python_iconn.ico %cur_path%release-build\assets\icon

rem ren %cur_path%release-build\bin\mpl.exe PyTuExe.exe

rmdir /q /s %cur_path%dist
rmdir /s /q %cur_path%build
del /q /f /s %cur_path%mpl.spec
rmdir /s /q %cur_path%lib\__pycache__

echo Option Explicit > %cur_path%release-build\PyTuExe.vbs
echo Dim obj >> %cur_path%release-build\PyTuExe.vbs
echo Set obj = CreateObject("wscript.shell") >> %cur_path%release-build\PyTuExe.vbs
echo obj.run "bin\mpl.exe -bs 8WFEHBN9EFM0EJF!M?SWE0NMSVO*9WEHFWEF9EWMF*0E#WSJD0FEWF0VSD9EWFMWEDMV-EWIFVSFEW-F9UEWVMWE-FWE",1 >> %cur_path%release-build\PyTuExe.vbs

echo.
echo Build Successfully

pause
exit
