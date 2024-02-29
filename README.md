This folder focuses on PMI estimation.

### File information
./notebooks
* 01_generate_pmi_per_img.ipynb and 02_create_master_dataset.ipynb need to be run in order to create ../data/img_PMIs.csv, ../data/img_PMIs_no_negs.csv, and ../data/master_dataset.[csv and pkl]. The master dataset includes all images with a valid PMI and all available image features (demographic, anatomical, and decay-related). 

* 03_gelderman_subset_master_dataset.ipynb subsets the master dataset.

* create_temp_hum_features.ipynb creates temperature and humidity features the data: /data/anau/temp_humidity_data/.

* create_weather_related_features.ipynb creates ADD and ADH features. For larger datasetsuse ../create_weather_related_features_parallelized.py.

* Notebooks prefixed with "Gelderman" focus on the set of images labeled with Gelderman et al.'s stages of decay and used for the SOD classification task.  
