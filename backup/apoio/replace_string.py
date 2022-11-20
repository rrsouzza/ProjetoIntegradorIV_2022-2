data = [
  '1-Teste 123',
  '2-Teste 123',
  '3-Teste 123',
  '4-Teste 123',
  '5-Teste 123',
  '6-Teste 123',
  '7-Teste 123',
  '8-Teste 123',
  '9-Teste 123',
  '10-Teste 123',
  '11-Teste 123',
  '12-Teste 123',
  '13-Teste 123',
  '14-Teste 123',
  '15-Teste 123',
  '101-Teste 123',
  '102-Teste 123',
  '103-Teste 123',
  '104-Teste 123',
  '105-Teste 123',
  '106-Teste 123',
]

index = 1

for line in data:
  if line[1] == '-':
    print(line)
    line = line[2:]
    print(line)
  if line[2] == '-':
    print(line)
    line = line[3:]
    print(line)
  if line[3] == '-':
    print(line)
    line = line[4:]
    print(line)
