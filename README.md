<img src="https://raw.githubusercontent.com/abdullah5-ig/abdullah5-ig/main/assets/minecraft-banner.gif" width="100%" alt="Abdullah Naqvi — Data &amp; Fintech Analyst">

<p align="center">
  <a href="https://abdullah-naqvi.vercel.app">
    <img src="https://img.shields.io/badge/Portfolio-3d54e6?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio"></a>
  <a href="https://www.linkedin.com/in/abdullah-naqvi-34162733b">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:abdullahnaqvi131@gmail.com">
    <img src="https://img.shields.io/badge/Email-0d1424?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
</p>

---

I'm studying **Business Data Analytics** at COMSATS University Islamabad, and data
analysis is what I do. SQL, Python, Power BI and Excel — cleaning messy data,
running the analysis, and building the charts and reports that make a finding
useful to someone who has to act on it.

I'm particularly interested in **fintech**: pricing, risk and customer economics.
Most of what I have built comes down to the same question a financial analyst
asks — what is this actually worth, and what should we do about it.

I recently finished an internship as a Market Research Analyst at Vertex Digital
Ventures, analysing US industry and buyer data to test whether an opportunity was
real before anyone spent money on it.

What I care about is the question behind the numbers — not just what the data
says, but whether it still holds up when you go looking for reasons it might not.

<br>

# Featured work

<br>

## [Diamond Prices — a correlation pointing the wrong way](https://github.com/abdullah5-ig/diamond-price-intelligence)

**A pricing model on 53,794 assets, accurate to 7%. But the finding beats the model.**

<img src="https://raw.githubusercontent.com/abdullah5-ig/abdullah5-ig/main/assets/diamonds-paradox.png" alt="Better clarity looks cheaper until you control for size" width="100%">

In the raw data, **better quality diamonds look cheaper**. Flawless stones average
$2,871 while the worst clarity grade averages $5,057. The cause is size — flawless
diamonds here are half the weight. Compare diamonds of a similar size and a
**2.6× premium** appears, exactly as you would expect.

The first chart isn't noisy or borderline. It's clean, easy to read, and
confidently wrong. Any pricing advice built on it would be backwards, and a better
model would not have caught it, because the model was never the thing that was
broken.

| Metric | Result |
|---|---|
| R² on unseen data | **0.983** |
| Average error | **$263** |
| Diamonds analysed | **53,794** |

Also repaired real data problems: 20 diamonds recorded with a physical
measurement of zero, and 146 duplicate rows removed before splitting so the model
could not cheat.

`Python` · `pandas` · `NumPy` · `scikit-learn` · `Matplotlib`

<br>

## [Telco Customer Churn — who leaves, and who to call](https://github.com/abdullah5-ig/telco-churn-retention-analytics)

**Customer economics: predicting churn is the easy half, deciding who is worth spending on is the hard half.**

<img src="https://raw.githubusercontent.com/abdullah5-ig/abdullah5-ig/main/assets/churn-profit-curve.png" alt="Money made at each probability cutoff" width="100%">

A retention offer costs money whether or not the customer was going to leave. So I
worked out the point where calling someone pays off, from the offer cost and what a
customer is worth. That gives a cutoff of **27%**, not the default 50% — worth
**$9,270** more on the campaign.

Testing every cutoff empirically gives 27%. The cost formula gives 26% on its own.
Two different methods, almost the same answer.

<img src="https://raw.githubusercontent.com/abdullah5-ig/abdullah5-ig/main/assets/churn-calibration.png" alt="The model was overconfident before calibration" width="60%">

**The part I'd most want a reviewer to look at.** The model was overstating its
confidence — reporting 37% risk where the real rate was 20%. Accuracy scores
cannot see this; only a calibration chart can. It mattered because the cutoff above
is derived from those probabilities, so left uncorrected it moved the answer by 15
percentage points for no real reason.

| Metric | Result |
|---|---|
| Accuracy (ROC-AUC) | **0.845** across three compared models |
| Campaign value | **$47,357**, versus $38,087 at the default cutoff |
| Customers | **7,043** real records |

`Python` · `pandas` · `scikit-learn` · `Seaborn`

<br>

## Portfolio Risk & Return Analysis

**Which assets actually paid for the risk they carried?**

<img src="https://raw.githubusercontent.com/abdullah5-ig/abdullah5-ig/main/assets/security-market-line.png" alt="Security Market Line: return plotted against beta for four listed companies" width="100%">

Measured the risk and return of four listed companies — FFC, MARI, OGDC and FCCL
— and built two portfolios from them. Calculated returns from historical price
data, then measured how volatile each stock was and how much it moved with the
wider market.

Scored every asset on risk-adjusted return using the **Sharpe ratio, Treynor
ratio and Jensen's Alpha**, then plotted them against the Security Market Line.
The chart is the finding: **only FFC sits above the line**, meaning it was the
one asset paying more return than its risk level called for. The other three sat
below it.

`Excel` · `CAPM` · `Beta & Volatility` · `Sharpe & Treynor` · `Jensen's Alpha`

<br>

## Also on my [portfolio site](https://abdullah-naqvi.vercel.app)

**Diabetes Risk Prediction** — Python pipeline on 20,000 health and survey records.
96% accuracy overall, catching 65% of real cases with only 170 false alarms.

All four projects, with the full write-ups, are on the site.

<br>

# Toolkit

**Analysis**
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)

**Modelling**
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![SciPy](https://img.shields.io/badge/Statistics-8CAAE6?style=flat-square&logo=scipy&logoColor=white)

**Charts & dashboards**
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square)
![Seaborn](https://img.shields.io/badge/Seaborn-2d7d9a?style=flat-square)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Excel](https://img.shields.io/badge/Excel-217346?style=flat-square&logo=microsoftexcel&logoColor=white)

**Research** — market and customer research · opportunity sizing · competitor analysis

<br>

# How I work

Four habits that show up in both projects above, because they're the difference
between an analysis that looks finished and one that holds:

**Check the data before cleaning it.** Count the problem, work out what caused it,
then decide. In the churn data, 11 blank billing totals all belonged to customers
who joined that month. Their real total was zero, not missing. Filling them with an
average would have invented money that never existed.

**Assume the first pattern you see has something behind it.** Ask what else changes
along with it before you believe it. The diamonds project is that lesson in one
chart.

**Never let the model see the test data early.** All preparation happens inside the
pipeline so it only ever learns from training data. Preparing data before splitting
it quietly inflates every score.

**Say what the analysis cannot tell you.** Both repos end with their own
limitations. A result without its weaknesses stated is not a finished result.

<br>

# Certifications

- **Google Data Analytics Professional Certificate** — Google · Coursera
- **Foundations: Data, Data, Everywhere** — Google · Coursera

<br>

---

<p align="center">
  <sub>Open to opportunities in data analytics, business intelligence and fintech.<br>
  Islamabad, Pakistan</sub>
</p>
