Families={
    'Charley':
        {'sam':{'boxy','rosy'},
         'Nila':{'Pespsi'}},
    'Devi':
        {
            'Tommy':{'Tony'},
            'Timmy':{'Hamster'},
            'Tammy':{'Hamster'},
        },
    'Carlos':
        {'Diego':'cat','ferret':'Fox'}
        
}

for Parent,Children in Families.items():
    print(f"{Parent} has {len(Children)} Kid(s):")
    print(f" {',and '.join([str(Child) for Child in[*Children]])}")
#100 400 700 600 900 500 800 200 300
#700 900 600 400 800 300 200 500 100