@echo off
mkdir FolderLoop
for /l %%n in (1, 1, 10) do (
echo Number is %%n > "FolderLoop\File_%%n.txt"
)
pause
