import random
print("CREATED BY Pankaj Sharma\n")

def password(length, complexity):
  gen_pass = []
  complexlist1 = ["q", "w", "e", "r", "t", "y", "u", "i", "o",
                   "p", "a", "s", "d", "f", "g","h", "j", "k",
                     "l", "z", "x", "c", "v", "b", "n", "m", "1",
                       "2", "3", "4", "5", "6","7","8", "9", "0"]

  capalpha = [x.upper() for x in complexlist1 if isinstance(x, str)]
  complexlist2 = complexlist1 + ["!", "@", "#", "$"] + capalpha

  complexlist3 = complexlist2 + ["%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]

  complexlist4 = complexlist3 + ["[", "]", "{", "}", "|", "\\", ":", ";", "'", '"', "<", ">", ",", ".", "?","/"]

  if complexity == 1:
    selected_list = complexlist1
  elif complexity == 2:
    selected_list = complexlist2
  elif complexity == 3:
    selected_list = complexlist3
  elif complexity == 4:
    selected_list = complexlist4

  for i in range(length):
    gen_pass.append(random.choice(selected_list))

  return ''.join(gen_pass)


if __name__ == "__main__":

  length = int(input("Enter Password Length = "))
  print("\n1 for Complexity Level - 1    2 for Complexity Level - 2")
  print("3 for Complexity Level - 3    4 for Complexity Level - 4\n")
  complexity = int(input("Enter complexity level = "))

  while length < 5 or length == " ":
    print("Please should be more than 5")
    length = int(input("Enter Password Length = "))

  while complexity < 1 or complexity > 4 or complexity == " ":
    print("Please enter a number between 1 and 4.")
    complexity = int(input("Enter complexity level = "))


  generated_password = password(length, complexity)
  print(f"Generated Password: {generated_password}")
