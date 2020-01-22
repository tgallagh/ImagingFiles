# make plots of zeiss LSM files containing spectral 32-channel images

# libraries
import os
import tifffile as tiff
import numpy as np
import matplotlib.pyplot as plt   

wavelen=np.linspace(410,695,32)  # make list of wavelengths for channels 1-32
os.chdir("//LFD-Server/Files/Data/lfdguest1/Gallagher, Tara/PseudomonasSpectral/Pyocyanin_MOPS_pH_01-19-2020/Tara_Spectral_01-19-2020")
image_stack=tiff.imread(os.listdir()[0]) # read in first file in directory
image_stack.shape # shape of file
spec = np.sum(image_stack[0,0,:,:,:]) 
spec1=np.sum(spec,1)  # contains sum intensity for each channel (1-32)
plt.plot(wavelen,spec1)  



