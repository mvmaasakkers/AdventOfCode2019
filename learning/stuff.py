# l = ['One', 'Two', 'Three']
# l.append('Four')
# l.remove('Two')

# print(l)

# slang = {'cheerio': 'goodbye', 'rubbish': 'trash'}
# slang['smashing'] = 'terrific'
# del slang['cheerio']

# print(slang.get('rubbish'))
# if slang.get('cheerio'):
#     print(slang.get('cheerio'))
# else:
#     print("Nonne")
# print(slang)


non_flat = [ [1,2,3], [4,5,6], [7,8] ]
print([y for x in non_flat for y in x])
