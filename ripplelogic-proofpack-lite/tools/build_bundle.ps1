param(
    [string]$Root = ".",
    [string]$BundleName = "RippleLogic_ProofPack_Lite_v8.5.3_beta.1"
)

$rootPath = (Resolve-Path $Root).Path
$parent = Split-Path $rootPath -Parent
$zipPath = Join-Path $parent ($BundleName + ".zip")

if (Test-Path $zipPath) {
    Remove-Item $zipPath -Force
}

Compress-Archive -Path (Join-Path $rootPath "*") -DestinationPath $zipPath -CompressionLevel Optimal
Write-Host "Bundle created: $zipPath"

$zipHash = (Get-FileHash -Algorithm SHA256 -Path $zipPath).Hash.ToLower()
Write-Host "ZIP SHA256: $zipHash"
