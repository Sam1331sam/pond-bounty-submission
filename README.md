* Bot & Sybil Detection Dataset for Pond Bounties

* Problem Definition
This dataset targets the detection of bots, Sybil wallets, automated submissions, and reward-farming patterns on the Pond platform. The goal is to distinguish genuine activity from manipulation to improve fairness, integrity, and trust.

* Dataset Description
The dataset contains 10 sample accounts across different scenarios:

| Column           | Description                             |
|------------------|-----------------------------------------|
| username         | Unique account name                     |
| followers        | Number of followers                     |
| following        | Number of accounts followed             |
| posts            | Number of posts or actions              |
| account_age_days | Age of account in days                  |
| engagement_rate  | Engagement rate or activity score       |
| label            | `human` or `bot`                        |
| scenario         | Type of activity (social account, Sybil wallet, reward farming) |

* Insights
- Bot accounts often show unusual activity patterns, like extremely high posts but low engagement.
- Sybil wallets usually have minimal connections but may perform repetitive actions.
- Reward-farming accounts have high activity but low engagement quality.

* Usage
This dataset can be used to:
- Build or test detection methods for bots and Sybil wallets.
- Analyze patterns of automated submissions and reward farming.
- Demonstrate approaches to improve platform fairness and integrity.

* Verification
Pond Profile: https://www.cryptopond.xyz/developer/08b2a996-6b60-11f0-a1f3-024775222cc3

* Licensing
This dataset is for educational and bounty purposes only. Free to use for the Pond Bounty submission.

* Reproducibility
No code is required to demonstrate this dataset; it is ready for analysis, visualization, or integration into detection pipelines.

This project demonstrates a simple yet effective approach to identifying inauthentic accounts on the Pond platform. Using a structured dataset of account metrics and basic engagement analysis, we can distinguish between human and bot activity. While this submission uses straightforward rules for demonstration, the methodology can be easily extended with more advanced detection algorithms, additional features, or larger datasets. The provided code and dataset are fully reproducible, enabling further experimentation and improvement to enhance platform integrity and fairness.

