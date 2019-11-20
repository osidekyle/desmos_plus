from riemann import riemann
task = input("What would you like to do?\n")
if "riemann" in task.lower():
    riemann()
else:
    print("Sorry thats not an available option\n")
