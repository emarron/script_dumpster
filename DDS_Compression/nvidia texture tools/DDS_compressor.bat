
FOR /R "%1" %%G in ("%2") DO (
    ECHO %%G
    nvtt_export.exe "%%G" -f "%3"
)