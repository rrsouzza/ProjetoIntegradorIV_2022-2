with open('tweets.txt', 'r', encoding='utf=8') as txt_file:
  with open('parsed.txt', 'w', encoding='utf-8') as parse_file:
    indexGeral = 1
    indexUnico = 1
    revisouPrimeiroMes = False
    revisouSegundoMes = False
    revisouTerceiroMes = False
    lines = txt_file.readlines()
    for line in lines:
      if (indexUnico == 179 and not revisouPrimeiroMes):
        indexUnico = 1
        indexGeral += 1
        revisouPrimeiroMes = True
      if (indexUnico == 194 and not revisouSegundoMes):
        indexUnico = 1
        indexGeral += 1
        revisouSegundoMes = True
      
      if (line.startswith(f'{indexUnico}-')):
        line = line.replace(f'{indexUnico}', f'{indexGeral}')
        indexGeral += 1
        indexUnico += 1

      parse_file.write(f'{line}')

      

      