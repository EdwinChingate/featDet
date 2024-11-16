from PondMZStats import *
import numpy as np
# Add the Welch test to compare all the peaks
# Add r2 calculation for Gaussian models
# Consider deconvolution with Gaussian models
def PeaksIdent(RawSignals,minInt=1e2,min_mz=0,max_mz=1000,minSignals=4,JustStats=True,stdDistance=3, PeaksNumber=0):
    Signals_filter=(RawSignals[:,0]<max_mz)&(RawSignals[:,0]>min_mz)
    Signals=RawSignals[Signals_filter,:]
    Filter=Signals[:,1]<minInt #Identify low intensity signals
    FilterLoc=np.where(Filter)[0] #Get the indices of evaluated mz with low intensity 
    # Evaluate the number of mz with a higher intensity between the ones with low intensity
    DifLoc=FilterLoc[1:]-FilterLoc[:-1] 
    DifLocFilter=DifLoc>minSignals
    # Find the mz clusters containing more signals than the defined
    DifLocLoc=np.where(DifLocFilter)[0] 
    SpectrumPeaks=[]
    if PeaksNumber>0:
        DifLocLoc=DifLocLoc[:PeaksNumber]
    for filterLocID in DifLocLoc:
        min_mz_loc=FilterLoc[filterLocID]+1
        max_mz_loc=FilterLoc[filterLocID+1]
        PeakData=Signals[min_mz_loc:max_mz_loc,:]
        minMZ=np.min(PeakData[:,0])
        maxMZ=np.max(PeakData[:,0])
        PeakStats=PondMZStats(PeakData)
        if type(PeakStats)!=type(0):
            if JustStats:
                SpectrumPeaks.append(PeakStats)       
            else:            
                SpectrumPeaks.append([PeakStats,PeakData]) 
    if JustStats:
        SpectrumPeaks=np.array(SpectrumPeaks)
    return SpectrumPeaks
