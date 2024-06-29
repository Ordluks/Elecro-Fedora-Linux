from re import match

def confirm(message) -> bool:
  result = input(message + '? (Y/n) ')
  if result == '':
    return True
  elif not match('^[YNyn]$', result):
    print('Please enter y or n')
    return confirm(message)
  else:
    return result.capitalize() == 'Y'