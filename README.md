# Samsung Sentence NER (Named Entity Recognition) Tagger
For questions please contact Michelle Morales: ms.morales3@gmail.com

**Table of Contents**
- [Overview of NER model](#Overview)
- [Running NER model](#Running)
- [More resources & discussion](#More)

# Overview

This repository provides the Samsung Next NER Tagger! The tagger is provided in an easy to run Docker container to enable a speedy set-up. The NER model is trained using the CONLL2003 training dataset, validation and testing sets are used during evaluation.

![Dataset Overview](https://github.com/michellemorales/samsung_interview/blob/master/images/CONLL%20Dataset%20Overview.png)

The CONLL2003 dataset is a corpus of news data, tagged with various information, including named entities. 

![Entity Distribution](https://github.com/michellemorales/samsung_interview/blob/master/images/CONLL%20Entity%20Distribution.png)

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
 
# Run-time

1. Install Docker: https://docs.docker.com/get-docker/
2. Run 
3. Run docker container:

`docker run ner-tagger "This is the sentence I want to tag with named entities."`

# More Resources & Discussion

The jupyter notebook that was used for training the model is included is also included in this repository. You can view it here:

`Data Analysis and Development.ipynb`

The notebook does the following:

- Loads CONLL2003 dataset (https://github.com/davidsbatista/NER-datasets/tree/master/CONLL2003)
- Formats the data into a pandas dataframe, where each row is a sentence (format is given in a screenshot below)
- Generates descriptive statistics on the data and visualizes them for easy interpretability 
- Trains the Bert NER transformer model using the CONLL training data

![Dataframe format](https://github.com/michellemorales/samsung_interview/blob/master/images/Dataframe%20Format.png)

In order to run the analysis, you need to have all the dependencies installed:

`pip install -r requirements.txt`

Then, download the CONLL2003 data and make sure to update `conll_data_path` to point to the correct directory on your machine:

`conll_data_path = 'path_to_conll_folder/CONLL2003/'`

If all the dependencies are installed, the notebook should run succesfully. 


CONLL2003 also includes German files, which should allow for the same approach using a different data source. 
CONLL English is from the Reuters corpus, which is a collection of news stories. Because of the corpus does not span multiple domains (news, social media, emails,blog posts, etc.) it may cause the NER model to not generalize to new domains. Given our intended user for this model is our Data Broker client, we may want to re-consider retraining this with relevant domain data. 
