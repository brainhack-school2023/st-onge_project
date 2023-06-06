![image](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/f10c8f2a-a5e3-40e4-bcef-8d99f204dfec)


# Identifying Potential Biomarkers for Parkinson’s Disease Using Neurite Orientation Dispersion and Diffusion Imaging (NODDI) 

## ABOUT ME 
---
<a href="https://github.com/samuellestonge">
   <img src="https://avatars.githubusercontent.com/u/57685132?v=4" width="100px;" alt=""/>
   <br /><sub><b>Samuelle St-Onge </b></sub>
</a>

Hi everyone! My name is Samuelle St-Onge and I am a first year PhD student at Polytechnique Montréal, Canada. Prior to my PhD, I also did a master's in healthcare technology engineering at ÉTS in Montréal, as well as a Bachelor's degree in Mechanical engineering at Université de Moncton, New Brunswick, Canada. During my PhD, most of my work will be focused on spinal cord imaging for pediatric populations. 

## PROJECT DEFINITION
---
### Parkinson's disease
Parkinson’s disease is a neurogenerative disease for which we currently do not have any cure. Although there are treatment options available, early diagnosis is key to be able to start the treatment early and slow down the progression of the disease. However, since there there is still a lot of things we don't quite understand about Parkinson's disease, it is oftentimes difficult to diagnose at early stages. During this project, I will finding new biomarkers for Parkinson's, which could help diagnose the disease at an earlier stage, therefore being able to start treatment early and slow disease progression. 

### Diffusion MRI and Neurite Orientation Dispersion and Diffusion Imaging (NODDI)
In recent work, diffusion MRI has shown a potential interest for finding biomarkers in the context of neurodegenerative diseases such as Parkinson, using Neurite Orientation Dispersion and Diffusion Imaging, commonly known as NODDI.  

#### What is NODDI? 
NODDI is a diffusion MRI technique which aims to extract metrics based on the morphology of neurites, which are composed of dendrites and axons. 

The most common metrics that can be extracted from NODDI are : 

1. Orientation Dispersion Index (ODI)
2. Neurite Density Index (NDI) 
3. Isotropic Volume Fraction (Viso) 

### Project summary 
My project aims to use an existing open-source NODDI toolbox and adapt it to a spinal cord diffusion MRI dataset containing both healthy subjects and subjects diagnosed with Parkinson's disease. Then, using the python data analysis tools and skills I have learned during BrainHack School, I will analyze the extracted metrics from the NODDI model fitting to explore potential biomarkers for Parkinson's disease.

#### Why NODDI for Parkinson's disease?
- Literature has shown an interest in diffusion MRI to identify potential Parkinson's disease biomarkers in brain images (Zhang et al., 2012)
- et al. (2012) found links between neurite morphology and other neurodegenerative diseases, such as multiple sclerosis

#### Why spinal cord images for Parkinson's disease biomarkers? 
- Spinal cord lesions have been recorded in Parkinson's disease patients (Tredici et al., 2012)
- To our knowledge, NODDI in the spinal cord for Parkinson's disease patients has not yet been studied

## OBJECTIVES
---
### Main objectives : 
The main objectives of this project were :

#### 1. Perform NODDI fitting

More specifically, the project aims to perform NODDI fitting on a diffusion MRI dataset with Parkinson's disease patients at various stages of the disease, as well as control subjects. The goal was to use a pre-existing NODDI toolbox (for example, a Matlab Toolbox), and to write a script to be able to perform multi-subject fitting using said toolbox. Since NODDI fitting is computationally expensive, I wanted to implement some sort of parallel computing to be able to speed up the process for all my subjects. 

#### 2. Extract and analyze NODDI metrics

Following NODDI fitting, the second main objective was to extract the NODDI metrics (ODI, NDI, Viso) to be able to do some data analysis using Python. 

#### *** Identifying potential biomarkers for Parkinson's disease

As a long-term goal, this project aims to identify potential biomarkers for Parkinson's disease using the extracted NODDI metrics.


![image](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/f727afd4-ffea-4ed1-b612-e2a47e3fae12)


### My personal objectives for this project were: 



## DATA
---




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
---

![image](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/54f759f4-462b-4d9c-8c86-4f56b0f763e0)
![regression_plots](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/40ff403c-f77a-490f-a397-7b3532867daf)



## DELIVERABLES
---


## LIMITATIONS AND FUTURE WORK
---


## CONCLUSION
---


## REFERENCES
---

De Leener B, Levy S, Dupont SM, Fonov VS, Stikov N, Louis Collins D, Callot V, Cohen-Adad J. 2017. SCT: Spinal Cord Toolbox, an open-source software for processing spinal cord MRI data. Neuroimage. <https://spinalcordtoolbox.com/user_section/citing_sct.html>

UCL Microstructure Imaging Group. 2021. NODDI Matlab Toolbox. <http://mig.cs.ucl.ac.uk/index.php?n=Tutorial.NODDImatlab>.

