import psutil

print("Psutil version:", psutil.__version__)
print("Current process:", psutil.Process().name())
