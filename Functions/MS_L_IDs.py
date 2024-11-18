import numpy as np
def MS_L_IDs(DataSet,Level=1):
    IDvec=[]
    spectrum_id=0
    for SpectralSignals in DataSet:
        MSLevel=SpectralSignals.getMSLevel()
        if MSLevel==Level:
            RT=SpectralSignals.getRT()
            IDvec.append([spectrum_id,RT])
        spectrum_id+=1
    IDvec=np.array(IDvec)
    return IDvec
