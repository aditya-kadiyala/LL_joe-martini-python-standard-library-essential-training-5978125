testcontent = "Che guevara was cheeky while eating quiche"
teststring = "che"

def find_occurrences(content, test):
    # result = 0
    # return result
    content = content.lower()
    test = test.lower()

    starts_with = content.startswith(test)
    ends_with = content.endswith(test)
    
    starts_or_ends_with = starts_with or ends_with   # 1
    starts_and_ends_with = starts_with and ends_with # 2 

    contains = test in content # This was wrong way - Question was not clear (contains inside excluding first and last char)
    contains = content.find(test, 1, len(content)-1) != -1

    does_not_starts_or_ends_with = not starts_or_ends_with
    contains_but_does_not_start_or_end_with = contains and does_not_starts_or_ends_with # 3
  

    if contains and starts_and_ends_with:
      return 3
    
    elif starts_or_ends_with or (contains_but_does_not_start_or_end_with):
        return 1
    
    elif starts_and_ends_with or (contains and starts_or_ends_with):
        return 2
    
    else:
        return 0
    
testcontent = "Cheekiness"
teststring = "che"
assert find_occurrences(testcontent, teststring) == 1
# assert find_occurrences(testcontent, teststring) == 2

print(find_occurrences(testcontent, teststring))


# Solution
def find_occurrences_solution(content, test):
    result = 0
    content = content.lower()
    test = test.lower()

    if content.find(test, 1, len(content) - 1) != -1:
      result += 1
    
    if content.startswith(test):
       result += 1
    
    if content.endswith(test):
       result += 1

    return result