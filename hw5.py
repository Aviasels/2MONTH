designations = []
codes = []

data = ('O!', 'Megacom', '0705', 'Beeline', '0550', '0770', 'Katel', '0510','Fonex', '0543' )
for item in data:
    if item.isalpha() or "!" in item:
        designations.append(item)
    elif item.isdigit():
        codes.append(item)

numbers = {}
for name, code in zip(designations,
          codes):
    if name not in numbers:
        numbers[name] = set()
    numbers[name].add(code)

numbers.pop("Katel", None)
numbers.pop("Fonex", None)

numbers['O!']. update(['0700', '0500'])
numbers['Megacom'].update(['0999','0555'])
numbers['Beeline'].update(['0222', '0777'])

for numbers, code_set in numbers.items():
    print(f'{numbers} = {code_set}')








