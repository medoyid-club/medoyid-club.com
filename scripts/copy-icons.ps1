# Скрипт: copy-icons.ps1
# Назначение: Поиск и копирование SVG-иконок по ключевым словам с фильтрацией
# Использование:
#   -Keywords "home,news,video" -Style outline -Exact $true -Limit 1
#   -Keywords home news video -Style all -Exact $false -Limit 0

param(
    [Parameter(Mandatory=$true)]
    [string[]]$Keywords,
    [ValidateSet("outline", "filled", "all")]
    [string]$Style = "all",
    [bool]$Exact = $false,
    [int]$Limit = 0
)

# Обработка ключей: если передана одна строка с запятыми, разбиваем её
if ($Keywords.Count -eq 1 -and $Keywords[0] -like "*,*") {
    $Keywords = $Keywords[0] -split "," | ForEach-Object { $_.Trim() }
}

$SourceDirs = @()
if ($Style -eq "all" -or $Style -eq "outline") {
    $SourceDirs += "D:\work\medoyid-club\temp_media\tabler-icons-main\icons\outline"
}
if ($Style -eq "all" -or $Style -eq "filled") {
    $SourceDirs += "D:\work\medoyid-club\temp_media\tabler-icons-main\icons\filled"
}
$TargetDir = "D:\work\medoyid-club.com\medoyid-club\static\icons"

$found = 0
foreach ($SourceDir in $SourceDirs) {
    Write-Host "\nПоиск в: $SourceDir" -ForegroundColor Cyan
    foreach ($kw in $Keywords) {
        if ($Exact) {
            $pattern = "^" + [regex]::Escape($kw) + "\.svg$"
            $files = Get-ChildItem -Path $SourceDir -Filter "*.svg" -Recurse | Where-Object { $_.Name -match $pattern }
        } else {
            $files = Get-ChildItem -Path $SourceDir -Filter "*${kw}*.svg" -Recurse
        }
        if ($Limit -gt 0) {
            $files = $files | Select-Object -First $Limit
        }
        if ($files.Count -eq 0) {
            Write-Host "  Не найдено иконок для ключа: $kw" -ForegroundColor Yellow
        }
        foreach ($file in $files) {
            $dest = Join-Path $TargetDir $file.Name
            Copy-Item $file.FullName $dest -Force
            Write-Host "  Скопировано: $($file.Name)" -ForegroundColor Green
            $found++
        }
    }
}
if ($found -eq 0) {
    Write-Host "Не найдено ни одной иконки по заданным ключам." -ForegroundColor Red
} 