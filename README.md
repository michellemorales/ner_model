# Sentence NER (Named Entity Recognition) Tagger
For questions please contact Michelle Morales: ms.morales3@gmail.com

**Table of Contents**
- [Overview of NER model](#Overview)
- [Running NER model](#Running)
- [More resources & discussion](#More)

# Overview

This repository provides a NER Tagger! The tagger is provided in an easy to run Docker container to enable a speedy set-up. The NER model is trained using the [CONLL2003 training dataset](https://github.com/davidsbatista/NER-datasets/tree/master/CONLL2003), validation and testing sets are used during evaluation.

![Dataset Overview](https://github.com/michellemorales/ner_model/blob/master/images/CONLL%20Dataset%20Overview.png)

The CONLL2003 dataset is a corpus of news data, tagged with various information, including named entities. The following entities are included in the corpus, with the following distribution:

![Entity Distribution](https://github.com/michellemorales/ner_model/blob/master/images/Entities%20Distribution.png)

For more information on the CONLL2003 dataset, please see: https://www.clips.uantwerpen.be/conll2003/ner/

The model is trained using the [Simple Transformers library](https://github.com/ThilinaRajapakse/simpletransformers) following the guidance provided in this very helpful [blog post](https://towardsdatascience.com/simple-transformers-named-entity-recognition-with-transformer-models-c04b9242a2a0Performance ) written by Thilina Rajapakse, the Simple Transformers main creator.

The Bert based model is trained using the following parameters: 

`NERModel('bert', 'bert-base-cased', use_cuda=False, args={'learning_rate': 2e-5, 'overwrite_output_dir': True, 'reprocess_input_data': True})`

This model results show a reasonable baseline for an initial model. Results are shown in the table below:

**Performance on the CONLL test set**

| Metric  | Performance |
| ------------- | ------------- |
| eval_loss | 0.106 |
| precision  | 0.893 |
|recall| 0.909 |
| f1_score | 0.900  |
 
# Run-time

To run this model on your machine, you only need to follow 3 simple steps:

1. Install Docker: https://docs.docker.com/get-docker/
2. Pull the docker image: `docker pull michellemorales/ner_model:latest`
4. Run docker container:

In order to the run the tagger, open up Terminal and type in this command, replace the example sentence with your own:

`docker run ner-tagger "This is the sentence I want to tag with named entities."`

Do **not** forget to include quotes! The command will return the sentence tagged with the named entities, like so:

![Docker Example](https://github.com/michellemorales/ner_model/blob/master/images/Docker%20Container%20Example.png)

Alternatively, we provide the Python script for loading and predicting using the trained model in the `ner_model/` directory. Simply change into that directory and run: `python run_ner.py "This is the sentence I want to tag with named entities."`. Make sure you have `simpletransformers` library installed. 

# More Resources & Discussion

## Resources:

The jupyter notebook that was used for training the model is included is also included in this repository. You can view it here:

`Data Analysis and Development.ipynb`

The notebook does the following:

- Loads CONLL2003 dataset
- Formats the data into a pandas dataframe, where each row is a sentence (format is given in a screenshot below)
- Generates descriptive statistics on the data and visualizes them for easy interpretability 
- Trains the Bert NER transformer model using the CONLL training data

![Dataframe format](https://github.com/michellemorales/ner_model/blob/master/images/Dataframe%20Format.png)

In order to run the analysis, you need to have all the dependencies installed:

`pip install -r requirements.txt`

Then, download the CONLL2003 data and make sure to update `conll_data_path` to point to the correct directory on your machine:

`conll_data_path = 'path_to_conll_folder/CONLL2003/'`

If all the dependencies are installed, the notebook should run succesfully. 

## Discussion

This NER model provides a great proof-of-concept for how to build a tagger. Some questions/thoughts:

**1. What would you like to try next?**
CONLL English is from the Reuters corpus, which is a collection of news stories. Because the corpus does not span multiple domains (news, social media, emails,blog posts, etc.) it may cause the NER model to not generalize to new domains. Given our intended user for this model is our Data Broker client, we may want to re-consider retraining this with relevant domain data. As a first next step, I would like to evaluate its performane on a labeled dataset from a more informal domain, like Twitter.

**2. Once we gather out own annotated data, could we reuse this model or would we create a new one?**
One possibility is to retrain a new model with the new data from scratch, using the same architecture. However, with a deep learning model such as the one leveraged, the more data the more likely performance will improve. Therefore, we could instead puruse a different approach where we leverage the existing model and we fine-tune it with our collected data, to help expand the model learning to our relevant domain.

**3. We plan to expand our offering to multiple different langauges next year. Could we use a single model for multiple languages? Is there a way we could leverage our existing model for that?**
CONLL2003 also includes German files, which should allow for the same approach using a different data source. However, that approach would require finding a good amount of data in each new language, in order to try and attain the same performance. Luckily, we do not need to train a new model for each language added, there exist approaches, similar to the one used in this model, that allow us to train one model that can be used across several languages. Specifically, the Multilingual BERT Zero-Shot Transfer models allow us to perform zero-shot transfer from one language to another. 

