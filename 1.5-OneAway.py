def oneaway(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    elif len(s1) - len(s2) == 1:
        return oneinsert(s1, s2)
    elif len(s1) - len(s2) == -1:
        return oneinsert(s2, s1)
    else:
        return onereplace(s1, s2)

def oneinsert(s1, s2):
    index1 = 0
    index2 = 0
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            elif index1 == index2:
                index1 += 1
        elif s1[index1] == s2[index2]:
            index1 += 1
            index2 += 1
    return True

def onereplace(s1, s2):
    difference = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if difference is True:
                return False
            else:
                difference = True
    return True

oneaway("apple", "aple")
oneaway("pile", "pie")