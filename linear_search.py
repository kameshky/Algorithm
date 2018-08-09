def linear_search(given_numbers, search_number):
    for n in range(len(given_numbers)):
        if(given_numbers[n] == search_number):
            return n
    return "Not Found"


print("Provide numbers with comma in between")
given_no = list(map(int,input().replace(" ","").split(',')))
print("What number to search:",end="")
search_no = int(input())

print(linear_search(given_no, search_no))