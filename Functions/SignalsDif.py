def SignalsDif(Peaks):
    mz_Dif=[]
    for peak in Peaks:
        data_peak=peak[1]
        Low_mz=data_peak[:-1,0]
        High_mz=data_peak[1:,0]
        mz_Dif=list(High_mz-Low_mz)+mz_Dif
    return mz_Dif
