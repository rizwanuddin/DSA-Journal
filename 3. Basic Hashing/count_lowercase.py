def precompute(s):
    hash_arr = [0] * 26

    for ch in s:
        hash_arr[ord(ch) - ord('a')] += 1

    return hash_arr


def fetch(hash_arr, c):
    return hash_arr[ord(c) - ord('a')]


s = input()

hash_arr = precompute(s)

q = int(input())

for _ in range(q):
    c = input()
    print(fetch(hash_arr, c))
## here ord() function is used to get the ASCII value of the character. 
# By subtracting the ASCII value of 'a' from the ASCII value of the character,
# we can get the index in the hash array corresponding to that character. 
# For example, if c is 'b', then ord('b') - ord('a') will give us 1, 
# which is the index for 'b' in the hash array.