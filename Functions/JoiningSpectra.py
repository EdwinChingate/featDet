import numpy as np
def JoiningSpectra(DataSet,IDVec):
    if len(IDVec)>1:
        RawSpectra=JoiningSpectra(DataSet,IDVec[1:])
        RawSignals=JoiningSpectra(DataSet,IDVec[:1]) 
        RawSpectra=np.append(RawSpectra,RawSignals,axis=0)
        RawSpectra=RawSpectra[RawSpectra[:, 0].argsort(),:]
    else:
        Spec_Id=int(IDVec[0])
        RawSpectra=np.array(DataSet[Spec_Id].get_peaks()).T
    return RawSpectra
