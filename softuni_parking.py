num = int(input())
registered = {}
for i in range(num):
    command = input().split()

    if command[0] == "register":
        username, license_number = command[1], command[2]
        if username in registered:
            print(f"ERROR: already registered with plate number {license_number}")
        else:
            registered[username] = license_number
            print(f"{username} registered {license_number} successfully")

    elif command[0] == "unregister":
        name = command[1]
        if name not in registered:
            print(f"ERROR: user {name} not found")
        else:
            registered.pop(name)
            print(f"{name} unregistered successfully")

for key,value in registered.items():
    print(f"{key} => {value}")
