x = "!" + "1" * 15 + "2" * 25 + "3" * 35 + "4" * 45

while "!1" in x or "!2" in x or "!3" in x or "!4" in x:
    if "!1" in x:
        x = x.replace("!1", "22!", 1)
    if "!2" in x:
        x = x.replace("!2", "12!", 1)
    if "!3" in x:
        x = x.replace("!3", "24!", 1)
    if "!4" in x:
        x = x.replace("!4", "44!", 1)


print(x)

print(x.count("4"))

# Найти кол-во 4 в получившейся строке