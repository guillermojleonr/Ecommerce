# DJANGO_SETTINGS_MODULE
ImproperlyConfigured: Requested settings, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.

DJANGO_SETTINGS_MODULE is missing, doesn't appear in os.environ, seems like it's not beeing set up by the modules that's supposed to add it to
the enviroment variables.

`import os, environ`
`print(os.environ)`

> environ({'ALLOW_ROBOTS': 'False', 'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\guill\\AppData\\Roaming', 'APPLICATION_INSIGHTS_NO_DIAGNOSTIC_CHANNEL': '1', 
'APP_ID': '1064288210506014', 'CHROME_CRASHPAD_PIPE_NAME': '\\\\.\\pipe\\crashpad_18544_HJLETUIAIWRALDYU', 'CLIENT_SECRET': 'VWP5XVnLhSREKwc139jREUA4WFVaVMAc', 
'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 
'COMPUTERNAME': 'DELL-GUILLERMO', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'CONDA_DEFAULT_ENV': 'base', 
'CONDA_EXE': 'C:\\Users\\guill\\anaconda3\\condabin\\..\\Scripts\\conda.exe', 'CONDA_PREFIX': 'C:\\Users\\guill\\anaconda3', 'CONDA_PROMPT_MODIFIER': '(base) ', 
'CONDA_PYTHON_EXE': 'C:\\Users\\guill\\anaconda3\\python.exe', 'CONDA_SHLVL': '1', 'DATABASE_NAME': '', 'DATABASE_PASS': '', 'DATABASE_USER': '', 'DEBUG': 'True', 
'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'ELECTRON_RUN_AS_NODE': '1', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\guill', 'JPY_INTERRUPT_EVENT': '2560', 
'LOCALAPPDATA': 'C:\\Users\\guill\\AppData\\Local', 'LOGONSERVER': '\\\\DELL-GUILLERMO', 'MOZ_PLUGIN_PATH': 'C:\\Program Files (x86)\\Foxit Software\\Foxit Reader\\plugins\\', 
'NUMBER_OF_PROCESSORS': '12', 'ONEDRIVE': 'C:\\Users\\guill\\OneDrive', 
'ONEDRIVECONSUMER': 'C:\\Users\\guill\\OneDrive', 'ORIGINAL_XDG_CURRENT_DESKTOP': 'undefined', 'OS': 'Windows_NT', 
'PATH': 'c:\\Users\\guill\\anaconda3;C:\\Users\\guill\\anaconda3;C:\\Users\\guill\\anaconda3\\Library\\mingw-w64\\bin;C:\\Users\\guill\\anaconda3\\Library\\usr\\bin;C:\\Users\\guill\\anaconda3\\Library\\bin;C:\\Users\\guill\\anaconda3\\Scripts;C:\\Users\\guill\\anaconda3\\bin;C:\\Users\\guill\\anaconda3\\condabin;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0;C:\\Windows\\System32\\OpenSSH;C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\ProgramData\\DockerDesktop\\version-bin;C:\\Program Files\\Git\\cmd;C:\\Program Files (x86)\\dotnet;C:\\Program Files\\dotnet;C:\\Program Files\\PuTTY;C:\\Users\\guill\\AppData\\Local\\Programs\\Python\\Python310\\Scripts;C:\\Users\\guill\\AppData\\Local\\Programs\\Python\\Python310;C:\\Users\\guill\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\guill\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Users\\guill\\AppData\\Local\\GitHubDesktop\\bin;.', 
'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'AMD64 Family 23 Model 96 Stepping 1, AuthenticAMD', 
'PROCESSOR_LEVEL': '23', 'PROCESSOR_REVISION': '6001', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PROMPT': '(base) $P$G', 'PSMODULEPATH': 'C:\\Users\\guill\\Documents\\WindowsPowerShell\\Modules;C:\\Users\\guill\\AppData\\Local\\Google\\Cloud SDK\\google-cloud-sdk\\platform\\PowerShell', 'PUBLIC': 'C:\\Users\\Public', 'PYTHONIOENCODING': 'utf-8', 'PYTHONUNBUFFERED': '1', 'SECRET_KEY': 'g1%mo$4f$3%9u^1h@jnl5s8$9!m0z3%2wizgp5isa+!wz-drr', 'SESSIONNAME': 'Console', 'SOLICALL_BIN': 'C:\\Program Files (x86)\\SoliCall\\bin\\', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\guill\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\guill\\AppData\\Local\\Temp', 'USERDOMAIN': 'DELL-GUILLERMO', 'USERDOMAIN_ROAMINGPROFILE': 'DELL-GUILLERMO', 'USERNAME': 'guill', 'USERPROFILE': 'C:\\Users\\guill', 'VBOX_HWVIRTEX_IGNORE_SVM_IN_USE': '1', 'VSCODE_AMD_ENTRYPOINT': 'vs/workbench/api/node/extensionHostProcess', 'VSCODE_CODE_CACHE_PATH': 'C:\\Users\\guill\\AppData\\Roaming\\Code\\CachedData\\e4503b30fc78200f846c62cf8091b76ff5547662', 'VSCODE_CWD': 'C:\\Users\\guill\\AppData\\Local\\Programs\\Microsoft VS Code', 'VSCODE_HANDLES_UNCAUGHT_ERRORS': 'true', 'VSCODE_IPC_HOOK': '\\\\.\\pipe\\005ca530b2ebc55575de5f144c5c430d-1.70.2-main-sock', 'VSCODE_NLS_CONFIG': '{"locale":"en","availableLanguages":{},"_languagePackSupport":true}', 'VSCODE_PID': '18544', 'WINDIR': 'C:\\Windows', 'PYDEVD_USE_FRAME_EVAL': 'NO', 'TERM': 'xterm-color', 'CLICOLOR': '1', 'PAGER': 'cat', 'GIT_PAGER': 'cat', 'MPLBACKEND': 'module://matplotlib_inline.backend_inline'})

