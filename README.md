# Samsung Sentence NER Tagger

This repository contains the necessary 

For questions please contact Michelle Morales: ms.morales3@gmail.com

**Table of Contents**
- [Overview of NER tool built](#Overview)
- How to set-up NER tool
- [How to run tool](#Running)
- [Additional analysis](#Additional Analysis) - Jupyter notebook included for addiontal exploratory work

# Overview
# Additional Analysis

`Exploratory Analysis.ipynb` 
- Loads CONLL2003 dataset (https://github.com/davidsbatista/NER-datasets/tree/master/CONLL2003)
- Formats the data into a pandas dataframe, where each row is a sentence
- Generates descriptive statistics on the data and visualizes them for easy interpretability 

In order to run the analysis, you need to download the CONLL2003 data make sure to update `conll_data_path` to point to the correct directory on your machine:

`conll_data_path = 'path_to_conll_folder/CONLL2003/'`

If all the dependencies are installed, the notebook should run succesfully. The notebook includes a preprocessed dataframe to allow for further analyses. The dataframe has the following format:

![Dataframe format](https://github.com/michellemorales/samsung_interview/blob/master/images/Dataframe%20Format.png)

To understand the dataset the following charts are also created:

![Dataset Overview](https://github.com/michellemorales/samsung_interview/blob/master/images/CONLL%20Dataset%20Overview.png)

![Entity Distribution](https://github.com/michellemorales/samsung_interview/blob/master/images/CONLL%20Entity%20Distribution.png)



## Tool Overview
# Running


TODO
- add requirements
