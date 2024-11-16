from JoiningSpectra import *
from SamplingSpectra import *
from Spectral_ids_vector import *
def SpectralList(DataSet,MS1IDVec,RTslice=10):
    first_id=0
    SpectraList=[]
    SpectraClusters=Spectral_ids_vector(DataSet,MS1IDVec,RTslice=10)
    for Spec_Id in SpectraClusters[1:]:
        last_id=Spec_Id
        RawSpectra=JoiningSpectra(DataSet,MS1IDVec[first_id:last_id])
        SampleSpectra=SamplingSpectra(RawSpectra,SampleFraction=30)
        SpectraList.append(SampleSpectra)
        first_id=last_id
    return SpectraList