As you can see DJANGO_SETTINGS_MODULE is not there.

## Has something to do with the import process?
`import sys, os, environ`
`print(sys.path)`

>['d:\\Repositories\\ml_querier', 'c:\\Users\\guill\\anaconda3\\python39.zip', 'c:\\Users\\guill\\anaconda3\\DLLs', 'c:\\Users\\guill\\anaconda3\\lib', 'c:\\Users\\guill\\anaconda3', '', 'c:\\Users\\guill\\anaconda3\\lib\\site-packages', 'c:\\Users\\guill\\anaconda3\\lib\\site-packages\\win32', 'c:\\Users\\guill\\anaconda3\\lib\\site-packages\\win32\\lib', 'c:\\Users\\guill\\anaconda3\\lib\\site-packages\\Pythonwin']

No,when you print(sys.path) the current directory where the script is beeing executed appears because it's added automatically allowing the correct importation of modules, i think 
django.conf import settings is working properly.

## Console operations
Every time we make an operation related with django we need to specify the DJANGO_SETTINGS_MODULE enviroment variable, when we use manage.py this enviroment variable is set.
when we use django-admin we need to first set DJANGO_SETTINGS_MODULE=mysite.settings before we make an operation, that's the reason why people recomend to use django-admin only to create a new project and manage.py to make the rest operations. Manage.py sets the enviroment variable DJANGO_SETTINGS_MODULE each time you run the file and that's why we don't see this issue by running manage.py.

I realized that this exception raise only when executing stand-alone scripts that references a django-related element. In this case i used to run auth_op.ipynb with no problems because i didn't use any django-related element, but when I tried to introduce django settings in the class properties of app then the exeption raised.

When we use django we don't execute stand-alone scripts, we execute the functions through the webserver runned by manage.py and I guess that's the reason why I didn't see this exception before.

To fix this and to run stand-alone scripts referencing django-elements put this at the begging of the script

`import os`
`os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ml_querier.settings')`

With this instruction we are settings this enviroment variable even if we can't see it in environ.os, seems like we need to set it every time and then it dissapears.