import numpy as np
def SamplingSpectra(RawSpectra,SampleFraction=30):
    N_datapoints=len(RawSpectra[:,0])
    SampleSize=int(N_datapoints*SampleFraction/100)
    SampleIndex=np.linspace(0,N_datapoints-1,SampleSize,dtype='int')
    RandomVec=(np.random.rand(SampleSize-2)-0.5)*int(100/SampleFraction)
    RandomVec=np.array(RandomVec,dtype='int')
    SampleIndex[1:-1]=SampleIndex[1:-1]+RandomVec
    SampleSpectra=RawSpectra[SampleIndex,:]
    return SampleSpectra
