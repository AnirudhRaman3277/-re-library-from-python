import re
import fileinput

def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " "
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)

print("Enter your text - Leave a blank line without space at first to end:")
lines = []

while True:
    line = input()
    if line == "":  
        break
    lines.append(line)

user_text = "\n".join(lines)
print("\nInput:")
print(user_text)

print("\nOutput:")
output = comment_remover(user_text)
print(output)