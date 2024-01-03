# Solution Overview // Denouement

## Challenge Background

Information about this code challenge can be found in the [bounty_hunter README.md](./bounty_hunter/README.md). However a quick summary is as follows:

> We've included a dataset of businesses around the Bay Area. Your task is to
> write a crawler that collects and stores as much information as you
> can about these businesses in a structured format.
>
> In addition, we'd like you to provide the ability to run the following queries
> on your result dataset:
>
> - What are the address and phone number of each business?
> - How many businesses are registered in a given zip code (94608)?
> - How many of the businesses offer wifi at their location?
> - Which businesses serve alcohol?

## Implementation

### Overview

The solution is implemented as a CLI application that allows the user to enter a question and receive an answer. The CLI application is implemented in [bounty_hunter/main.py](./bounty_hunter/main.py).

Instead of using a static dataset or a one-time scraping of the web, this solution does a "pre-tune" of a limited dataset from [Yelp's Fusion API](https://fusion.yelp.com/). Academically, I tried to use the least amount of prefetched data as possible to demonstrate the ability of the RAG [Retrieval Augmented Generation] Architecture, and the ability of the LangChain [LLMSingleActionAgent](https://blog.langchain.dev/custom-agents/) to leverage local data supplemented with an active Google Search to return specific answers to any number of questions.

### Limitations

Fundamentally, inference and prompt engineering are nascent fields, and because our pre-tuned data is (purposefully) limited, this is somewhat prone to "hallucination" as evidenced by specific, general questions of the dataset:

> How many businesses are there?

In such a case, we've defined a specific prompt to remind the llm that the local dataset is sufficient in its response

> First leverage the `businesses_database` tool to search for the business referenced in the input, then use the `google_search` tool to find additional information.
>
> If the question is about the number of businesses, use the `businesses_database` tool and answer. Do not use the `google_search` tool.

Better pre-tuning/fine-tuning, one-time static scrape should sufficient to cure some large percentage of the "hallucinations" but additional prompt fine-tuning/engineer should make this tool quite accurate.

### Cost

- [Yelp's Fusion API](https://fusion.yelp.com/) is free for 5000 requests per day. This solution uses 1 request per business, so the solution can be run 5000 times per day but we usually only run a single time for pre-tuning purposes
- [Google's Custom Search API](https://developers.google.com/custom-search/v1/overview) is free for 100 requests per day. This solution uses 1-5 request per question, so the solution can be run 100 times per day.
- [GPT-3.5-turbo-1106](https://platform.openai.com/docs/models/gpt-3-5)

In practice, however, the cost comes out to about $0.05 per $70 API calls (or, roughly, "questions asked").

## Future Improvements

- [ ] Add more data to the database to improve the quality of retrieval answers
- [ ] Leverage Ollama/local LLM because our task scope is small/specific and we can run locally
- [ ]

## Appendix

- [LLMSingleActionAgent](https://blog.langchain.dev/custom-agents/)
- [YELP's Fusion API](https://fusion.yelp.com/)
- [Ollama](https://github.com/jmorganca/ollama)
