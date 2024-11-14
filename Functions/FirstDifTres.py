from PeaksIdent import *
from SignalsDif import *
from SignalsDifStats import *
def FirstDifTres(RawSignals,FirstSignals=100,min_mz=0,max_mz=1000):
    Signals_filter=(RawSignals[:,0]<max_mz)&(RawSignals[:,0]>min_mz)
    Signals=RawSignals[Signals_filter,:]    
    Peaks=PeaksIdent(Signals[:FirstSignals,:],JustStats=False)
    mz_Dif=SignalsDif(Peaks)
    stats_Dif=SignalsDifStats(mz_Dif)
    return stats_Dif
