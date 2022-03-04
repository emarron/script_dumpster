
FOR /R "%1" %%G in (*.tga) DO (
    ECHO %%G
    nvtt_export.exe "%%G" -f "%2"
)