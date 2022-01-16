## EnvBert - BERT for Environment Domain

EnvBert is an easy-to-use Python library built on top of Bert models to identify essential environmental data as a part of due diligence in environmental site assessments.

[![Downloads](https://static.pepy.tech/personalized-badge/envbert?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)](https://pepy.tech/project/envbert)
<a href="https://pypi.org/project/EnvBert/">
    <img alt="CI" src="https://img.shields.io/badge/pypi-v0.0.6-orange">
</a>

| Feature  | Output  |
|---|---|
| EDD Prediction | Categorizes the Environment data under different classes |
| Relevancy | Classify whether it's relevant or not for the Environment domain |
| Ranking | Relevance probability is returned against the predicted classes |

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install EnvBert

```bash
pip install EnvBert
```

## Usage

```python
# returns the predicted class along with the probability 
from EnvBert.due_diligence import *

doc = """
	weathered shale was encountered below the surface area with fluvial deposits. 
	Sediments in the coastal plain region are found above and below the bedrock 
	with sandstones and shales that form the basement rock"
      """

predict(doc)

```

## About
This Package is part of the Research topic "AI for Environment Due-Diligence" conducted by Afreen Aman, Deepak John Reji, Shaina Raza. If you use this work (code, model or dataset),

Please cite us and star at: AI for Environment Due-Diligence, (2022), GitHub repository, https://github.com/dreji18/environmental-due-diligence

## License
[MIT](https://choosealicense.com/licenses/mit/) License
