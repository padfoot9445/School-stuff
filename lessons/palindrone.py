def palindrome(_input: list):
    input_len = len(_input)
    if input_len % 2:
        _input.pop(input_len // 2)
        return palindrome(_input)
    return _input[0:(input_len // 2)] == list(reversed(_input[(input_len // 2):]))
#clear whitespace and case and make into a list
while True:
  __input = input()
  if palindrome([i for i in __input if i.isalpha()]):
      print(f"{__input} is a palindrome.")
  else:
      print(f"{__input} is not a palindrome.")