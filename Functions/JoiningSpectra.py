import numpy as np
def JoiningSpectra(DataSet,MS1IDVec):
    if len(MS1IDVec)>1:
        RawSpectra=JoiningSpectra(DataSet,MS1IDVec[1:])
        RawSignals=JoiningSpectra(DataSet,MS1IDVec[:1]) 
        RawSpectra=np.append(RawSpectra,RawSignals,axis=0)
        RawSpectra=RawSpectra[RawSpectra[:, 0].argsort(),:]
    else:
        Spec_Id=int(MS1IDVec[0])
        RawSpectra=np.array(DataSet[Spec_Id].get_peaks()).T
    return RawSpectra
