import numpy as np
import pandas as pd
from PyQt5 import QtCore
import struct
class metadata:
    # this is the metadata structure that need's
    MetaDataSignal = QtCore.pyqtSignal(int)
    def __init__(self, n=1):
        self.channel = n
        self.DataStreamList = []
        for i in range(self.channel+1):
            self.DataStreamList.append([])

    def save(self, path, mode = 'w'):
        dic_res = {"T":self.DataStreamList[0]}
        for i in range(5):
            print(len(self.DataStreamList[i]))
        if mode=='w':
            for i in range(1, self.channel):
                dic_res["Data-{}".format(i)] = self.DataStreamList[i]

        xml_df = pd.DataFrame(dic_res, index=None)
        xml_df.to_csv(path, index=None, mode=mode)
        print("Save Successfully! {}".format(path))

    def Datasplit(self, ans, msg):
        if ans==0:
            datas = struct.unpack('<iiiii', msg)
            for i in range(self.channel):
                self.DataStreamList[i].append(datas[i])

        self.MetaDataSignal.emit(ans)

if __name__ == '__main__':
    D = metadata()
    # D.fill()
    D.save("./1.csv", "a")
