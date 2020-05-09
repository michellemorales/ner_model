# Samsung Sentence NER Tagger

This repository contains the necessary 

For questions please contact Michelle Morales: ms.morales3@gmail.com

**Table of Contents**
- [Overview of NER tool built](#Overview)
- [How to set-up NER tool](#Set-up)
- [How to run tool](#Running)
- [Extra resources](#More)

# Overview

This repository provides the Samsung Next NER Tagger! The tagger is provided in an easy to run Docker container to enable a speedy set-up. The NER model is trained using the CONLL2003 training dataset, validation and testing sets are used during evaluation.

![Dataset Overview](https://github.com/michellemorales/samsung_interview/blob/master/images/CONLL%20Dataset%20Overview.png)

For an overivew of the CONLL2003 dataset, please see: https://www.clips.uantwerpen.be/conll2003/ner/

The model is trained using the [Simple Transformers library](https://github.com/ThilinaRajapakse/simpletransformers) following the guidance provided in this very helpful [blog post](https://towardsdatascience.com/simple-transformers-named-entity-recognition-with-transformer-models-c04b9242a2a0Performance ) written by Thilina Rajapakse, the Simple Transformers main creator.

The Bert based model is trained using the parameters: 

`NERModel('bert', 'bert-base-cased', use_cuda=False, args={'learning_rate': 2e-5, 'overwrite_output_dir': True, 'reprocess_input_data': True})`

Performance on the CONLL test set is:

| Metric  | Performance |
| ------------- | ------------- |
| eval_loss | Content Cell  |
| precision  | Content Cell  |
|recall|Performance|
| f1_score | X|

eval_loss': 2.4489634037017822,
 'precision': 0.058823529411764705,
 'recall': 0.36363636363636365,
 'f1_score': 0.10126582278481011
 

# Set-up
1. Install Docker: https://docs.docker.com/get-docker/
2. Run 
# Run-time
# More resources

`Exploratory Analysis.ipynb` 
- Loads CONLL2003 dataset (https://github.com/davidsbatista/NER-datasets/tree/master/CONLL2003)
- Formats the data into a pandas dataframe, where each row is a sentence
- Generates descriptive statistics on the data and visualizes them for easy interpretability 

In order to run the analysis, you need to download the CONLL2003 data make sure to update `conll_data_path` to point to the correct directory on your machine:

`conll_data_path = 'path_to_conll_folder/CONLL2003/'`

If all the dependencies are installed, the notebook should run succesfully. The notebook includes a preprocessed dataframe to allow for further analyses. The dataframe has the following format:

![Dataframe format](https://github.com/michellemorales/samsung_interview/blob/master/images/Dataframe%20Format.png)

To understand the dataset the following charts are also created:



![Entity Distribution](https://github.com/michellemorales/samsung_interview/blob/master/images/CONLL%20Entity%20Distribution.png)

