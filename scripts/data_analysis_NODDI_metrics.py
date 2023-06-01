import os
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
import numpy as np
from sklearn.preprocessing import LabelEncoder

# STEP 1. Load data from csv file 

path_to_data = 'C:/Users/Samuelle/OneDrive - polymtl.ca/2. COURS\Brainhack School 2023/Project/participants_and_metrics.xlsx'
data = pd.read_excel(path_to_data)

# STEP 2 : Specify the metric you would like to output graphs for (ex: ODI, NDI, etc.)

NODDI_metrics = ['ODI', 'NDI', 'IVF']

# STEP 3 : Specify the labels you would like to output graphs for (ex: white matter, gray matter, etc.)

NODDI_labels = ['white matter', 'gray matter', 'spinal cord']

# STEP 4 : Specify vertebral levels

vert_levels = ['C5', 'C4', 'C3', 'C2']

WM_data = data[data['label'].str.contains('WM')]
GM_data = data[data['label'].str.contains('GM')]
SC_data = data[data['label'].str.contains('SC')]

# STEP 4 : Compute 

for metric in NODDI_metrics:

    if metric == 'ODI':

        for label in NODDI_labels :

            if label == 'white matter' :

                C5_data_WM = WM_data[WM_data['vert_level'].str.contains('C5')]
                PD_stage_C5_WM = C5_data_WM['PD_stage']
                PD_metric_C5_WM = C5_data_WM['ODI_size']

                C4_data_WM = WM_data[WM_data['vert_level'].str.contains('C4')]
                PD_stage_C4_WM = C4_data_WM['PD_stage']
                PD_metric_C4_WM = C4_data_WM['ODI_size']

                C3_data_WM = WM_data[WM_data['vert_level'].str.contains('C3')]
                PD_stage_C3_WM = C3_data_WM['PD_stage']
                PD_metric_C3_WM = C3_data_WM['ODI_size']

                C2_data_WM = WM_data[WM_data['vert_level'].str.contains('C2')]
                PD_stage_C2_WM = C2_data_WM['PD_stage']
                PD_metric_C2_WM = C2_data_WM['ODI_size']

                # Create dataframes

                data = {'PD Stage': PD_stage_C5_WM, 'PD Metric': PD_metric_C5_WM}
                df1 = pd.DataFrame(data)

                data = {'PD Stage': PD_stage_C4_WM, 'PD Metric': PD_metric_C4_WM}
                df2 = pd.DataFrame(data)
  
                data = {'PD Stage': PD_stage_C3_WM, 'PD Metric': PD_metric_C3_WM}
                df3 = pd.DataFrame(data)

                data = {'PD Stage': PD_stage_C2_WM, 'PD Metric': PD_metric_C2_WM}
                df4 = pd.DataFrame(data)

            if label == 'gray matter':

                C5_data_GM = GM_data[GM_data['vert_level'].str.contains('C5')]
                PD_stage_C5_GM = C5_data_GM['PD_stage']
                PD_metric_C5_GM = C5_data_GM['ODI_size']

                C4_data_GM = GM_data[GM_data['vert_level'].str.contains('C4')]
                PD_stage_C4_GM = C4_data_GM['PD_stage']
                PD_metric_C4_GM = C4_data_GM['ODI_size']

                C3_data_GM = GM_data[GM_data['vert_level'].str.contains('C3')]
                PD_stage_C3_GM = C3_data_GM['PD_stage']
                PD_metric_C3_GM = C3_data_GM['ODI_size']

                C2_data_GM = GM_data[GM_data['vert_level'].str.contains('C2')]
                PD_stage_C2_GM = C2_data_GM['PD_stage']
                PD_metric_C2_GM = C2_data_GM['ODI_size']

                # create dataframes

                data = {'PD Stage': PD_stage_C5_GM, 'PD Metric': PD_metric_C5_GM}
                df5 = pd.DataFrame(data)

                data = {'PD Stage': PD_stage_C4_GM, 'PD Metric': PD_metric_C4_GM}
                df6 = pd.DataFrame(data)
  
                data = {'PD Stage': PD_stage_C3_GM, 'PD Metric': PD_metric_C3_GM}
                df7 = pd.DataFrame(data)

                data = {'PD Stage': PD_stage_C2_GM, 'PD Metric': PD_metric_C2_GM}
                df8 = pd.DataFrame(data)

            if label == 'spinal cord':
                
                C5_data_SC = SC_data[SC_data['vert_level'].str.contains('C5')]
                PD_stage_C5_SC = C5_data_SC['PD_stage']
                PD_metric_C5_SC = C5_data_SC['ODI_size']

                C4_data_SC = SC_data[SC_data['vert_level'].str.contains('C4')]
                PD_stage_C4_SC = C4_data_SC['PD_stage']
                PD_metric_C4_SC = C4_data_SC['ODI_size']

                C3_data_SC = SC_data[SC_data['vert_level'].str.contains('C3')]
                PD_stage_C3_SC = C3_data_SC['PD_stage']
                PD_metric_C3_SC = C3_data_SC['ODI_size']

                C2_data_SC = SC_data[SC_data['vert_level'].str.contains('C2')]
                PD_stage_C2_SC = C2_data_SC['PD_stage']
                PD_metric_C2_SC = C2_data_SC['ODI_size']

                # create dataframes

                data = {'PD Stage': PD_stage_C5_SC, 'PD Metric': PD_metric_C5_SC}
                df9 = pd.DataFrame(data)

                data = {'PD Stage': PD_stage_C4_SC, 'PD Metric': PD_metric_C4_SC}
                df10 = pd.DataFrame(data)
  
                data = {'PD Stage': PD_stage_C3_SC, 'PD Metric': PD_metric_C3_SC}
                df11 = pd.DataFrame(data)

                data = {'PD Stage': PD_stage_C2_SC, 'PD Metric': PD_metric_C2_SC}
                df12 = pd.DataFrame(data)

