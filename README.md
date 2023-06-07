<p align="center">
  <img src="https://github.com/brainhack-school2023/st-onge_project/assets/57685132/f10c8f2a-a5e3-40e4-bcef-8d99f204dfec">
</p>

# Identifying Potential Biomarkers for Parkinson’s Disease Using Neurite Orientation Dispersion and Diffusion Imaging (NODDI)

## ABOUT ME 

<a href="https://github.com/samuellestonge">
   <img src="https://avatars.githubusercontent.com/u/57685132?v=4" width="100px;" alt=""/>
   <br /><sub><b>Samuelle St-Onge </b></sub>
</a>

Hi everyone! My name is Samuelle St-Onge and I am a first year PhD student in biomedical engineering at Polytechnique Montréal, Canada. Prior to my PhD, I also did a master's in healthcare technology engineering at ÉTS in Montréal, as well as a Bachelor's degree in Mechanical engineering at Université de Moncton, New Brunswick, Canada. During my PhD, most of my work will be focused on spinal cord imaging for pediatric populations. 

## PROJECT DEFINITION

### Parkinson's disease
Parkinson’s disease is a neurogenerative disease for which we currently do not have any cure. Although there are treatment options available, early diagnosis is key to be able to start the treatment early and slow down the progression of the disease. However, since there there is still a lot of things we don't quite understand about Parkinson's disease, it is oftentimes difficult to diagnose at early stages. During this project, I will be exploring the use of NODDI (a diffusion MRI technique) applied to spinal cord images in the case of Parkinson's disease. More specifically, I will be applying NODDI to spinal cord images acquired from Parkison's disease patients at various stages of the disease to identify potential biomarkers for Parkinson's disease, with the ultimate goal of  helping clinicians diagnose the disease at an earlier stage, thus allowing early treatment to slow the progression of the disease. 

### Diffusion MRI and Neurite Orientation Dispersion and Diffusion Imaging (NODDI)
In recent work, diffusion MRI has shown a potential interest for finding biomarkers in the context of neurodegenerative diseases such as Parkinson, using Neurite Orientation Dispersion and Diffusion Imaging, commonly known as NODDI.  

#### What is NODDI? 
NODDI is a diffusion MRI technique which aims to extract metrics based on the morphology of neurites, which are composed of dendrites and axons. 

The most common metrics that can be extracted from NODDI (Mitchell et al., 2019) are : 

1. Orientation Dispersion Index (ODI) : Measures the variability in neurite orientation
2. Neurite Density Index (NDI) : Measures the density of neurites
3. Isotropic Volume Fraction (Viso) : Measures the fractional volume of extracellular fluid 

![image](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/817b3ce2-6291-44d0-ac00-b4f3d18e0756)

### Project summary 
My project aims to use an existing open-source NODDI toolbox and adapt it to a spinal cord diffusion MRI dataset containing both healthy subjects and subjects diagnosed with Parkinson's disease. Then, using the python data analysis tools and skills I have learned during BrainHack School, I will analyze the extracted metrics from the NODDI model fitting to explore potential biomarkers for Parkinson's disease.

#### Why NODDI for Parkinson's disease?
- Literature has shown an interest in diffusion MRI to identify potential Parkinson's disease biomarkers in brain images (Zhang et al., 2012)
- Links have been found between neurite morphology and other neurodegenerative diseases, such as multiple sclerosis (Zhang et al., 2012)

#### Why spinal cord images for Parkinson's disease biomarkers? 
- Spinal cord lesions have been recorded in Parkinson's disease patients (Tredici et al., 2012)
- To our knowledge, NODDI in the spinal cord for Parkinson's disease patients has not yet been studied

## OBJECTIVES

### Main objectives : 
The main objectives of this project were :

#### 1. Perform NODDI fitting

More specifically, the project aims to perform NODDI fitting on a diffusion MRI dataset with Parkinson's disease patients at various stages of the disease, as well as control subjects. The goal was to use a pre-existing NODDI toolbox (for example, a Matlab Toolbox), and to write a script to be able to perform multi-subject fitting using said toolbox. Since NODDI fitting is computationally expensive, I wanted to implement some sort of parallel computing to be able to speed up the process for all my subjects. 

#### 2. Extract and analyze NODDI metrics

Following NODDI fitting, the second main objective was to extract the NODDI metrics (ODI, NDI, Viso) to be able to do some data analysis using Python. 

<p align="center">
  <img src="https://github.com/brainhack-school2023/st-onge_project/assets/57685132/f727afd4-ffea-4ed1-b612-e2a47e3fae12">
</p>

### Long-term objective :

As a long-term goal, this project aims to identify potential biomarkers for Parkinson's disease using the extracted NODDI metrics.

### Personal objectives : 


## DATA

For this project, I have used a spinal cord dataset from some of our collaborators at McGill University. This dataset contains a total of 113 subjects, from which 87 have been diagnosed with Parkinson's disease at various stages of the disease ("low", "medium" and "advanced" stages) and the remaining 26 are healthy control subjects. 

The dataset contains other common MRI modalities, such as T1-weigthed and T2-weighted images. However, for the scope of BrainHack School, I have decided to focus only on the diffusion images and use NODDI.

#### Why this dataset?
I have chosen this specific dataset, since it comes from our collaborators at McGill and is part of a larger study, where we will be extracting and analyzing metrics from other MRI modalities to see if we can identify potential biomarkers for Parkinson's disease in the spinal cord. Also, to my knowledge, there are no similar public dataset available. 

