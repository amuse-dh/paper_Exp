import pandas as pd

def stock_manage():
    stock = pd.read_csv('C:/Users/user/PycharmProjects/pythonProject1/stock.csv')

    result = pd.read_csv('C:/Users/user/PycharmProjects/pythonProject1/result.csv')

    stock_list = stock['product'].values.tolist()

    for i in range(len(result)):
        if result.iloc[i]['product'] in stock_list:
            stock_idx = stock.index[stock['product'] == result.iloc[i]['product']].tolist()
            idx = stock_idx

            stock_cnt = stock.iloc[idx]['cnt']
            stock_cnt = stock_cnt - 1
            stock.loc[idx,'cnt'] = stock_cnt

    stock.to_csv('C:/Users/user/PycharmProjects/pythonProject1/stock.csv', index = False,mode = 'w')

    print(stock)