import os
folder = os.listdir(path='/home/runner/Englishtext/docs')
folder.sort()
with open('4.txt', 'a') as final:
  folder.sort(key=len)
  for i in folder:
    with open(os.path.join('docs', i)) as file:
      final.write(os.path.basename(i)+'\n')
      piece = file.read()
    final.write(str(len(piece))+'\n')
    final.write(piece+'\n')

   



