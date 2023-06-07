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

## 1.  PROJECT DEFINITION

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
My project aims to use an existing open-source NODDI toolbox to perform NODDI fitting of a spinal cord diffusion MRI dataset containing both healthy subjects and subjects diagnosed with Parkinson's disease. Then, using the data analysis tools and skills I have learned during BrainHack School, I have written a Python script to analyze the extracted metrics from the NODDI model fitting, which will then help me compare the metrics with the progression of the disease and identify potential biomarkers for Parkinson's disease.

#### Why NODDI for Parkinson's disease?
- Literature has shown an interest in diffusion MRI to identify potential Parkinson's disease biomarkers in brain images (Zhang et al., 2012)
- Links have been found between neurite morphology and other neurodegenerative diseases, such as multiple sclerosis (Zhang et al., 2012)

#### Why spinal cord images for Parkinson's disease biomarkers? 
- Spinal cord lesions have been recorded in Parkinson's disease patients (Tredici et al., 2012)
- To our knowledge, NODDI in the spinal cord for Parkinson's disease patients has not yet been studied

## 2.  OBJECTIVES

### Main objectives : 
The main objectives of this project were :

#### 1. Perform NODDI fitting

More specifically, the project aims to perform NODDI fitting on a diffusion MRI dataset with Parkinson's disease patients at various stages of the disease, as well as control subjects. The goal was to use a pre-existing NODDI toolbox and to write a script to be able to perform multi-subject fitting using said toolbox. Since NODDI fitting is computationally expensive, I wanted to implement some sort of parallel computing to be able to speed up the process for all my subjects. 

#### 2. Extract and analyze NODDI metrics

Following NODDI fitting, the second main objective was to extract the NODDI metrics (ODI, NDI, Viso) to be able to do some data analysis using Python. 

<p align="center">
  <img src="https://github.com/brainhack-school2023/st-onge_project/assets/57685132/f727afd4-ffea-4ed1-b612-e2a47e3fae12">
</p>

### Long-term objective :

As a long-term goal, this project aims to identify potential biomarkers for Parkinson's disease using the extracted NODDI metrics.

### Personal objectives : 

During this project, my personal objectives were to apply the neuroimaging data analysis skills I have learned during BrainHack School and to learn the basics of diffusion MRI and NODDI fitting. I also wanted to get familiar using images in NITFI format and datasets in BIDS, and to apply new tools and concepts that will be essential for my PhD.  

## 3.  DATA

For this project, I have used a spinal cord dataset from our collaborators at McGill University. This dataset contains a total of 113 subjects, from which 87 have been diagnosed with Parkinson's disease at various stages of the disease ("low", "medium" and "advanced" stages) and the remaining 26 are healthy control subjects. 

The dataset contains other common MRI modalities, such as T1-weigthed and T2-weighted images. However, for the scope of BrainHack School, I have decided to focus only on diffusion images and NODDI.

#### Why this dataset?
I have chosen this specific dataset, since it is part of a larger study with our collaborators at McGill, where we will be extracting and analyzing metrics from other MRI modalities to see if we can identify potential biomarkers for Parkinson's disease in the spinal cord. Also, to my knowledge, there are no similar public dataset available. 

## 4.  TOOLS AND METHODS

### Tools

