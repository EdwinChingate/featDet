from PondMZStats import *
from WeightPondStats import *
from PeaksFindDif import *
import numpy as np
def featDet(SpectraList,ZeroInt=1e2,min_mz=200,max_mz=300):
    FirstSpectra=True
    SpectraPeaks=[]
    for Spectra in SpectraList:
        SampleSpectra=Spectra.copy()
        N_Peaks=len(SpectraPeaks)
        for peak_position in np.arange(N_Peaks,dtype='int'):
            PeakStats1=SpectraPeaks[peak_position,:]
            min_mz_peak=PeakStats1[-2]
            max_mz_peak=PeakStats1[-1]
            peakFilter=(SampleSpectra[:,0]>min_mz_peak)&(SampleSpectra[:,0]<max_mz_peak)&(SampleSpectra[:,1]>ZeroInt)
            PeakData=SampleSpectra[peakFilter,:]
            if len(PeakData[:,0])>10:
                SampleSpectra[peakFilter,1]=0
                PeakStats2=PondMZStats(PeakData)
                PeakStats=WeightPondStats(PeakStats1,PeakStats2)
                SpectraPeaks[peak_position,:]=PeakStats
        NewPeaks=PeaksFindDif(SampleSpectra,min_mz=min_mz,max_mz=max_mz)
        if FirstSpectra:
            SpectraPeaks=NewPeaks
            FirstSpectra=False
        elif type(NewPeaks)!=type(0):
            SpectraPeaks=np.append(SpectraPeaks,NewPeaks,axis=0)
    SpectraPeaks=SpectraPeaks[SpectraPeaks[:, 0].argsort(),:]
    return SpectraPeaks
