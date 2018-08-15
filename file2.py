

# load text from invoice.txt and suppliernames.txt into invoice and suppliers:
with open('C:\\Users\\nongn\\Desktop\\Xtracta\\invoice.txt', 'r', )as f:
    invoice = f.readlines()
with open('C:\\Users\\nongn\\Desktop\\Xtracta\\suppliernames.txt', 'r')as f:
    suppliers = f.readlines()

def get_company_id():
    '''
    draw out company name from invoice，and match it with the given list of suppliernames
    :return: supplier which consists of name and id
    '''
    a = []  # store info of line 4
    b = []  # resort by 'pos_id'
    c = []  # store info before word 'Due'
    word = ''
    # find all words in line 4, and only keep suppilernames left
    for i in invoice:
        i = eval(i)
        if i['line_id'] == 4:
            a.append(i)
            b.append('')
        
    for n in a:
        b[n['pos_id']] = n
        
    for m in b:
        if m['word'] != 'Due':
            c.append(m)
        else:
            break   # Find all text before 'Due', once retrieve the 'Due', then break out of the loop 
    for j in c:
        word += j['word']   # merge all words together 

    # match and find the supplier in the list of suppliernames.txt,removing the white place
    for supplier in suppliers:
        if word.replace(' ', '') in supplier.replace(' ', ''):
            return supplier

def get_price():
    '''
    get the price details and 
    :return: price = {'shipping': '', 'subtotal': '', 'total': '', 'payments': '', 'banlancedue': ''}
    '''
    price = {}
    for i in invoice:
        i = eval(i)
        if i['line_id'] == 13:
            if i['pos_id'] == 9:
                price['Shipping'] = i['word']
        if i['line_id'] == 19:
            if i['pos_id'] == 3:
                price['Tax'] = i['word']
        if i['line_id'] == 19:
            if i['pos_id'] == 5:
                price['Subtotal'] = i['word']
        if i['line_id'] == 20:
            if i['pos_id'] == 3:
                price['Total'] = i['word']
        if i['line_id'] == 21:
            if i['pos_id'] == 2:
                price['Payments'] = i['word']
        if i['line_id'] == 22:
            if i['pos_id'] == 2:
                price['Banlance Due'] = i['word']
    return price

if __name__ == '__main__':
    id = get_company_id()
    price = get_price()
    print(id)
    print(price)
	
	