#### For NODDI fitting :
Matlab : 
- [NODDI Matlab Toolbox](http://mig.cs.ucl.ac.uk/index.php?n=Tutorial.NODDImatlab) (UCL Microstructure Imaging Group, 2021)
- [Matlab Parallel Computing Toolbox](https://www.mathworks.com/products/parallel-computing.html)
- [Matlab Optimization Toolbox](https://www.mathworks.com/products/optimization.html)

#### For registration and NODDI metric extraction : 
- The [Spinal Cord Toolbox](https://spinalcordtoolbox.com/) (De Leener et al., 2017)

#### For data analysis : 
Python :
- [`matplotlib`](https://matplotlib.org/)
- [`nibabel`](https://nipy.org/nibabel/)
- [`seaborn`](https://seaborn.pydata.org/)
- [`nilearn`](https://nilearn.github.io/stable/index.html)

#### For version control : 
- Git and Github

### Methods 

The following diagram summarizes the key stages of the methods used for my project : 

![image](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/0583b4c0-5d8c-40b5-9adf-4d2d486674bb)

#### NODDI fitting :
Starting with the diffusion MRI images from the dataset, I first performed NODDI fitting using the [NODDI Matlab Toolbox](http://mig.cs.ucl.ac.uk/index.php?n=Tutorial.NODDImatlab) (UCL Microstructure Imaging Group, 2021) from UCL Microstructure Imaging Group. Using this toolbox, I wrote a [Matlab script](https://github.com/brainhack-school2023/st-onge_project/blob/main/scripts/NODDI_multi-subject_fitting.m) to be able to perform multi-subject NODDI fitting with a BIDS-compliant dataset. The NODDI Matlab Toolbox also gives the user the option of using the Matlab Parallel Computing Toolbox, which speeds up the fitting process significantly. 

For the inputs, the NODDI Matlab Toolbox requires diffusion MRI files (`sub-PXXX_dwi.nii`, `sub-PXXX.bvec`, `sub-PXXX.bval`). It is also possible to specify a mask, in order to restrict the fitting to a certain region of the image (for example, only the spinal cord). In this specific project, I used segmentation files that had already been performed on 42 subjects prior to BrainHack School, by a previous graduate student. Initially, my goal was to start by performing NODDI fitting and metric analysis for these 42 subjects with the segmentation files, and then go back and segment the remaining subjects and re-run the NODDI fitting and metric analysis pipeline for the whole dataset. Howerver, I did not have enough time to go back and do the segmentation during BrainHack School. For this reason, I decided to focus only on 42 of the 113 subjects in the dataset for my Brainhack School project.

#### Registration to PAM50 template
Following NODDI fitting, I decided to perform registration on the output metrics to be able to compute an average metric for each subject category : control, low disease, medium disease and advanced disease. 
To perform the registration, I used the [`Spinal Cord Toolbox (SCT)`](https://spinalcordtoolbox.com/index.html) and followed the recommended steps in the documentation. 

The following diagram shows a summary of the `Spinal Cord Toolbox` pipeline for registration to the [`PAM50 template`](https://spinalcordtoolbox.com/overview/concepts/pam50.html?highlight=pam50) with DWI images : 

![image](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/fff88b6a-7c3e-430c-b4b1-76cba46fbdd2)

*Detailed explanations for each of these steps can be found in the [Spinal Cord Toolbox DWI tutorial](https://spinalcordtoolbox.com/user_section/tutorials/diffusion-weighted-mri/template-registration-for-dmri.html). 

#### Metric extraction using the Spinal Cord Toolbox
Following NODDI fitting, to extract the values of the ODI, NDI and Viso metrics (which were all in NIFTI format following the NODDI fitting process with Matlab), I used the command [`sct_extract_metric`](https://spinalcordtoolbox.com/user_section/tutorials/diffusion-weighted-mri/extracting-dti-from-specific-regions.html) from the `Spinal Cord Toolbox`. The following diagram shows a summary of the command amd the arguments that were used for my project : 

![image](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/3a0798dc-31d0-4344-b172-0e62c97bec6d)

The command `sct_extract_metric` outputs a .csv file for the metric from the file specified in the `-i` argument. For this specific project, I chose the labels 50, 51 and 52 with the `-l` argument, which correspond to the spinal cord, white matter and gray matter. I also chose to extract metrics from C2 to C5, using the `-vert` argument. 

## 5.  RESULTS

### Computing average metrics

Following the registration to the PAM50 template, I have written a [Python script to compute average metrics](https://github.com/brainhack-school2023/st-onge_project/blob/main/scripts/average_image_metrics.py) and display them as images. The following image shows an example of the average orientation dispersion index (ODI) for each subject category (control, low PD, medium PD and advanced PD).

![image](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/87377dc2-df84-4e68-99f1-dc09762d48b6)

By looking at the image above, we can notice an offset between the images used to compute the average. This is most likely due to a problem with the registration step. Following BrainHack School, I would like to try the registration with different parameters to see if I can fix this offset. 

### Regression plots

I have also written a [Python script for data analysis](https://github.com/brainhack-school2023/st-onge_project/blob/main/scripts/data_analysis_NODDI_metrics.py), which takes the metrics from the .csv files obtained with the `sct_extract_metric` command to do regression plots. The image below shows an example of the regression plots that can be achieved with this script.

![image](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/c206c463-c9a7-4560-8993-d9b77110df48)

The plots are divided by vertebrae level (in this example, from C2 to C5) as well as by label (white matter, gray matter and spinal cord). In each plot, we can observe the metric with the progression of the disease (from control subjects to advanced Parkinson's disease subjects). 

In this specific project, since I have used only 42 subjects, there is not enough data to draw any conclusions, nor identify potential biomarkers for Parkinson's disease. Also, future versions of the Python script should include a regression model with p-values, to be able to perform a more rigorous statistical analysis. 

In future work, after having improved the python script to include p-values, I would like to perform the analysis for the entire dataset (113 subjects). By repeating the analysis with the entire dataset, I would suspect seeing an increase in ODI in the white matter and a decrease in ODI in the gray matter, since these have been linked to neurodegeneration according to literature (Zhang et al., 2012). 

## 6.  DELIVERABLES


   ![image](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/ed1381bc-9cbf-4733-8fbb-7a4e13cced9b) [Matlab script to perform multi-subject NODDI fitting](https://github.com/brainhack-school2023/st-onge_project/blob/main/scripts/NODDI_multi-subject_fitting.m) using the [NODDI Matlab Toolbox](http://mig.cs.ucl.ac.uk/index.php?n=Tutorial.NODDImatlab) (UCL Microstructure Imaging Group, 2021) 

   ![image](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/90f42e61-d337-4421-8e0a-9df9a31409a7) [Python script to compute average NODDI metrics](https://github.com/brainhack-school2023/st-onge_project/blob/main/scripts/average_image_metrics.py) and display average images for each subject category (control subjects, low PD, medium PD and advanced PD)

   ![image](https://github.com/brainhack-school2023/st-onge_project/assets/57685132/fa1ff39b-cef1-4d3b-a699-55679dc7ef47) [Python script to perform data analysis](https://github.com/brainhack-school2023/st-onge_project/blob/main/scripts/data_analysis_NODDI_metrics.py), i.e. regression plots to display and compare metrics (such as ODI, NDI and Viso) with Parkinson's disease progression. 

## 7.  LIMITATIONS AND FUTURE WORK

### For the NODDI fitting : 
Following BrainHack School, I would like to pre-process the entire dataset, by also adding [motion correction using the Spinal Cord Toolbox](https://spinalcordtoolbox.com/user_section/tutorials/diffusion-weighted-mri/motion-correction-for-dmri.html). 

I would also like to use a larger mask to perform the NODDI fitting. As I mentionned in the "Methods" section above, in this project I used segmentation files as a mask for the NODDI fitting. However, it would be interesting to try a mask that is larger than the segmentation of the spinal cord to see if it can help reduce potential partial volume effect. 

Furthermore, I would like to try performing the registration to the PAM50 template prior to the NODDI fitting, to be able to extract the metric values and compute average images dirrectly from the output metrics. 

### For the NODDI metric analysis : 

Regarding the metric analysis, I would like to try the registration to the PAM50 template with different parameters to fix the offset I have with the current results. 

For the regression plots, it would be important to consider the age as a control variable, to avoid overestimating the effect of Parkinson's disease progression when performing the regression analysis. 

Finally, I would like to incorporate a regression model with p-values to perform more rirogous statistics on the different NODDI metrics. 

## 8.  CONCLUSION
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
