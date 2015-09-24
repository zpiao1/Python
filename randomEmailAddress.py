import random


def createDomainString(length):
    domainString = ""
    for countChar in range(length):
        while True:
            char = chr(random.randint(46, 122))
            if char == '.' and (countChar == 0 or countChar == length - 1):
                continue
            elif char == '.' or char.isalnum():
                break
        domainString += char

    return domainString


while True:
    localLen = random.randint(1, 64)
    domainFirstLen = random.randint(1, 255)
    domainLastLen = random.randint(1, 255)
    if localLen + domainFirstLen + domainLastLen <= 252:  # Total 254, including a '.'
        break  # and a '@'

local = domainFirst = domainLast = ""
for count in range(localLen):
    while True:
        code = random.randint(32, 126)
        if code != 64:
            break
    local += chr(code)

domainFirst = createDomainString(domainFirstLen)
domainLast = createDomainString(domainLastLen)

email = local + '@' + domainFirst + '.' + domainLast
print(email)  # very scary
