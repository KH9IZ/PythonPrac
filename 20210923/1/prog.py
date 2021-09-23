num = int(input())


print(f"A {'+' if num % 2 == 0 and num % 25 == 0 else '-'} "
      f"B {'+' if num % 2 and num % 25 == 0 else '-'} "
      f"C {'+' if num  % 8 == 0 else '-'}") 
