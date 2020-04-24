

## Installation
Ref: https://spacy.io/usage
Ref: https://github.com/explosion/spacy-models

(OSX/pip/python 3.x)

```shell
$ python -m venv .env
$ source .env/bin/activate
$ pip install --upgrade pip
# pip install -U , upgrade
$ pip install spacy
$ python -m spacy validate
```

Install Lemmatization lookup tables
```
$ pip install spacy-lookups-data
```

### Compile from source

```shell
$ git clone https://github.com/explosion/spaCy 
$ cd spacy
$ python -m venv .env
$ source .env/bin/activate
$ export PYTHONPATH=`pwd`
$ pip install -r requirements.txt
$ python setup.py build_ext --inplace
```

### Run Tests

```shell
$ python -c "import os; import spacy; print(os.path.dirname(spacy.__file__))"
$ pip install -r requirements.txt
$ python -m pytest [spacy directory]            # basic tests
$ python -m pytest [spacy directory] --slow     # basic and slow tests
```

## Install Models
Ref: https://github.com/explosion/spaCy 

(Example Language: English, Loading style: Use spacy.load())

```shell
$ python -m spacy download en_core_web_sm
$ python
>>> import spacy
>>> nlp = spacy.load("en_core_web_sm")
>>> doc = nlp("This is a sentence.")
>>> print([(w.text, w.pos_) for w in doc])

```

### Use your own models


## spacy101

### Terms

| Name                          | Description |
| --                            | --          |
| Tokenization                  | Segmenting text into words, punctuations marks etc. |
| Part-of-speech (POS) Tagging  | Assigning word types to tokens, list verb or noun. |
| Dpendency Parsing             | Assigning syntactic dependency labels, describing the relations between individual tokens, like subject or object. |
| Lemmatization                 | Assigning the base forms of words. For example, the lemma of "was" is "be", and the lemma of "rats" is "rat". |
| Sentence Boundary Detection (SBD) | Finding and segmenting individual sentences. |
| Named Entity Recognition (NER) | Labelling named "real-world" objects, like persons, companies or locations. |
| Entity Linking (EL)           | Disambiguating textual entitles to unique identifiers in a Kownledge Base. |
| Similarity                    | Comparing words, text spans and documents and how similar they are to each other. |
| Text Classification           | Assigning categories or labels to a whole document, or parts of a document. |
| Rule-based Matching           | Finding sequences of tokens based on their texts and linguistic annotations, similar to regular expressions. |
| Training                      | Updating and improving a statistical model's predictions. |
| Serialization                 | Saving objects to files or byte strings. |


### Statistical models

Typical components:
- Binary weights: for the part-of-speech tagger, dependency parser and named entity recognizer to predict those annotations in context.
- Lexical entries: in the vocabulary, i.e. words and their context-independent attributes like the shape or spelling.
- Data files: like lemmatization rules and lookup tables.
- Word vectors: i.e. multi-dimensional meaning representations of words that let you determine how similar they are to each other.
- Configuration options: like the language and processing pipeline settins

### Linguistic annotations

spacy.load() : loading a model, return a Language object, we usually call it nlp. Calling the nlp object on a string of text will return a processed Doc:

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billlion")
for token in doc:
    print(token.text, token.pos_, token.dep_)

```

#### Tokenization
First, the raw text is split on whitespace characters. Then the tokenizer processes the text from left to right. On each substring, it performs two checks:
1. Does the substring match a tokenizer exception rule ?
2. Can a prefix, suffix or infix be split off ?

Tokenizer exception: Special-case rule to split a string into several tokens or prevent a token from being split when punctuation rules are applied.
Prefix: Character(s) at the beginning, e.g. $, (, "
Suffix: Character(s) at the end, e.g. km, ), ", !
Infix: Character(s) in between, e.g. -, --, /, _

![](img/tokenization.svg)

Tokenization rules References:
- Adding languages
- Customizing the tokenizer

#### Part-of-speech tags and dependencies
spaCy encodes all strings to hash values to reduce memory usage and improve efficiency. So to get the readable string representation of an attribute, we need to add an underscore _ to its name.

Text: The original word text.
Lemma: The base form of the word.
POS: The simple part-of-speech tag.
Tag: The detailed part-of-speech tag.
Dep: Syntactic dependency, i.e. the relation between tokens.
Shape: The word shape - capitialization, punctuation, digits.
is alpha: Is the token an alpha character ?
is stop: Is the token part of a stop list, i.e. the most common words of the language ?

spacy.explain() will show you a short description of a tag.

#### Named Entities
Named entities are available as the ents property of a Doc

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

```

