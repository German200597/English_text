
# for i in docs:
# with open('1.txt', 'w') as final:
#   with open('1.txt') as one:
#     piece_one = one.readlines()
#     size_one = len(piece_one)
#   with open('2.txt') as two:
#     piece_two = two.readlines()
#     size_two = len(piece_two)
#   with open('3.txt') as three:
#     piece_three = three.readlines()
#     size_three = len(piece_three)



import os
folder = os.listdir(path='/home/runner/Englishtext/docs')
with open('4.txt', 'a') as final:
  for i in folder:
    with open(os.path.join('docs', i)) as file:
      final.write(os.path.basename(i))
      piece = file.readlines()
    final.write(str(len(piece)))
    final.write(piece)
      
    # with open (i) as text:
    #   smile = text.readlines()
    # final.write(smile)
  #   with open(i) as text:
  #     piece = text.readlines()
  #     size_one = len(piece)
  #     print(size_one)
  #     final.write(os.path.basename(i))
  #     print(size_one)
  # sortirovka = sorted()   
   



