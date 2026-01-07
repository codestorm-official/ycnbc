# Download news data from CNBC! CNBC's API

<table border=1 cellpadding=10><tr><td>

#### *** IMPORTANT LEGAL DISCLAIMER ***

---

ycnbc is **not** affiliated, endorsed, or vetted by CNBC, It's an open source tool that uses Web Scraping and is intended for research and educational purposes.
</td></tr></table>

---

**ycnbc** offers a threaded and Pythonic way to news and market data from [CNBC](https://www.cnbc.com).

[Changelog »](https://github.com/asepscareer/ycnbc/blob/master/CHANGELOG.rst)

---

## Why ycnbc is compelling:

- **Simplicity**: Easy-to-use API for quick data retrieval.
- **Directness**: No retries, ensuring immediate feedback on success or failure.
- **Focus**: Specifically designed for CNBC data, providing relevant and targeted information.
- **Lightweight**: Minimal dependencies for a streamlined experience.

---

## Quick Start

---
### Requirements

- Python >=3.8+
- curl-cffi>=0.5.9
- lxml>=4.9.3
- cssselect>=1.2.0

---
### Installation

```
$ pip install ycnbc --upgrade --no-cache-dir
```

---

### Usage for Markets
```python
import ycnbc

markets = ycnbc.Markets()

quote_summary = markets.quote_summary('AAPL')
pre_markets = markets.pre_markets()
us_markets = markets.us_markets()
europe_markets = markets.europe_markets()
asia_markets = markets.asia_markets()
currencies = markets.currencies()
cryptocurrencies = markets.cryptocurrencies()
futures_and_commodities = markets.futures_and_commodities()
bonds = markets.bonds()
funds_and_etfs = markets.funds_and_etfs()
```

### Usage for news

```python
import ycnbc

news = ycnbc.News()

# Get trending news
trending_news = news.trending()

# Get latest news
latest_news = news.latest()

# Get news by category
economy_news = news.economy()
jobs_news = news.jobs()
white_house_news = news.white_house()
hospitals_news = news.hospitals()
transportation_news = news.transportation()
media_news = news.media()
internet_news = news.internet()
congress_news = news.congress()
policy_news = news.policy()
finance_news = news.finance()
life_news = news.life()
defense_news = news.defense()
europe_politics_news = news.europe_politics()
china_politics_news = news.china_politics()
asia_politics_news = news.asia_politics()
world_politics_news = news.world_politics()
equity_opportunity_news = news.equity_opportunity()
politics_news = news.politics()
wealth_news = news.wealth()
world_economy_news = news.world_economy()
central_banks_news = news.central_banks()
real_estate_news = news.real_estate()
health_science_news = news.health_and_science()
small_business_news = news.small_business()
life_insurance_news = news.life_and_health_insurance()
business_news = news.business()
energy_news = news.energy()
industrials_news = news.industrials()
retail_news = news.retail()
cybersecurity_news = news.cybersecurity()
mobile_news = news.mobile()
technology_news = news.technology()
cnbc_disruptors_news = news.cnbc_disruptors()
tech_guide_news = news.tech_guide()
social_media_news = news.social_media()
climate_news = news.climate()
```

Note:

- URL pages containing news content that have the `PRO` tag still cannot be retrieved using this library.

---

### Legal Stuff

**ycnbc** is distributed under the **Apache Software License**. See
the [LICENSE.txt](./LICENSE.txt) file in the release for details.

---

### P.S.

Please drop me a note with any feedback you have.

**Asep Saputra**