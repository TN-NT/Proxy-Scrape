@echo off
title PROXY SCRAPER BY TIAGZ


:choice
set /P c= Do you install requirements [Y/N]?
if /I "%c%" EQU "Y" goto :install
if /I "%c%" EQU "N" goto :start
goto :choice

:install
pip install requirements.txt
goto :start

:start
python "Proxy Scraper Made by TIAGZ and NAOY.py"
pause