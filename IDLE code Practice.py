"""def countTeams(skills, minPlayers, minLevel, maxLevel):
    valid_skills = [skill for skill in skills if minLevel <= skill <= maxLevel]

    def generate_combinations(arr, n):
        result = []
        def backtrack(start, path):
            if len(path) == n:
                result.append(path[:])
                return
            for i in range(start, len(arr)):
                path.append(arr[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return result
    count = 0
    n = len(valid_skills)
    for i in range(minPlayers, n + 1):
        count += len(generate_combinations(valid_skills, i))
    return count
skills = [4,8,5,6]
minPlayers = 1
minLevel = 5
maxLevel = 7
print(countTeams(skills, minPlayers, minLevel, maxLevel))"""


p=int(input("enter a number : "))
k=str(p)


a=k
b=k[::-1]
print(a,'\n',b)
if(a==b):
    print("the number is palindrome")
else:
    print("not pali")
