Text: The original entity text.
Start: Index of start of entity in the Doc.
End: Index of end of entity in the Doc.
Label: Entity label, i.e. type.


#### Word vectors and similarity
Similarity is determined by comparing word vectors or "word embeddings", multi-dimensional meaning representations of a word. Word vectors can be generated using an algorithm like word2vec
Inorder to use real word vectors, you need to download a larger model.

Example, check if a token has a vector assigned, and get the L2 norm

```python
import spacy

nlp = spacy.load("en_core_web_md")
tokens = nlp("dog cat banana afskfsd")

for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)

```

Text: the original token text.
has_vector: Does the token have a vector representation ?
Vector norm: The L2 norm of the token's vector (the square root of the sum of the values squared)
OOV: Out-of-vocabulary

Predicting similarity is useful for building recommendation systems or flagging duplicates. Each Doc, Span and Token comes with a .similarity() method that lets you compare it with another object, and determine the similarity.


### Pipelines

![](img/pipeline.svg)

The processing pipeline always depends on the statistical model and its capabilities. Each model will specify the pipeline to use in its meta data.

The tokenizer is not part of the regular pipeline.

References:
- language processing pipelines


### Vocab, hashes and lexemes
Whenever possible, spaCy tries to store data in a vocabulary, the Vocab, that will be shared by multiple documents. To save memory, spaCy also encodes all strings to hash values.

![](img.img/vocab_stringstore.svg)

Token: A word, punctuation mark etc. in context, including its attributes, tags and dependencies.
Lexeme: A "word type" with no context. Includes the word shape and flags.
Doc: A processed container of tokens in context.
Vocab: The collection of lexemes.
StringStore: The dictionary mapping hash values to strings.

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("I love coffee")
print(doc.vocab.strings["coffee"])  # 3197928453018144401
print(doc.vocab.strings["3197928453018144401"])  # 'coffee'

```

#### Knowledge Base
A knowledge base(KB) is created by first adding all entities to it. Next, for each potential mention or alias, a list of relevant KB IDs and their prior probabilities is added. The sum of these prior probabilities should never exceed 1 for any given alias.

Mention: A textual occurrence of a named entity.
KB ID: A unique identifier referring to a particular real-world concept.
Alias: A plausible synonym or description for a certain KB ID.
Prior probability: The probability of a certain mention resolving to a certain KB ID, prior to knowing anything about the context in which the mention is used.
Entity vector: A pretrained word vector capturing the entity description.

```python
import spacy
from spacy.kb import KnowledgeBase

# load the model and create an empty KB
nlp = spacy.load('en_core_web_sm')
kb = KowledgeBase(vocab=nlp.vocab, entity_vector_length=3)

# adding entities
kb.add_entity(entity="Q1004791", freq=6, entity_vector=[0, 3, 5])
kb.add_entity(entity="Q42", freq=342, entity_vector=[1, 9, -3])
kb.add_entity(entity="Q5301561", freq=12, entity_vector=[-2, 4, 2])

# adding aliases
kb.add_alias(alias="Douglas", entities=["Q1004791", "Q42", "Q5301561"], probabilities=[0.6, 0.1, 0.2])
kb.add_alias(alias="Douglas Adams", entities=["Q42"], probabilities=[0.9])

print()
print("Number of entities in KB:", kb.get_size_entities()) # 3
print("Number of aliases in KB:", kb.get_size_aliases()) # 2

```

Given a textual entity, the Knowledge Base can provide a list of plausible candidates or entity identifiers. The EntityLinker will take this list of candidates as input, and disambiguate the mention to the most probable identifier, given the document context.

```python

candidates = kb.get_candidates("Douglas")
for c in candidates:
    print(" ", c.entity_, c.prior_prob, c.entity_vector)

```

### Serialization

Pickle is Python's built-in object persistence system. It lets you transfer arbitrary Python objects between processes. This is usually used to load an object to and from disk, but it's also used for distributed computing, e.g. with PySpark or Dask. When you unpickle an object, you're agreeing to execute whatever code it contains. It's like calling eval() on a string. -- so don't unpickle objects from untrusted sources.

All container classes, i.e. Language (nlp), Doc, Vocab and StringStore have the following methods avaiable:
- to_bytes: return bytes
- from_bytes: return object
- to_disk
- from_disk: return object






