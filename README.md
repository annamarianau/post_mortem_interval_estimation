This repo focuses on PMI estimation.

### Folder/File details
###### ./
* create_weather_related_features_parallelized.py - script that calculates ADD and ADH for different thresholds. Uses python's multiprocessing package to speed up code. Use ./notebooks/add_ADD_ADH_features.ipynb to preapre data for this script. 

###### ./data
* img_PMIs.csv and img_PMIs_no_negs.csv - images aligned with a PMI. The latter contains no negative PMIs. Files were created with ../notebooks/01_generate_pmi_per_image.ipynb.
* master_dataset.[csv and pkl] - images aligned with available image attributes, such as donor demographics, anatomical data (existing and predicted), and stage of decay data (existing and predicted). Files were created with ../notebooks/02_create_master_dataset.ipynb.
* master_dataset_w_ADD.csv - same as master_dataset.[csv and pkl] but with ADD features. 
* unique_donor_data.[csv and pkl] - output from ../notebooks/add_ADD_ADH_features.ipynp and input to create_weather_related_features_parallelized.py.
* Gelderman_SOD_cohort - this folder contains data related to the Gelderman SOD-labeled cohort. 

###### ./notebooks
* 01_generate_pmi_per_img.ipynb and 02_create_master_dataset.ipynb need to be run in order to create ../data/img_PMIs.csv, ../data/img_PMIs_no_negs.csv, and ../data/master_dataset.[csv and pkl].

* add_ADD_ADH_features.ipynb - prepares data for create_weather_related_features_parallelized.py.

* add_temp_hum_features.ipynb - creates different temperature and humidity aggregated features.

* Gelderman_SOD_cohort_analysis.ipynb - analyzes the Gelderman SOD-labeled cohort to create a stronger dataset for PMI estimation task. 

* sample_for_additional_labeling.ipynb - samples data for additional SOD labeling based on the analysis results of Gelderman_SOD_cohort_analysis.ipynb. Additional details here: https://github.com/icputrd/pmi_estimation/tree/main/labeling.

* sample_for_additional_labeling2.ipynb - samples the entire decay process for certain donors. Was done to have some donors whose entire decay process is SOD-labeled. Additional details here: https://github.com/icputrd/pmi_estimation/tree/main/labeling.

* process_additional_labels.ipynb - processes the additional samples from sample_for_additional_labeling.ipynb and prepares a dataset for PMI estimation.

###### ./regression_analysis
This folder contains all code and data for 4th paper (PMI estimation).


