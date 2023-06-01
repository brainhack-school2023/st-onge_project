import os
import nibabel as nb
import numpy as np
from matplotlib import transforms
import matplotlib.pyplot as plt
import scipy 
from nilearn import plotting

### CREATE AVERAGE IMAGE FROM EXTRACTED NODDI METRICS 

# Path to dataset directory : 
dataset_directory = 'D:/1_Doctorat/Projets/BMPD/derivatives/noddi_processing'

# load an image
test_load = nb.load('D:/1_Doctorat/Projets/BMPD/derivatives/noddi_processing/sub-P001/sub-P001_odi_reg.nii')
print(test_load.shape)

# show an image
x_min, x_max = 50, 90  # Adjust the values according to your desired range
y_min, y_max = 50, 90  # Adjust the values according to your desired range
plt.imshow(test_load.get_fdata()[:, :, 880], cmap='gray')
cb = plt.colorbar(orientation='horizontal', shrink=.75) 
cb.set_label('iteration count') 
plt.show()

# Average image for control subjects : 

img = nb.load("D:/1_Doctorat/Projets/BMPD/derivatives/noddi_processing/sub-P001/sub-P001_odi_reg.nii")
sum_img = img.get_fdata()

ctrl_directory = "D:/1_Doctorat/Projets/BMPD/derivatives/noddi_processing/ctrl"

number_of_images = 0
for subject in os.listdir(ctrl_directory):
    number_of_images +=1
    if subject.startswith('sub-P') :
        path_to_img = "D:/1_Doctorat/Projets/BMPD/derivatives/noddi_processing/ctrl/" + subject + "/" + subject + "_odi_reg.nii"
        img = nb.load(path_to_img)
        img_data = img.get_fdata()
        if subject == 1 : 
            sum_img = img_data
        else:
            sum_img = sum_img + img_data

print(sum_img)
print(number_of_images)
img_avg = sum_img/number_of_images

plt.imshow(img_avg[:, :, 880], cmap='gray')
plt.title('average image for control subjects')
cb = plt.colorbar(orientation='horizontal', shrink=.75) 
cb.set_label('iteration count') 
plt.show()

# Average image for low stage PD subjects : 

low_PD_directory = "D:/1_Doctorat/Projets/BMPD/derivatives/noddi_processing/low"

number_of_images = 0
for subject in os.listdir(low_PD_directory):
    number_of_images +=1
    if subject.startswith('sub-P') :
        path_to_img = "D:/1_Doctorat/Projets/BMPD/derivatives/noddi_processing/low/" + subject + "/" + subject + "_odi_reg.nii"
        img = nb.load(path_to_img)
        img_data = img.get_fdata()
        if subject == 1 : 
            sum_img = img_data
        else:
            sum_img = sum_img + img_data

print(sum_img)
print(number_of_images)
img_avg = sum_img/number_of_images

plt.imshow(img_avg[:, :, 880], cmap='gray')
plt.title('average image for low stage PD subjects')
cb = plt.colorbar(orientation='horizontal', shrink=.75) 
cb.set_label('iteration count') 
plt.show()

# Average image for medium PD subjects : 

med_PD_directory = "D:/1_Doctorat/Projets/BMPD/derivatives/noddi_processing/med"

number_of_images = 0
for subject in os.listdir(med_PD_directory):
    number_of_images +=1
    if subject.startswith('sub-P') :
        path_to_img = "D:/1_Doctorat/Projets/BMPD/derivatives/noddi_processing/med/" + subject + "/" + subject + "_odi_reg.nii"
        img = nb.load(path_to_img)
        img_data = img.get_fdata()
        if subject == 1 : 
            sum_img = img_data
        else:
            sum_img = sum_img + img_data

print(sum_img)
print(number_of_images)
img_avg = sum_img/number_of_images

plt.imshow(img_avg[:, :, 880], cmap='gray')
plt.title('average image for medium stage PD subjects')
cb = plt.colorbar(orientation='horizontal', shrink=.75) 
cb.set_label('iteration count') 
plt.show()

# Average image for advanced PD subjects : 

img = nb.load("D:/1_Doctorat/Projets/BMPD/derivatives/noddi_processing/sub-P001/sub-P001_odi_reg.nii")
sum_img = img.get_fdata()

adv_PD_directory = "D:/1_Doctorat/Projets/BMPD/derivatives/noddi_processing/adv"

number_of_images = 0
for subject in os.listdir(adv_PD_directory):
    number_of_images +=1
    if subject.startswith('sub-P') :
        path_to_img = "D:/1_Doctorat/Projets/BMPD/derivatives/noddi_processing/adv/" + subject + "/" + subject + "_odi_reg.nii"
        img = nb.load(path_to_img)
        img_data = img.get_fdata()
        if subject == 1 : 
            sum_img = img_data
        else:
            sum_img = sum_img + img_data

print(sum_img)
print(number_of_images)
img_avg = sum_img/number_of_images

plt.imshow(img_avg[:, :, 880], cmap='gray')
plt.title('average image for advanced PD subjects')
cb = plt.colorbar(orientation='horizontal', shrink=.75) 
cb.set_label('iteration count') 
plt.show()



