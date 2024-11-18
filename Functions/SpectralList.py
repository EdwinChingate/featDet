from JoiningSpectra import *
from SamplingSpectra import *
from Spectral_ids_vector import *
def SpectralList(DataSet,IDVec,RTslice=10,SampleFraction=30):
    first_id=0
    SpectraList=[]
    SpectraClusters=Spectral_ids_vector(DataSet=DataSet,IDVec=IDVec,RTslice=RTslice)
    for Spec_Id in SpectraClusters[1:]:
        last_id=Spec_Id
        RawSpectra=JoiningSpectra(DataSet=DataSet,IDVec=IDVec[first_id:last_id])
        SampleSpectra=SamplingSpectra(RawSpectra=RawSpectra,SampleFraction=SampleFraction)
        SpectraList.append(SampleSpectra)
        first_id=last_id
    return SpectraList
