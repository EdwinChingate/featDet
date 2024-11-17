import numpy as np
from PeaksIdent import *
from PondMZStats import *
def PeaksFindDif(RawSignals,ZeroInt=1e4,min_mz=0,max_mz=1000,JustStats=True,PeaksSafetyFactor=2,DiffromPeaks=10,stdDistance=4,PeaksNumber=10,minSignals=30,minQuality=10):
    # It's using another algorithm to analize a fraction of the spectrum and get a reference value for the DifTres parameter
    min_mz=max([np.min(RawSignals[:,0]),min_mz])
    Peaks=PeaksIdent(RawSignals,minInt=ZeroInt,min_mz=min_mz,max_mz=max_mz,JustStats=True, PeaksNumber=PeaksNumber,minSignals=minSignals)
    if len(Peaks)==0:
        return 0
    DifTres=np.max(Peaks[:,10])
    Expected_std_mz=np.median(Peaks[:,1])
    DiffromPeaksVec=np.ones(DiffromPeaks)*DifTres
    Expected_std_mzVec=np.ones(DiffromPeaks)*Expected_std_mz
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
        PeakStats=PondMZStats(PeakData,minSignals=minSignals,Expected_std_mz=Expected_std_mz,stdDistance=stdDistance)             
        if type(PeakStats)!=type(0):
            DifPeakLoc=peaks_count%DiffromPeaks
            DiffromPeaksVec[DifPeakLoc]=PeakStats[10]
            Expected_std_mzVec[DifPeakLoc]=PeakStats[1]
            DifTres=np.median(DiffromPeaksVec)
            peaks_count+=1
            if JustStats:
                SpectrumPeaks.append(PeakStats)       
            else:            
                SpectrumPeaks.append([PeakStats,PeakData]) 
        min_mz_loc=max_mz_loc  
    if len(SpectrumPeaks)==0:
        return 0
    if JustStats:
        SpectrumPeaks=np.array(SpectrumPeaks) 
        QualityLoc=SpectrumPeaks[:,4]>minQuality
        SpectrumPeaks=SpectrumPeaks[QualityLoc,:]
    return SpectrumPeaks
