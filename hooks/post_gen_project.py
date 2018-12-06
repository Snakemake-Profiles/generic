import os

TARGET = os.path.abspath(os.getcwd())

for root, dirs, files in os.walk(TARGET):
   for filename in files:
       # read file content
       with open(os.path.join(root, filename)) as f:
           content = f.read()
       # replace tag by install path
<<<<<<< HEAD
       content = content.replace('$((INSTALDIR))', TARGET)
=======
       content = content.replace('$((INSTALLDIR))', TARGET)
>>>>>>> 6af7df29a723d8a3ed6a4d9019923171a8053981
       # replace file content
       with open(os.path.join(root, filename), 'w') as f:
           f.write(content)
