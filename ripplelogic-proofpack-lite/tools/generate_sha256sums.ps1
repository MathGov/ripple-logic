param(
    [string]$Root = "."
)

$rootPath = (Resolve-Path $Root).Path
$excludeNames = @("SHA256SUMS.txt")
$excludeExts = @(".zip")

$files = Get-ChildItem -Path $rootPath -Recurse -File |
    Where-Object {
        ($excludeNames -notcontains $_.Name) -and
        ($excludeExts -notcontains $_.Extension.ToLower())
    } |
    Sort-Object FullName

$lines = foreach ($f in $files) {
    $hash = (Get-FileHash -Algorithm SHA256 -Path $f.FullName).Hash.ToLower()
    $rel = $f.FullName.Substring($rootPath.Length).TrimStart('\','/')
    $rel = $rel -replace '\\','/'
    "$hash  $rel"
}

$outPath = Join-Path $rootPath "SHA256SUMS.txt"
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllLines($outPath, $lines, $utf8NoBom)

Write-Host "Wrote SHA256SUMS.txt with $($lines.Count) entries -> $outPath"