# Convert PD stage to str
df1['PD Stage'] = df1['PD Stage'].astype(str)
df2['PD Stage'] = df2['PD Stage'].astype(str)
df3['PD Stage'] = df3['PD Stage'].astype(str)
df4['PD Stage'] = df4['PD Stage'].astype(str)
df5['PD Stage'] = df5['PD Stage'].astype(str)
df6['PD Stage'] = df6['PD Stage'].astype(str)
df7['PD Stage'] = df7['PD Stage'].astype(str)
df8['PD Stage'] = df8['PD Stage'].astype(str)
df9['PD Stage'] = df9['PD Stage'].astype(str)
df10['PD Stage'] = df10['PD Stage'].astype(str)
df11['PD Stage'] = df11['PD Stage'].astype(str)
df12['PD Stage'] = df12['PD Stage'].astype(str)


# Convert PD metric to float
df1['PD Metric'] = df1['PD Metric'].astype(float)
df2['PD Metric'] = df2['PD Metric'].astype(float)
df3['PD Metric'] = df3['PD Metric'].astype(float)
df4['PD Metric'] = df4['PD Metric'].astype(float)
df5['PD Metric'] = df5['PD Metric'].astype(float)
df6['PD Metric'] = df6['PD Metric'].astype(float)
df7['PD Metric'] = df7['PD Metric'].astype(float)
df8['PD Metric'] = df8['PD Metric'].astype(float)
df9['PD Metric'] = df9['PD Metric'].astype(float)
df10['PD Metric'] = df10['PD Metric'].astype(float)
df11['PD Metric'] = df11['PD Metric'].astype(float)
df12['PD Metric'] = df12['PD Metric'].astype(float)

