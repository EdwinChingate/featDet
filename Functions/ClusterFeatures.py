import numpy as np
from PondMZStats import *
from WeightPondStats import *
def ClusterFeatures(SpectraPeaks):
    SpectraPeaks=SpectraPeaks[SpectraPeaks[:, 0].argsort(),:]    
    NextLoc=np.where(SpectraPeaks[:-1,15]>SpectraPeaks[1:,14])[0]
    if len(NextLoc)==0:
        return SpectraPeaks
    NextLoc2=NextLoc+1
    DelLoc=np.append(NextLoc,NextLoc2)
    CleanSpectraPeaks=[]
    for peak_next in NextLoc:
        PeakStats1=SpectraPeaks[peak_next,:]
        PeakStats2=SpectraPeaks[peak_next+1,:]
        PeakStats=WeightPondStats(PeakStats1,PeakStats2)
        CleanSpectraPeaks.append(PeakStats)
    CleanSpectraPeaks=np.array(CleanSpectraPeaks)
    SpectraPeaks=np.delete(SpectraPeaks,DelLoc,axis=0)
    SpectraPeaks=np.append(SpectraPeaks,CleanSpectraPeaks,axis=0)
    SpectraPeaks=SpectraPeaks[SpectraPeaks[:, 0].argsort(),:]
    return SpectraPeaks
