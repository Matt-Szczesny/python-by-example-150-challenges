num = 10

while num > 0:

    print(f"""There are {num} green bottles hanging on the wall, 
          {num} green bottles hanging on the wall, 
          and if 1 green bottle should accidentally fall""")

    ans = ""
    num -= 1
    
    while num != ans:
        ans = int(input("how many green bottles will be hanging on the wall? "))
        print("Try again!")
    else:
        print(f"There will be {num} green bottles hanging on the wall")

else:
    print("There are no more green bottles hanging on the wall")