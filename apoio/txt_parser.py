def printFile():
  with open('tweets.txt') as txt_file:
    for line in txt_file:
      line = line.rstrip()
      if (line.__len__() > 2):
        print(f'line: {line}')

def teste1():
  with open('tweets.txt') as txt_file:
    with open('./apoio/tweets_parsed.txt', 'w') as txt_parsed:
      for line in txt_file:
        line = line.rstrip();
        if (line.__len__() > 2):
          print(f'line: {line}')
          next_line = next(txt_file)
          print(f'nextLine: ', {str(next_line)})
          final_line = ''
          if (line.endswith(';')):
            final_line = line
          else:
            final_line = f'{line}. {next_line}'
          print(f'final_line: {final_line}')

def teste2():
  with open('tweets.txt') as txt_file:
    # lines = txt_file.read().splitlines(keepends=True)
    lines = txt_file.readlines()
    for index, line in enumerate(lines):
      if (not line.__len__() >= 2):
        lines.pop(index)
      
    with open('./apoio/tweets_parsed.txt', 'w') as txt_parsed:
      length = len(lines)
      index = 0
      while (index <= length):
        try:
          current_line = lines[index].rstrip()
        except Exception as e:
          # print(f'Error: {e}')
          current_line = ''

        try:
          next_first_line = lines[index + 1].rstrip()
        except Exception as e:
          # print(f'Error: {e}')
          next_first_line = ''

        try:
          next_second_line = lines[index + 2].rstrip()
        except Exception as e:
          # print(f'Error: {e}')
          next_second_line = ''

        try:
          next_third_line = lines[index + 3].rstrip()
        except Exception as e:
          # print(f'Error: {e}')
          next_third_line = ''

        try:
          next_fourth_line = lines[index + 4].rstrip()
        except Exception as e:
          # print(f'Error: {e}')
          next_fourth_line = ''

        try:
          next_fifth_line = lines[index + 5].rstrip()
        except Exception as e:
          # print(f'Error: {e}')
          next_fifth_line = ''

        try:
          next_sixth_line = lines[index + 6].rstrip()
        except Exception as e:
          # print(f'Error: {e}')
          next_sixth_line = ''

        try:
          next_seventh_line = lines[index + 7].rstrip()
        except Exception as e:
          # print(f'Error: {e}')
          next_seventh_line = ''

        final_line = ''

        # print(f'---------current_line----------- {current_line}')
        # print(f'---------next_first_line----------- {next_first_line}')
        # print(f'---------next_second_line----------- {next_second_line}')
        # print(f'---------next_third_line----------- {next_third_line}')
        # print(f'---------next_fourth_line----------- {next_fourth_line}')
        # print(f'---------next_fifth_line----------- {next_fifth_line}')
        # print(f'---------next_sixth_line----------- {next_sixth_line}')
        # print(f'---------next_seventh_line----------- {next_seventh_line}')

        if (current_line.endswith(';')):
          final_line = current_line
          index = index + 1
        elif (next_first_line.endswith(';')):
          final_line = f'{current_line} {next_first_line}'
          index = index + 2
        elif (next_second_line.endswith(';')):
          final_line = f'{current_line} {next_first_line} {next_second_line}'
          index = index + 3
        elif (next_third_line.endswith(';')):
          final_line = f'{current_line} {next_first_line} {next_second_line} {next_third_line}'
          index = index + 4
        elif (next_fourth_line.endswith(';')):
          final_line = f'{current_line} {next_first_line} {next_second_line} {next_third_line} {next_fourth_line}'
          index = index + 5
        elif (next_fifth_line.endswith(';')):
          final_line = f'{current_line} {next_first_line} {next_second_line} {next_third_line} {next_fourth_line} {next_fifth_line}'
          index = index + 6
        elif (next_sixth_line.endswith(';')):
          final_line = f'{current_line} {next_first_line} {next_second_line} {next_third_line} {next_fourth_line} {next_fifth_line} {next_sixth_line}'
          index = index + 7
        elif (next_seventh_line.endswith(';')):
          final_line = f'{current_line} {next_first_line} {next_second_line} {next_third_line} {next_fourth_line} {next_fifth_line} {next_sixth_line} {next_seventh_line}'
          index = index + 8

        txt_parsed.write(f'{final_line}\n')
        
        # print(f'final_line: {final_line}')
        # print(f'index: {index}')

        if (final_line == '' and next_first_line == '' and next_second_line == '' and next_third_line == '' and next_fourth_line == '' and next_fifth_line == '' and next_sixth_line == '' and next_seventh_line == ''):
          break
                
# printFile()

teste2()