## TOOLS AND METHODS
---


![image](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/0583b4c0-5d8c-40b5-9adf-4d2d486674bb)

### For NODDI fitting :
Matlab : 
- [NODDI Matlab Toolbox](http://mig.cs.ucl.ac.uk/index.php?n=Tutorial.NODDImatlab) (UCL Microstructure Imaging Group, 2021)
- [Matlab Parallel Computing Toolbox](https://www.mathworks.com/products/parallel-computing.html)
- [Matlab Optimization Toolbox](https://www.mathworks.com/products/optimization.html)

### For registration and NODDI metric extraction : 
- The [Spinal Cord Toolbox](https://spinalcordtoolbox.com/) (De Leener et al., 2017)

### For data analysis : 
Python :
- [`matplotlib`](https://matplotlib.org/)
- [`nibabel`](https://nipy.org/nibabel/)
- [`seaborn`](https://seaborn.pydata.org/)
- [`nilearn`](https://nilearn.github.io/stable/index.html)

### For version control : 
- Git and Github


## RESULTS


### 
![image](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/0b405e5a-7c3e-4be9-910f-094f86cf158f)




![image](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/0e7c4d10-4bf0-4861-8fed-dd1711cfdb34)




## DELIVERABLES


   ![image](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/ed1381bc-9cbf-4733-8fbb-7a4e13cced9b) [Matlab script to perform multi-subject NODDI fitting](https://github.com/brainhack-school2023/st-onge_project/blob/main/scripts/NODDI_multi-subject_fitting.m) using the [NODDI Matlab Toolbox](http://mig.cs.ucl.ac.uk/index.php?n=Tutorial.NODDImatlab) (UCL Microstructure Imaging Group, 2021) 

   ![image](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/90f42e61-d337-4421-8e0a-9df9a31409a7) [Python script to compute average NODDI metrics](https://github.com/brainhack-school2023/st-onge_project/blob/main/scripts/average_image_metrics.py) and display average images for each subject category (control subjects, low PD, medium PD and advanced PD)

   ![image](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/fa1ff39b-cef1-4d3b-a699-55679dc7ef47) [Python script to perform data analysis](https://github.com/brainhack-school2023/st-onge_project/blob/main/scripts/data_analysis_NODDI_metrics.py), i.e. regression plots to display and compare metrics (such as ODI, NDI and Viso) with Parkinson's disease progression. 



## LIMITATIONS AND FUTURE WORK

### For the NODDI fitting : 


### For the NODDI metric analysis : 


## CONCLUSION
As a new PhD student, BrainHack school was a great opportunity for me to learn about the basics of neuroscience imaging and data analysis. Although there are still some improvements to be made regarding my project, I look forward to apply the tools and skills I have learned during BrainHack School to work on improving what I have implemented so far. 

<p align="center">
  <img src="https://github.com/brainhack-school2023/st-onge_project/assets/57685132/f3f6012a-75e9-4f59-9361-058dc0e1e7a8">
</p>

## REFERENCES

De Leener B, Levy S, Dupont SM, Fonov VS, Stikov N, Louis Collins D, Callot V, Cohen-Adad J. 2017. SCT: Spinal Cord Toolbox, an open-source software for processing spinal cord MRI data. Neuroimage. <https://spinalcordtoolbox.com/user_section/citing_sct.html>

Del Tredici, Kelly et Heiko Braak. 2012. « Spinal cord lesions in sporadic Parkinson’s disease ». Acta Neuropathologica, vol. 124, no 5, p. 643‑664. <https://doi.org/10.1007/s00401-012-1028-y>.

Grussu, Francesco, Torben Schneider, Hui Zhang, Daniel C. Alexander et Claudia A. M. Wheeler–Kingshott. 2015. « Neurite orientation dispersion and density imaging of the healthy cervical spinal cord in vivo ». NeuroImage, vol. 111, p. 590‑601. <https://doi.org/10.1016/j.neuroimage.2015.01.045>.

Mitchell, Trina, Derek B. Archer, Winston T. Chu, Stephen A. Coombes, Song Lai, Bradley J. Wilkes, Nikolaus R. McFarland, Michael S. Okun, Mieniecia L. Black, Ellen Herschel, Tanya Simuni, Cynthia Comella, Tao Xie, Hong Li, Todd B. Parrish, Ajay S. Kurani, Daniel M. Corcos et David E. Vaillancourt. 2019. « Neurite orientation dispersion and density imaging (NODDI) and free‐water imaging in Parkinsonism ». Human Brain Mapping, vol. 40, no 17, p. 5094‑5107. <https://doi.org/10.1002/hbm.24760>.

UCL Microstructure Imaging Group. 2021. NODDI Matlab Toolbox. <http://mig.cs.ucl.ac.uk/index.php?n=Tutorial.NODDImatlab>.

Wang, Nian, Jieying Zhang, Gary Cofer, Yi Qi, Robert J. Anderson, Leonard E. White et G. Allan Johnson. 2019. « Neurite orientation dispersion and density imaging of mouse brain microstructure ». Brain Structure and Function, vol. 224, no 5, p. 1797‑1813. <https://doi.org/10.1007/s00429-019-01877-x>.

Zhang, Hui, Torben Schneider, Claudia A. Wheeler-Kingshott et Daniel C. Alexander. 2012. « NODDI: Practical in vivo neurite orientation dispersion and density imaging of the human brain ». NeuroImage, vol. 61, no 4, p. 1000‑1016. <https://doi.org/10.1016/j.neuroimage.2012.03.072>.
