# Bitcoin Manager

Manage all your daily currency operations with this. From listening
to events such as rate raise/drop with custom limits, trigger buys,
trigger sells, to simple account management as current balance in
different currencies, fees, historic balance, etc... 

#### Bitcoin agent

Right now, I'll work using [Ripio](https://ripio.com/) but
the idea is to make a service decoupled from specific bitcoin agents,
so you can quickly setup the application and have it working
with any provider.

### Core services

* Currency Reporter
    * Get Currency Rates
* Wallet
    * Available funds
    * Current balance
    
### Setup

1. Install requirements
2. Set `funds.csv` with your own values

#### WIP

* Check balance (USD / $)
* Trigger sell
* Trigger buy