def ReadData(fileName, IsShow):
    import scipy.io as sio
    import numpy as np
    print('Reading data ...')
    X = sio.loadmat(fileName)
    # test_data
    # train_data
    # train_label
    # srate
    # Data['train_data'][1][1][0]  行 列 另一组数据
    # Data['train_label'][1]
    # 时间信息 0-5s 为运动想象的时间
    # 选择通道为C3 和 C4
    C3 = X['train_data'][27, 0:1000,:]
    C4 = X['train_data'][33, 0:1000,:]
    X['train_data'] = np.array([C3[:,:],C4[:,:]])
    C3 = X['test_data'][27, 0:1000,:]
    C4 = X['test_data'][33, 0:1000,:]
    X['test_data'] = np.array([C3[:,:],C4[:,:]])
    if(IsShow == 1):
        print(type(X))
    return X