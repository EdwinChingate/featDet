from PondMZStats import *
import numpy as np
# Add the Welch test to compare all the peaks
# Add r2 calculation for Gaussian models
# Consider deconvolution with Gaussian models
def PeaksIdent(RawSignals,minInt=1e2,minSignals=4):
    Filter=RawSignals[:,1]<minInt #Identify low intensity signals
    FilterLoc=np.where(Filter)[0] #Get the indices of evaluated mz with low intensity 
    # Evaluate the number of mz with a higher intensity between the ones with low intensity
    DifLoc=FilterLoc[1:]-FilterLoc[:-1] 
    DifLocFilter=DifLoc>minSignals
    # Find the mz clusters containing more signals than the defined
    DifLocLoc=np.where(DifLocFilter)[0] 
    SpectrumPeaks=[]
    for filterLocID in DifLocLoc:
        min_mz_loc=FilterLoc[filterLocID]+1
        max_mz_loc=FilterLoc[filterLocID+1]
        PeakStats=PondMZStats(RawSignals[min_mz_loc:max_mz_loc,:])
        SpectrumPeaks.append(PeakStats)        
    SpectrumPeaks=np.array(SpectrumPeaks)
    return SpectrumPeaks
