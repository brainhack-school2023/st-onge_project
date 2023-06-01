% Multi-subject NODDI fitting (using the NODDI Toolbox from UCL Microstructure Imgaging Group)

% To be able to run this script, you will need to install the NODDI Toolbox from UCL Microstructure Imaging Group, which can be downloaded here : https://www.nitrc.org/projects/noddi_toolbox/ .
% You will also need the optimization toolbox from Matlab as well as the NIFTI Matlab library, which can be found here : https://github.com/NIFTI-Imaging/nifti_matlab

% STEP 1 : add the NODDI toolbox directory to your matlab path : 

addpath(genpath('PATH/TO/NODDI/TOOLBOX'));

% STEP 2 : Specify the directory of your dataset (*Note : for this script to work, you will need a BIDS compliant dataset). 

rawdatadir = 'PATH/TO/YOUR/BIDS/DATASET/';

% MULTI-SUBJECT NODDI FITTING : 

cd(rawdatadir)
subj_files = dir(fullfile(rawdatadir, 'sub-P*'));

subjects = {subj_files([subj_files.isdir]).name}

N = numel(subjects)

for i = 1:N
    
    subj = char(subjects(i))
    % subject directory for raw files
    datadir = strcat('PATH/TO/YOUR/BIDS/DATASET/', subj, '/dwi')
    cd(datadir)

    %% LOAD DATA

    diffusion_data = strcat(subj, '_dwi.nii');
    mask = strcat(subj, '_label-mask_dwi.nii');
    bvals = strcat(subj, '_dwi.bval');
    bvecs = strcat(subj, '_dwi.bvec');

    %% CONVERT DATA TO REQUIRED FORMAT FOR NODDI FITTING

    roi = strcat('NODDI_roi_', subj, '.mat');
    CreateROI(diffusion_data, mask, roi);

    %% PROTOCOL

    protocol = FSL2Protocol(bvals, bvecs);

    %% CREATE MODEL (WatsonSHStickTortIsoV_B0)

    noddi = MakeModel('WatsonSHStickTortIsoV_B0');

    %% FITTING
    fitted_params = strcat('FittedParams_', subj, '.mat');
    batch_fitting(roi, protocol, noddi, fitted_params);

    %% SAVE RESULTS AS NIFTI

    SaveParamsAsNIfTI(fitted_params, roi, mask, subj);

end
