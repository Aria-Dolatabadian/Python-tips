def func():
    DNA="UTCAAUTCAAUTC"
    i=[]
    while True:
        if 'UTC' in DNA:
            i.append(DNA.find('UTC'))
            DNA=DNA.replace('UTC','utc',1)
        else:
            break
    print(i)
func()
