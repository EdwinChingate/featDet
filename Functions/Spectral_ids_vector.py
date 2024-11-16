import numpy as np
def Spectral_ids_vector(DataSet,MS1IDVec,RTslice=10):
    LastSpec_Id=int(MS1IDVec[-1])
    TotalRT=DataSet[LastSpec_Id].getRT()
    DataSetSlicing=int(TotalRT/RTslice)
    N_spectra=len(MS1IDVec)
    SpectraClusters=np.linspace(0,N_spectra+1,DataSetSlicing+1,dtype='int')
    return SpectraClusters
