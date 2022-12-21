import platform
import subprocess
if platform.system() == "Linux" or platform.system() == "Darwin":
    proc = subprocess.check_output("ps -ef|wx -l", shell=True)
elif platform.system() == "Windows":
    proc = subprocess.check_output("tasklist.exe|find /i  \" K\" /c", shell=True)
anzahlProc = int(proc)
if anzahlProc > 300:
    print("WARNUNG! Die Anzahl der Prozesse liegt über dem Schwellenwert!", anzahlProc)
else:
    print("Die Anzahl der Prozesse liegen unter dem Schwellenwert!", anzahlProc, "Schwellenwert -> 300 Prozesse!")

    def forloop():
        for i in x:
            print(i, "--", x[i] / 1024 / 1024 / 1024)
