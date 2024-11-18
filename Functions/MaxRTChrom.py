import numpy as np
def MaxRTChrom(DataSet,SpectraPeaks,IDVec,minInt=1e5,minSigInt=20):
# I can also change the search order, and use the information I already have to reduce my searching space
# This function is just filtering the quality of my signals, and adding the RT of the maximum signal to the main table    
    for peak_id in np.arange(len(SpectraPeaks)):
        maxIntVec=[]
        RTVec=[]
        peak=SpectraPeaks[peak_id,:]
        min_mz=peak[-2]
        max_mz=peak[-1]
        for spectrum_id in IDVec:
            spectrum=DataSet[int(spectrum_id)]
            RawSpectrum=np.array(spectrum.get_peaks()).T
            LittleSpecFil=(RawSpectrum[:,0]>min_mz)&(RawSpectrum[:,0]<max_mz)
            LittleSpec=RawSpectrum[LittleSpecFil,:]
            if len(LittleSpec)>0:
                maxInt=np.max(LittleSpec[:,1])            
                RT=spectrum.getRT()
                maxIntVec.append(maxInt)
                RTVec.append(RT)
        maxInt=np.max(maxIntVec)
        RTLoc=int(np.where(np.array(maxIntVec)==maxInt)[0][0])
        IntVecFil=np.where(np.array(maxIntVec)>minInt)[0]    
        if len(IntVecFil)>minSigInt:
            SpectraPeaks[peak_id,5]=RTVec[RTLoc]
    return SpectraPeaks
