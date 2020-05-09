#!interpreter [optional-arg]
# -*- coding: utf-8 -*-

"""
This script is used to load the Samsung Next NER pre-trained model which
is used for tagging sentences with named entities
"""

from simpletransformers.ner import NERModel
import sys

def main(sentence):
    """Predicts NER labels""" 
    model = NERModel('bert', 'outputs/', use_cuda=False) #
    predictions, raw_outputs = model.predict([sentence])
    print(predictions)

if __name__ == "__main__":
    main(sys.argv[1])