#Using Generators Calculate the following series:-
#1+4+9+16+25+36

def series():
    sumresult=0
    counter=1
    while(counter <=6):
        sumresult+=counter*counter
        if(counter==3):
            yield(sumresult)
        if(counter==5):
            yield(sumresult)
        counter+=1
    yield(sumresult)
    print("Evaluation Done")
result = series()
print(type(result))
for x in result:
    print(x)
