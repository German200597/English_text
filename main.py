import os
folder = os.listdir(path='/home/runner/Englishtext-1/docs')
folder.sort()
files = []
with open('4.txt', 'a') as final:
  
  for i in folder:
    with open(os.path.join('docs', i)) as file:
      piece = file.read()
      files.append(
        {
          'name': i,
          'content': piece,
          'length': piece.count('\n')+1
        } 
      )
  # Сортируем
  files.sort(key=lambda x: x['length'])
  # Печатаем
  for entry in files:
    final.write(entry['name'] + '\n')
    final.write(str(entry['length'])+ '\n')
    final.write(entry['content'] + '\n')
    
  # print(files)

   



