from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

result2 = get_file_content("calculator", "main.py")
print(f"actual output of function: {result2}")
print(f"output length: {len(result2)}")
print(f"output truncated: {'truncated' in result2}")

result3 = get_file_content("calculator", "pkg/calculator.py")
print(f"actual output of function: {result3}")
print(f"output length: {len(result3)}")
print(f"output truncated: {'truncated' in result3}")

result4 = get_file_content("calculator", "/bin/cat")
print(f"actual output of function: {result4}")
print(f"output length: {len(result4)}")
print(f"output truncated: {'truncated' in result4}")

result5 = get_file_content("calculator", "pkg/does_not_exist.py")
print(f"actual output of function: {result5}")
print(f"output length: {len(result5)}")
print(f"output truncated: {'truncated' in result5}")
