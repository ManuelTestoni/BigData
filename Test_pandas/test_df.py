import pandas as pd

def test_df():
    ds=pd.DataFrame({'foo':[1,2,6],'fee':[3,4,5]})
    print(ds)

    ds=pd.DataFrame({'foo':{'a':1,'b':1},'fee':{'c':1,'d':2}})
    print(ds)

if __name__ == '__main__':
    test_df()