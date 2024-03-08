
def reverseWords(s: str) -> str:
        sep = s.split(" ")[::-1]
        return " ".join([ i for i in sep if i != "" ])

def areAlmostEqual(s1: str, s2: str) -> bool:
        if s1 == s2: 
            return True 
            
        m = [0] * 26
        for i, j in zip(s1, s2):
            m[ord(i) - ord('a')] += 1
            m[ord(j) - ord('a')] -= 1

        if not all(counts == 0 for counts in m):
            return False

        count = 0
        for i, j in zip(s1, s2):
            if i != j: 
                count += 1

        return count <= 2 

def main():
    s = "  hello world  "
    print(reverseWords(s))


if __name__ == '__main__':
        main()