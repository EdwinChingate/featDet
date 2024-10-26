minInt=1e2
minIntPeak=1e4
mz_Tol=1e-3
minSignals=4
def Centroids(RawSignals,minInt=1e2,minIntPeak=1e4,mz_Tol=1e-3,minSignals=4)
    # Add an intensity filter
    IntensityFilterLocator=RawSignals[:,1]>minInt
    IntensityFilter=np.where(IntensityFilterLocator)[0]
    Signals=RawSignals[IntensityFilter,:]
    ResidualSignals=Signals.copy()
    #Find the signal with the highest intensity
    maxInt=1e6
    FeaturesVec=[]
    while maxInt>minIntPeak:
        NFeatureSignals=0
        mz_Tol_Times=0
        while NFeatureSignals<minSignals:
            mz_Tol_Times+=1
            N_Old_Signals=len(ResidualSignals)
            maxInt=np.max(ResidualSignals[:,1])
            maxIntLocator=ResidualSignals[:,1]==maxInt
            mz_maxIntFilter=np.where(maxIntLocator)[0]
            mz_Feature=float(ResidualSignals[mz_maxIntFilter,0])
            minmz_Feature=mz_Feature-mz_Tol*mz_Tol_Times
            maxmz_Feature=mz_Feature+mz_Tol*mz_Tol_Times
            FeatureSignalsLocator=(ResidualSignals[:,0]>minmz_Feature)&(ResidualSignals[:,0]<maxmz_Feature)
            FeatureSignals=ResidualSignals[FeatureSignalsLocator,:]
            NFeatureSignals=len(FeatureSignals[:,0])
        MaxInt_FeatureLocator=(ResidualSignals[:,0]<minmz_Feature)|(ResidualSignals[:,0]>maxmz_Feature)
        ResidualSignals=ResidualSignals[MaxInt_FeatureLocator,:]
        N_New_Signals=len(ResidualSignals)
        FeaturesVec.append(mz_Feature)
        print(mz_Feature,NFeatureSignals,mz_Tol_Times)
    return FeaturesVec
