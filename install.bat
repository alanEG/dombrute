@echo off
echo Script started.

REM Download Chromium mini_installer
echo Downloading Chromium mini_installer...
curl "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Win%%2F1001268%%2Fmini_installer.exe?generation=1652148457582142&alt=media" -o "%TEMP%\chromium.exe"

REM Run Chromium browser
echo Starting install Chromium browser...
"%TEMP%\chromium.exe"

REM Download custom Chromedriver
echo Downloading custom Chromedriver...
curl "https://chromedriver.storage.googleapis.com/103.0.5060.134/chromedriver_win32.zip" -o "%TEMP%\chromedriver.zip"

REM Unzip custom Chromedriver
powershell -command "Expand-Archive -Path '%TEMP%\chromedriver.zip' -DestinationPath '%TEMP%'"

REM Move Chromedriver to the current directory
move "%TEMP%\chromedriver.exe" "%cd%"

REM Download mitmproxy installer
echo Downloading mitmproxy installer...
curl "https://snapshots.mitmproxy.org/9.0.1/mitmproxy-9.0.1-windows-x64-installer.exe" -o "%TEMP%\mitmproxy_installer.exe"

REM Run Chromedriver
echo Installing mitmproxy...
"%TEMP%\mitmproxy_installer.exe"

REM Remove the archive files 
echo Removing the archive files
powershell -command "Remove-Item -Path '%TEMP%\chrom*' -Recurse -Force"
powershell -command "Remove-Item -Path '%TEMP%\mitmproxy_installer.exe' -Recurse -Force"
