import re

pattern = re.compile(r"[(^A-Z)A-Za-z%&$\d]{6,}\d")

password = "GumimaNuli23&%6"

if pattern.fullmatch(password):
    print("Congrats, you have access!")
else:
    print("Sorry, you are not authorized")
