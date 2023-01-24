user_input = input('enter any number: ')
if user_input.isnumeric():
  number = int(user_input)

  for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
else:
  print('please enter numbers only.')