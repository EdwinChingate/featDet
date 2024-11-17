from ClusterFeatures import *
import numpy as np
from PondMZStats import *
from WeightPondStats import *
from PeaksFindDif import *
def featDet(SpectraList,ZeroInt=1e2,min_mz=200,max_mz=300,minSignals=30,minQuality=1,stdDistance=4):
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
            if len(PeakData[:,0])>minSignals:        
                Expected_std_mz=PeakStats1[1]
                PeakStats2=PondMZStats(PeakData,minSignals=minSignals,Expected_std_mz=Expected_std_mz,stdDistance=stdDistance)
                if type(PeakStats2)!=type(0):
                    PeakStats=WeightPondStats(PeakStats1,PeakStats2)
                    SpectraPeaks[peak_position,:]=PeakStats
                    min_mz_peak=PeakStats[-2]
                    max_mz_peak=PeakStats[-1]
                    peakFilter=(SampleSpectra[:,0]>min_mz_peak)&(SampleSpectra[:,0]<max_mz_peak)&(SampleSpectra[:,1]>ZeroInt)
            SampleSpectra[peakFilter,1]=0
        NewPeaks=PeaksFindDif(SampleSpectra,min_mz=min_mz,max_mz=max_mz,minQuality=minQuality,minSignals=minSignals,stdDistance=stdDistance)
        if FirstSpectra:
            SpectraPeaks=NewPeaks
            FirstSpectra=False
        elif type(NewPeaks)!=type(0):
            SpectraPeaks=np.append(SpectraPeaks,NewPeaks,axis=0)
            SpectraPeaks=ClusterFeatures(SpectraPeaks)
    SpectraPeaks=ClusterFeatures(SpectraPeaks)    
    return SpectraPeaks


