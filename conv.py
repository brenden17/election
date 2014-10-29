import pandas as pd

def convert_df2json2(df):
    if not isinstance(df, pd.DataFrame):
        return df

    items = list()
    print('[')
    for i, row in enumerate(df.values):
        l = list()
#             l.append(('identifier', df.index[i]))
        for j, colname in enumerate(df.columns):
            if colname == 'party' or colname == 'local' or colname == 'date':
                s = '{}: "{}"'.format(colname, row[j])
                l.append(s)
            elif colname == 'Unnamed: 0':
                pass
            else:
                s = '{}: {}'.format(colname, row[j])
                l.append(s)
        ss = ', '.join(l)

        print('{{{}}},'.format(ss))
    print(']')

df = pd.read_csv('data/all_t3.csv')
convert_df2json2(df)

