import json


class Model:
    title = '1'
    text = '2'
    author = '3'
    

    def save(self):
        d = {}
        attr = list(filter(lambda x: not x.startswith('_'), dir(Model)))
        attr.remove('save')
        for i in attr:
            d[i] = eval('self.' + i)
            #print(d[i])
        with open('log1.json', 'w') as f:
            json.dump(d, f)
        return print(d)


model1 = Model()
model1.title = '7'
model1.text = '8'
model1.author = '9'
#print(test.a)
model1.save()