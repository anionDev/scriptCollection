REM This is useful to allow dualboot for example
C:\Windows\System32\reg.exe Add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power" /f /v "HiberbootEnabled" /t REG_DWORD /d "0"