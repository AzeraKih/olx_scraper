import json

class item_class:
    name = ''
    price = ''
    location = ''
    date = ''
    hour = ''
    def __init__(self, name, price, location, date, hour):
        self.name = name
        self.price = price
        self.location = location
        self.date = date
        self.hour = hour
    
    def __str__(self):
        return (
            'Nome: ' + self.name +
            '\nPreço: ' + self.price + 
            '\nLocalidade: ' + self.location +
            '\nData: ' + self.date +
            '\nHora: ' + self.hour 
            )

    def __iter__(self):
        yield 'name', self.name
        yield 'price', self.price
        yield 'location', self.location
        yield 'date', self.date
        yield 'hour', self.hour

    @staticmethod
    def read_data(file_name):
        products = []
        with open('%s.json'%file_name, 'r+') as json_file:
            data = json.load(json_file)
            for p in data:
                products.append(item_class(p['name'], p['price'], p['location'], p['date'], p['hour']))
        return products

    @staticmethod
    def save_data(file_name, arr):
        
        arrJSON = [dict(a) for a in arr]

        with open('%s.json'%file_name, 'w+') as f:
            json.dump(arrJSON, f, indent=4)
        return True
        
    @staticmethod
    def find(arr, ID):
        
        name = ID[0:ID.rfind(' - ')]
        hour = ID[ID.rfind(' - ')+3:]
        for a in arr:
            if a.name == name and a.hour == hour:
                return a
        return True