# Apply label encoding to Disease Stage
label_encoder = LabelEncoder()
df1['PD Stage'] = label_encoder.fit_transform(df1['PD Stage'])
df2['PD Stage'] = label_encoder.fit_transform(df2['PD Stage'])
df3['PD Stage'] = label_encoder.fit_transform(df3['PD Stage'])
df4['PD Stage'] = label_encoder.fit_transform(df4['PD Stage'])
df5['PD Stage'] = label_encoder.fit_transform(df5['PD Stage'])
df6['PD Stage'] = label_encoder.fit_transform(df6['PD Stage'])
df7['PD Stage'] = label_encoder.fit_transform(df7['PD Stage'])
df8['PD Stage'] = label_encoder.fit_transform(df8['PD Stage'])
df9['PD Stage'] = label_encoder.fit_transform(df9['PD Stage'])
df10['PD Stage'] = label_encoder.fit_transform(df10['PD Stage'])
df11['PD Stage'] = label_encoder.fit_transform(df11['PD Stage'])
df12['PD Stage'] = label_encoder.fit_transform(df12['PD Stage'])


fig, axes = plt.subplots(4, 3, figsize=(12, 16))

#axes = axes.flatten()

# # Plot the regression plot
# # WM column
# sns.regplot(x='PD Stage', y='PD Metric', data=df1, ax=axes[0,0])
# sns.regplot(x='PD Stage', y='PD Metric', data=df2, ax=axes[1, 0])
# sns.regplot(x='PD Stage', y='PD Metric', data=df3, ax=axes[2, 0])
# sns.regplot(x='PD Stage', y='PD Metric', data=df4, ax=axes[3, 0])
# # GM column
# sns.regplot(x='PD Stage', y='PD Metric', data=df5, ax=axes[0, 1])
# sns.regplot(x='PD Stage', y='PD Metric', data=df6, ax=axes[1, 1])
# sns.regplot(x='PD Stage', y='PD Metric', data=df7, ax=axes[2, 1])
# sns.regplot(x='PD Stage', y='PD Metric', data=df8, ax=axes[3, 1])
# # SC column 
# sns.regplot(x='PD Stage', y='PD Metric', data=df9, ax=axes[0, 2])
# sns.regplot(x='PD Stage', y='PD Metric', data=df10, ax=axes[1, 2])
# sns.regplot(x='PD Stage', y='PD Metric', data=df11, ax=axes[2, 2])
# sns.regplot(x='PD Stage', y='PD Metric', data=df12, ax=axes[3, 2])

# WM column
# sns.violinplot(x='PD Stage', y='PD Metric', data=df1, ax=axes[0,0])
# sns.violinplot(x='PD Stage', y='PD Metric', data=df2, ax=axes[1, 0])
# sns.violinplot(x='PD Stage', y='PD Metric', data=df3, ax=axes[2, 0])
# sns.violinplot(x='PD Stage', y='PD Metric', data=df4, ax=axes[3, 0])
# # GM column
# sns.violinplot(x='PD Stage', y='PD Metric', data=df5, ax=axes[0, 1])
# sns.violinplot(x='PD Stage', y='PD Metric', data=df6, ax=axes[1, 1])
# sns.violinplot(x='PD Stage', y='PD Metric', data=df7, ax=axes[2, 1])
# sns.violinplot(x='PD Stage', y='PD Metric', data=df8, ax=axes[3, 1])
# # SC column 
# sns.violinplot(x='PD Stage', y='PD Metric', data=df9, ax=axes[0, 2])
# sns.violinplot(x='PD Stage', y='PD Metric', data=df10, ax=axes[1, 2])
# sns.violinplot(x='PD Stage', y='PD Metric', data=df11, ax=axes[2, 2])
# sns.violinplot(x='PD Stage', y='PD Metric', data=df12, ax=axes[3, 2])

# Set labels and title
axes[0, 0].set_title('White Matter')
axes[0, 1].set_title('Gray matter')
axes[0, 2].set_title('Spinal cord')

axes[0, 0].set_ylabel('C5')
axes[1, 0].set_ylabel('C4')
axes[2, 0].set_ylabel('C3')
axes[3, 0].set_ylabel('C2')


# Show the plot
plt.show()


            
