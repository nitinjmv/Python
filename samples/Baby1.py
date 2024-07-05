names = {
    "1": "aaru",
    "2": "aashu",
    "3": "nikku"
}
name = input('Enter name: (1.Aaru, 2.Aashu, 3.Nikku): ')

result = ""

match name:
    case "aaru" | "1":
        result = "ooki"
    case "aashu" | "2":
        result = 'noo  sssssssssssmiaauuu & doggy'
    case "nikku" | "3":
        result = "Babies"

print(f'{names.get(name)} says: {result}')
