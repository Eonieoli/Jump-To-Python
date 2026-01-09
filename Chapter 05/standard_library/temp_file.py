import tempfile
filename = tempfile.mkstemp()
print(filename)

f = tempfile.TemporaryFile()
print(f)
f.close()