import os
folder = os.listdir(path='/home/runner/Englishtext/docs')
folder.sort()
with open('4.txt', 'a') as final:
  folder.sort()
  for i in folder:
    counter=0
    with open(os.path.join('docs', i)) as file:
      for line in i:
        counter+=1
      final.write(os.path.basename(i)+'\n')
      piece = file.read()
    final.write(str(counter)+'\n')
    final.write(piece+'\n')

   



