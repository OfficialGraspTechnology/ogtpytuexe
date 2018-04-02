@echo off
cls
title = PyTuExe Uninstaller
color e
:: set up the window
mode con cols=60 lines=10

:begin
cls
set /p choice=Are you sure you want to uninstall OGT PyTuExe(Yes/No)?
if %choice% == Yes goto uninstall
if %choice% == y goto uninstall
if %choice% == yes goto uninstall
if %choice% == Y goto uninstall

if %choice% == No exit
if %choice% == n exit
if %choice% == no exit
if %choice% == N exit
echo Invalid command
ping localhost -n 2 >nul
goto begin

:uninstall
cls
color c
echo Cleaning up...
ping localhost -n 2 >nul
reg delete "HKEY_CURRENT_USER\Software\PyTuExe" /f >nul
echo Registry clean up complete
ping localhost -n 2 >nul
echo Removing PyTuExe...
ping localhost -n 2 >nul
del /f /q ..\PyTuExe.vbs >nul
echo Removing images...
ping localhost -n 2 >nul
rmdir /s /q ..\assets >nul
echo Removing bin...
ping localhost -n 2 >nul
rmdir /s /q ..\bin >nul
echo Removing readme.txt...
ping localhost -n 1 >nul
del /f /q ..\readme.txt >nul
echo Clean up complete.Quiting in 5 seconds...
ping localhost -n 5 >nul
exit
