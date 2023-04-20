# Bitcoin/Crypto Fincancial Analysis - Arbitrage Opportunities 

* This project entails building a tool to help credit union members evaluate their financial health. Specifically, members should beable to do two things:* 
*   1. They should be able to assess their monthly budgets.* 
*   2. They should be able to forecast a reasonably effective retirement plan based on their current holdings of cryptocurrencies, stocks, and bonds.*
---

## *Technologies*

- **Programming Language:** Python
- **Libraries:** OS, Requests, JSON, Python-dotenv, MCForecastTools
- **Software Development Kit:** Alpaca-Trade-API
- **Framework:** JupyterLab, can also use VS Code
- **Operating Systems:** Mac OS, Microsoft Windows

---

## *Installation Guide*
1. Confirm installation of libraries: "conda list requests", "conda list json"
2. Pip install: dotenv, alpaca-trade-api
3. Create Alpaca account to obtain your API Key and Secret Key. Both of these should be listed in a file called ".env"
    
---

## *Usage*

#### Creating a plan for emergencies
*Step 1: Assessing current value of the portfoloio*
- We use free APIs for our crypto currency evaluation - 
    btc_url = "https://api.alternative.me/v2/ticker/Bitcoin/?convert=USD"
    eth_url = "https://api.alternative.me/v2/ticker/Ethereum/?convert=USD"
- Use the Alpaca API to pull in current data for stock and bond portfolio. For use here, we are using SPY and AGG to represent each.

*Step 2: Assessing emergency fund requirements*
- We have set the requirements of emergency fund to 3x the monthly income.

#### Creating a plan for retirement
*Step 1: Collect Data*
- 3 years of portfolio returns assumming a 40-60 allocation (40% bonds and 60% stocks) using the Alpaca API

*Step 2: Run simulations*
- Run a 30 year Monte Carlo Simulation to determine the range of potential portfolio returns over the next 30 years.

<img width="593" alt="1_MC" src="https://user-images.githubusercontent.com/126728866/233496375-dcd7b834-563a-4cda-8eb6-39e46d242e4b.png">

<img width="491" alt="2_distr" src="https://user-images.githubusercontent.com/126728866/233496824-468bf535-e3d4-4a2e-9a5c-0bb03a043ff7.png">

- Run a 10 year Monte Carlo Simulation to determine the range of potential portfolio returns over the next 10 years. We chose to alter the portfolio to include a 20-80 allocation (bonds to stocks) in order to test if a more aggressive approach would shorten the time to retirement. As you can see below, the distribution is greater. I would hypothesize that this is because the asset allocation is riskier. Also, the average return is still 2.5x lower than the 30 year average expected return.

<img width="481" alt="3_dist" src="https://user-images.githubusercontent.com/126728866/233496840-5ad9c490-64ae-4016-ba23-f37ff6bb0076.png">

## *Contributor*

- Michelle Silver
- Email: supersilver1978@gmail.com

---

## *License*

This software is licensed under GNU General Public License v3.0. See the [LICENSE](https://github.com/djohnst914/Loan_Qualifier_New_Feature/blob/main/LICENSE) file for details. 
