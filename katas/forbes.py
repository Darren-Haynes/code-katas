"""Return the name, net worth, and industry of billionaires."""


def parse_key_value(line):
    """Get key, value data from line passed in."""
    line = line.strip()
    line = line.rstrip(',')
    line = line.replace('"', '')
    key, value = line.split(': ')
    return key, value


def billionaires():
    """Get youngest billionare and oldest billionaire under 80."""
    with open('forbes_billionaires_2016.json', 'r') as f:
        youngest = {'name': None, 'age': 1000}
        under80 = {'name': None, 'age': -1}
        temp = {}
        for line in f:
            if '"name":' in line:
                key, value = parse_key_value(line)
                temp[key] = value
            if '"age":' in line:
                key, value = parse_key_value(line)
                temp[key] = int(value)
            if '"net_worth (USD)":' in line:
                key, value = parse_key_value(line)
                temp[key] = int(value)
            if '"source":' in line:
                key, value = parse_key_value(line)
                temp[key] = value
            if '},' in line:
                if temp['age'] < 80 and temp['age'] > under80['age']:
                    for k in temp:
                        under80[k] = temp[k]
                if temp['age'] < youngest['age'] and temp['age'] > 0:
                    for k in temp:
                        youngest[k] = temp[k]

        return youngest, under80
