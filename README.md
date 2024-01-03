# metron (from ancient Greek μέτρον "measure"),

Retrieval Augmented Generation [RAG] with Chain of Thought [CoT] Analysis leveraged by Agent Architecture via LangChain

## Overview

The fundamental question `metron` seeks to answer is:

> How little data can we use to "pretune" a question?

supplemental to this central question, we also seek to answer:

> How can we leverage local data to answer a question?
> What role can RAG [Retrieval Augmented Generation] play in answering questions?
> What role can CoT [Chain of Thought] play in answering questions?
> What role can Agent architectures play in answering questions?

### Prerequisites

- [ ] [LLMSingleActionAgent](https://blog.langchain.dev/custom-agents/)
- [ ] [YELP's Fusion API](https://fusion.yelp.com/)
- [ ] [Google's Custom Search API](https://developers.google.com/custom-search/v1/overview)
- [ ] [GPT-3.5-turbo-1106](https://platform.openai.com/docs/models/gpt-3-5)
- [ ] [Ollama](https://github.com/jmorganca/ollama)
- [ ] Sqlite3

## Examples

## Installation

Initialize the python environment

```bash
make init
```

Supplement the dataset from Yelp's Fusion API into a local Sqlite3 database

```bash
make load
```

Run the CLI

```bash
make run
```

## Maintainer

J.Stone 🥃/💎
