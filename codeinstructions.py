varname = []
varvalue = []

def RunCode(p, t):
    if p == "print" or p == "pnt":
        print(" ".join(t[1:]))
    elif p == "repeat" or p == "rpt":
        try:
            times = int(t[1])
            for _ in range(times):
                RunCode(t[2], t[2:])  # Run the full command from t[2] onward
        except:
            print("Usage: repeat <number> <command>")
    elif p == "run":
        try:
            filename = t[1]
            with open(filename, "r") as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    if line == "" or line.startswith("#"):
                        continue  # skip empty lines and comments
                    tokens = line.split()
                    cmd = tokens[0]
                    RunCode(cmd, tokens)
        except FileNotFoundError:
            print(f"File '{t[1]}' not found.")
        except Exception as e:
            print("Error running file:", e)
    elif p == "execute" or p == "exc":
        try:
            exec(" ".join(t[1:]))
        except Exception as e:
            print("Execution error:", e)

    elif p == "exit":
        print("Goodbye!")
        exit()

    elif p == "set":
        # Example: set name = John
        if len(t) >= 4 and t[2] == "=":
            name = t[1]
            value = " ".join(t[3:])

            if name in varname:
                index = varname.index(name)
                varvalue[index] = value
                print(f"{name} updated to {value}")
            else:
                varname.append(name)
                varvalue.append(value)
                print(f"{name} set to {value}")
        else:
            print("Usage: set <varname> = <value>")

    elif p == "get":
        if len(t) >= 2:
            name = t[1]
            if name in varname:
                index = varname.index(name)
                print(varvalue[index])
            else:
                print(f"{name} not found.")
        else:
            print("Usage: get <varname>")
    elif p == "input" or p == "inp":
         name = t[1]
         value = input(t[2:])

         if name in varname:
                index = varname.index(name)
                varvalue[index] = value
                print(f"{name} updated to {value}")
         else:
                varname.append(name)
                varvalue.append(value)
                print(f"{name} set to {value}")
        
    else:
        print(p, "is not a keyword — check spelling")
