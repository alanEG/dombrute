Param(
    [Parameter(Mandatory=$false)]
    [string]
    $ChromeVersion
)


if ($ChromeVersion -eq "") {
    try {
        $ChromeVersion = ((Get-Item (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe').'(Default)').VersionInfo).ProductVersion
    } catch {
        Write-Output "[-]: Faild to get chrome version"
        Write-Output "[-]: Maybe chrome is not installed check it or run the script again with"
        write-Output "[+]: .\install.ps -ChromeVersion <YourChromeVersion>"    
        Exit
    }
}

$SplitVersion = $ChromeVersion.Split('.')
$Version = ($SplitVersion[0..($SplitVersion.Length - 2)]) -join '.'

# Download custom Chromedriver
Write-Host "Downloading custom Chromedriver..."
# Make the HTTP request and get the response content
$Select_Version = ([xml](Invoke-WebRequest -Uri "https://chromedriver.storage.googleapis.com/").Content).ListBucketResult.Contents | Where-Object {$_.Key.Contains($Version)}

if ($select_Version.Length -lt 1){
    write-Output "[-]: The version $Version of chromedriver is not Available"
    Exit
}

$Version = $select_Version[0].Key.split('/')[0]

Invoke-WebRequest -Uri "https://chromedriver.storage.googleapis.com/$Version/chromedriver_win32.zip" -OutFile "$env:TEMP\chromedriver.zip"

# Unzip custom Chromedriver
Expand-Archive -Path "$env:TEMP\chromedriver.zip" -DestinationPath "$env:TEMP"

# Move Chromedriver to the current directory
Move-Item -Path "$env:TEMP\chromedriver.exe" -Destination $PWD.Path

# Download mitmproxy installer
Write-Host "Downloading mitmproxy installer..."
Invoke-WebRequest -Uri "https://snapshots.mitmproxy.org/9.0.1/mitmproxy-9.0.1-windows-x64-installer.exe" -OutFile "$env:TEMP\mitmproxy_installer.exe"

# Run Chromedriver
Write-Host "Installing mitmproxy..."
Start-Process "$env:TEMP\mitmproxy_installer.exe"