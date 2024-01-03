# Code Challenge Jameson: Bounty Hunter

A RAG [Retrieval Augmented Generation] Implementation of the Bounty Hunter Code Challenge

## Examples

### How many businesses are there?

> make run
>
> python3 ./bounty_hunter/main.py
>
> 🤖 Please enter your question: how many businesses are there?
>
>
> Entering new AgentExecutor chain...
>
> Thought: I should use the `businesses_database` tool to find the number of businesses.
>
> Action: businesses_database
>
> Action Input: "number of businesses"
>
> Entering new SQLDatabaseChain chain...
>
> number of businesses
>
> SQLQuery:SELECT COUNT("name") AS num_businesses
> FROM businesses;
>
> SQLResult: [(98,)]
>
> Answer:There are 98 businesses in the database.
>
> Finished chain.
>
>
> Observation:There are 98 businesses in the database.
>
> I now know the final answer
>
> Final Answer: There are 98 businesses in the database.
>
> Finished chain.

### Does EvenFlow Plumbing have Wifi?

> make run
>
> python3 ./bounty_hunter/main.py
>
> 🤖 Please enter your question: Does EvenFlow Plumbing have Wifi?
>
>
> Entering new AgentExecutor chain...
>
> Thought: I need to find information about EvenFlow Plumbing's amenities.
>
> Action: businesses_database
>
> Action Input: EvenFlow Plumbing
>
> Entering new SQLDatabaseChain chain...
>
> EvenFlow Plumbing
>
> SQLQuery:SELECT name, address, phone, rating
>
> FROM businesses
>
> WHERE name = 'EvenFlow Plumbing'
>
> LIMIT 1;
>
> SQLResult:
>
> Answer:Final answer here
>
> Finished chain.
>
>
> Observation:Final answer here
>
> I now know the final answer
>
> Final Answer: EvenFlow Plumbing does not have Wifi.

## How to Run

```bash
make init - load the project with poetry and install dependencies
make load - pretune the dataset with the Yelp Fusion API and create the sqlite database
make run - run the CLI
```

### Prerequisites

- Python 3.11
- Poetry
- Make (*optional*)
- envrc (*optional*)

### Loading [Pretune] the Dataset (do this first to generate the limited local database)

```bash
make load
```

### Running the CLI

```bash
make run
```

## Solution Overview // Denouement

A small writeup can be found in [SOLUTION.md](./SOLUTION.md).

## Solution Maintainer

Jameson Stone 🥃/💎
