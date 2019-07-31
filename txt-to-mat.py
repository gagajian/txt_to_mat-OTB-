import os
import scipy.io as scio
import numpy as np

file = '/**/model/'  #your txt path
savefile = '/**/result/'  # your mat file path
pathlist = os.listdir(file)
# print(pathlist)

for i in range(len(pathlist)):
    path = os.path.join(file, pathlist[i])
    for j in range(len(pathlist[i])):
        if pathlist[i][j] == '.':
            save = pathlist[i][:j]
            break
    savepath = savefile + save + '_SiamRPN++.mat'

    f = open(path)
    data = f.readlines()
    result = []
    for j in range(len(data)):
        x = data[j].split(',')
        x[3] = float(x[3][:-1])
        x[0] = float(x[0])
        x[1] = float(x[1])
        x[2] = float(x[2])
        result.append(x)

    res = {}
    res['res'] = result
    res['type'] = 'rect'
    Mat = {'res': res['res'], 'type': 'rect', 'len': len(res['res']), 'annoBegin': 1, 'startFrame': 1}
    M = np.array([Mat])
    Mat2 = {'__header__': 'b', '__version__': 1.0, '__globals__': [], 'results': M}
    scio.savemat(savepath, Mat2)
    # print(data)
