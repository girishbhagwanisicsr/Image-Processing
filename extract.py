import json


def extract_amount(filen):

    with open(filen, 'r') as access_json:
        read_content = json.load(access_json)
        for i in range(0, 20):
            accessing = read_content['Blocks'][i]
            if 'Text' in accessing:
                if accessing['Text']:
                    if accessing['Text'].startswith('$'):
                        amount = accessing['Text']
        return amount


filena = input("Enter the File Name With Path ")
print("amount is ", extract_amount(filena))
