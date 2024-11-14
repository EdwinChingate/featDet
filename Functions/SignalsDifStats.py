import numpy as np
def SignalsDifStats(mz_Dif):
    Average_Dif=np.mean(mz_Dif)
    std_Dif=np.std(mz_Dif)
    max_Dif=np.max(mz_Dif)
    stats_Dif=[Average_Dif,std_Dif,max_Dif]
    return stats_Dif
