# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 16:23:22 2016

@author: WUJIANPING
"""
import matplotlib.pyplot as plt
def plot_roc(path):
    FPR = [];
    TPR = [];
    with open(path, "r") as fp:
        for line in fp:
            #print(line)
            cols = line.split()
            FPR.append(cols[0]);
            TPR.append(cols[1]);
    
    
    return FPR, TPR
            
  

if "__main__" == __name__:
    FPR, TPR = plot_roc(r"E:\old-research\Research\Caffe\happynear\caffe-windows-master\buildVS2013\LFWTest\ROC_Points.txt")
    FPR2, TPR2 = plot_roc(r"E:\old-research\Research\Caffe\happynear\caffe-windows-master\buildVS2013\LFWTest\lcnn_ROC_Points.txt")
    plt.figure(1)
    plt.title('ROC')
    plt.xlabel("FPR")
    plt.ylabel("TPR")
    plt.plot(FPR, TPR, 'm-', label='DeepID', linewidth = 2)
    plt.plot(FPR2, TPR2, 'c-', label='LCNN', linewidth = 2)
    plt.legend(loc= 4)
    plt.show()
    plt.savefig("D:\\face_ROC.png")