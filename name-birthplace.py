name = input("What is your name?")
birthplace = input("Where were you born?")

if birthplace[0] == 'a' or birthplace[0] == 'A':
    print("Hi", name, "from a place whose name starts with A, how are you today?")
else:
    print("Hi", name, "from a place whose name doesn't start with A, how are you today?")