def ReadData(fileName, IsShow):
    import scipy.io as sio
    import numpy as np
    print('正在读取数据中 》》》')
    X = sio.loadmat(fileName)
    # test_data
    # train_data
    # train_label
    # srate
    # Data['train_data'][1][1][0]  行 列 另一组数据
    # Data['train_label'][1]
    # 时间信息 0-5s 为运动想象的时间
    C3 = X['train_data'][27, 0:1000,:]
    C4 = X['train_data'][33, 0:1000,:]
    X['train_data'] = ([C3]
    [C4])
    print(type(C3))
    if(IsShow == 1):
        print(type(X))
    return X