chapter_code = {
  'A': [
    {
      'range_start': 0,
      'range_end': 99,
      'chapter': '1',
      'name': 'Certain infectious and parasitic diseases'
    }
  ],
  'B': [
    {
      'range_start': 0,
      'range_end': 99,
      'chapter': '1',
      'name': 'Certain infectious and parasitic diseases'
    },
    #{
     # 'range_start': 59,
     # 'range_end': 99,
     # 'chapter': '1',
     # 'name': 'Certain infectious and parasitic diseases'
    #},
  ],
}


def getChapterName(kode):
  # from excel file
  code_character = kode[0:1]
  range_character = int(kode[1:3])

  # chapter code
  character_code_list = chapter_code[code_character]


  for list in character_code_list:
    if(range_character >= list['range_start'] and range_character <= list['range_end']):
      # chapter name
      return list['name']
