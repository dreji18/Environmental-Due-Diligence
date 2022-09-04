## EnvBert - BERT for Environment Domain

EnvBert is an easy-to-use Python library built on top of Bert models to identify essential environmental data as a part of due diligence in environmental site assessments.

<img align="right" width="100%" src="https://user-images.githubusercontent.com/49631017/188302857-6b6fe277-7062-46fb-b473-d15827168e5a.png">

[![Downloads](https://static.pepy.tech/personalized-badge/envbert?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)](https://pepy.tech/project/envbert)
<a href="https://pypi.org/project/EnvBert/">
    <img alt="CI" src="https://img.shields.io/badge/pypi-v1.0.6-orange">
</a>

| Feature  | Output  |
|---|---|
| EDD Prediction | Categorizes the Environment data under different classes |
| Relevancy | Classify whether it's relevant or not for the Environment domain |
| Ranking | Relevance probability is returned against the predicted classes |
| Fine-tuning | Train for your custom Environment data and save, use your model |


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install EnvBert

```bash
pip install EnvBert
```

## Usage

### Predict with EnvBert 
```python
# load all the functions
from EnvBert.due_diligence import *

# returns the predicted class along with the probability of the actual EnvBert model
doc = """
	weathered shale was encountered below the surface area with fluvial deposits. 
	Sediments in the coastal plain region are found above and below the bedrock 
	with sandstones and shales that form the basement rock"
      """

envbert_predict(doc)

```
### Fine-tune over EnvBert with your custom Environment data and labels
```python
# load all the functions
from EnvBert.due_diligence import *

# define training config
training_config = {
    'learning_rate':5e-5,
    'epochs':10,
    'batch_size':16,
    'sentence column name':'Sentence', #training sentences column name
    'label column name': 'label', #encoded labels column name
    'save_dir': r'XX\XX\XXX' #model save path
    }

"""
please make sure you encode your labels
provide the save_dir path to automatically save the model after training
'sentence column name' and 'label column name' are mandatory fields in training config
you can tweak the other parameters or it will be taken by default
"""

# Train the model with just 1 line
new_model, new_tokenizer = finetune(df, training_config) #df is the dataframe with your sentences and labels

```
in case of any errors please install the package versions given in the requirements file

### Load your fine-tuned model and predict
```python
load_dir = r'XX\XX\XXX' #model save path

finetuned_model = finetune_predict(load_dir)

# single sentence prediction
doc= "contamination have been reported and remediation havent been carried out"
finetuned_model.sent(doc)

# predict over a dataframe column
df['prediction'] = finetuned_model.df(df, 'Sentence') #df is the dataframe and 'Sentence' is the column name

```

## About
This Package is part of the Research topic "AI for Environment Due-Diligence" conducted by Afreen Aman, Deepak John Reji. If you use this work (code, model or dataset), Please cite us and star at: AI for Environment Due-Diligence, (2022), GitHub repository, https://github.com/dreji18/environmental-due-diligence

## License
[MIT](https://choosealicense.com/licenses/mit/) License
