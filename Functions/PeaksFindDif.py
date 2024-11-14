import numpy as np
from PeaksIdent import *
def PeaksFindDif(RawSignals,ZeroInt=1e2,min_mz=0,max_mz=1000,plus_mz=2,minSignals=4,JustStats=True,PeaksSafetyFactor=2,DiffromPeaks=10):
    # It's using another algorithm to analize a fraction of the spectrum and get a reference value for the DifTres parameter
    min_mz=max([np.min(RawSignals[:,0]),min_mz])
    min_mzplus=min_mz+plus_mz
    Peaks=PeaksIdent(RawSignals,minInt=ZeroInt,min_mz=min_mz,max_mz=min_mzplus,minSignals=4,JustStats=True)
    DifTres=np.max(Peaks[:,10])
    DiffromPeaksVec=np.ones(DiffromPeaks)*DifTres
    # Filter the signals and reducing the size of the dataset
    Signals_filter=(RawSignals[:,0]<max_mz)&(RawSignals[:,0]>min_mz)&(RawSignals[:,1]>ZeroInt)
    Signals=RawSignals[Signals_filter,:]
    Signals=np.append(Signals,np.matrix([Signals[-1,0]+10,1e5]),axis=0)
    Dif_mz_vec=Signals[1:,0]-Signals[:-1,0]
    min_mz_loc=0
    L_Right_loc=5
    SpectrumPeaks=[]
    peaks_count=0
    while True:
        Right_loc=np.where(Dif_mz_vec>DifTres*PeaksSafetyFactor)[0]
        L_Right_loc=len(Right_loc)
        if L_Right_loc==0:
            break
        Loc_Right_loc=np.where(Right_loc>min_mz_loc)[0]
        if len(Loc_Right_loc)==0:
            break
        max_mz_loc=Right_loc[Loc_Right_loc[0]]+1
        PeakData=Signals[min_mz_loc:max_mz_loc,:]
        minMZ=np.min(PeakData[:,0])
        maxMZ=np.max(PeakData[:,0])
        PeakStats=PondMZStats(PeakData)             
        if type(PeakStats)!=type(0):
            DifPeakLoc=peaks_count%DiffromPeaks
            DiffromPeaksVec[DifPeakLoc]=PeakStats[10]
            DifTres=np.mean(DiffromPeaksVec)
            PeakStats.append(minMZ)
            PeakStats.append(maxMZ)
            PeakStats.append(PeakStats[0]-3*PeakStats[1])
            PeakStats.append(PeakStats[0]+3*PeakStats[1])
            peaks_count+=1
            if JustStats:
                SpectrumPeaks.append(PeakStats)       
            else:            
                SpectrumPeaks.append([PeakStats,PeakData]) 
        min_mz_loc=max_mz_loc

    if JustStats:
        SpectrumPeaks=np.array(SpectrumPeaks)    
    return SpectrumPeaks
