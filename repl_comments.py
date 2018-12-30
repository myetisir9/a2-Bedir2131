from hashlib import sha256

hashcode1 = '6ef1d0c9875355bfaeefe5bd4d56f9ad5e513bf20068a195f57107d32deb9ac2'

contentList = []
a = 1

def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

while True:
    b = input("Enter your comment:")
    password2 = input('Please enter your password:')

    hashcode2 = create_hash(password2)

    if hashcode1 == hashcode2:
        contentList.append(b)
        print('Previously entered comments:')
        for i in range(a):
            print(contentList[i])
            a += 1
    else:
        print('you cannot do that')
