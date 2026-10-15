
# BILLIONAIRE STATISTICS: Age differences 
# between male and female billionaires across countries

# Research Question:
# How do the age distributions of male and female billionaires compare,
# and does this vary across countries?

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis


## LOAD DATA

os.chdir("/Users/laurenbuchan/MAT2007/PROJECT")

billionaires = pd.read_csv(
    "/Users/laurenbuchan/Desktop/programming/Billionaires Statistics Dataset copy.csv"
)

print(billionaires.head())
print(billionaires.columns)


## CLEAN DATA

# Keep only age and gender
age_gender = billionaires[
    ["age", "gender"]
].dropna().copy()


# SEPARATE MALE AND FEMALE AGES

male_ages = age_gender[
    age_gender["gender"] == "M"
]["age"]

female_ages = age_gender[
    age_gender["gender"] == "F"
]["age"]


## BASIC STATISTICS

male_n = len(male_ages)
female_n = len(female_ages)

male_mean = male_ages.mean()
female_mean = female_ages.mean()

male_std = male_ages.std()
female_std = female_ages.std()

male_median = male_ages.median()
female_median = female_ages.median()

# Standard error of the mean
male_se = male_std / np.sqrt(male_n)
female_se = female_std / np.sqrt(female_n)

# Skewness
male_skewness = skew(male_ages)
female_skewness = skew(female_ages)

# Excess kurtosis
male_kurtosis = kurtosis(male_ages)
female_kurtosis = kurtosis(female_ages)


## PRINT BASIC RESULTS

print("\n===================================")
print("AGE RESULTS")
print("===================================")

print(f"Male sample size: {male_n}")
print(f"Female sample size: {female_n}")

print(f"\nMale mean age: {male_mean:.2f}")
print(f"Female mean age: {female_mean:.2f}")

print(f"\nMale median age: {male_median:.2f}")
print(f"Female median age: {female_median:.2f}")

print(f"\nMale standard deviation: {male_std:.2f}")
print(f"Female standard deviation: {female_std:.2f}")

print(f"\nMale standard error: {male_se:.2f}")
print(f"Female standard error: {female_se:.2f}")

print(f"\nMale skewness: {male_skewness:.3f}")
print(f"Female skewness: {female_skewness:.3f}")

print(f"\nMale kurtosis: {male_kurtosis:.3f}")
print(f"Female kurtosis: {female_kurtosis:.3f}")


## FIGURE 1:
# MALE VS FEMALE AGE DISTRIBUTION
# WITH SKEWNESS AND KURTOSIS

plt.figure(
    num="Figure 1",
    figsize=(10, 6)
)

# Same bins for both genders
bins = np.arange(
    15,
    106,
    5
)

# MALE HISTOGRAM

plt.hist(
    male_ages,
    bins=bins,
    density=True,
    alpha=0.55,
    color="steelblue",
    edgecolor="black",
    label="Male"
)

# FEMALE HISTOGRAM

plt.hist(
    female_ages,
    bins=bins,
    density=True,
    alpha=0.55,
    color="lightcoral",
    edgecolor="black",
    label="Female"
)

# MEAN LINES

plt.axvline(
    male_mean,
    color="blue",
    linestyle="--",
    linewidth=2,
    label=f"Male mean = {male_mean:.1f}"
)

plt.axvline(
    female_mean,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Female mean = {female_mean:.1f}"
)

# ADD SKEWNESS AND KURTOSIS TO FIGURE 1

statistics_text = (
    f"Male:\n"
    f"Skewness = {male_skewness:.2f}\n"
    f"Kurtosis = {male_kurtosis:.2f}\n\n"
    f"Female:\n"
    f"Skewness = {female_skewness:.2f}\n"
    f"Kurtosis = {female_kurtosis:.2f}"
)

plt.text(
    0.03,
    0.97,
    statistics_text,
    transform=plt.gca().transAxes,
    verticalalignment="top",
    fontsize=10,
    bbox=dict(
        boxstyle="round",
        facecolor="white",
        alpha=0.85
    )
)

# FIGURE 1 LABELS

plt.title(
    "Age Distribution of Male and Female Billionaires"
)

plt.xlabel(
    "Age (years)"
)

plt.ylabel(
    "Probability Density"
)

plt.legend()

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()

plt.show()


## FIGURE 2:
# CUMULATIVE AGE DISTRIBUTION WITH UNCERTAINTY BANDS

# Sort ages
male_sorted = np.sort(male_ages)
female_sorted = np.sort(female_ages)


# CALCULATE CUMULATIVE PERCENTAGES

male_cumulative = (
    np.arange(1, len(male_sorted) + 1)
    / len(male_sorted)
    * 100
)

female_cumulative = (
    np.arange(1, len(female_sorted) + 1)
    / len(female_sorted)
    * 100
)


# CALCULATE APPROXIMATE STATISTICAL UNCERTAINTY

# For a cumulative proportion p:
# uncertainty = sqrt(p(1-p)/N)

male_p = male_cumulative / 100
female_p = female_cumulative / 100

male_uncertainty = (
    np.sqrt(
        male_p * (1 - male_p) / len(male_sorted)
    )
    * 100
)

female_uncertainty = (
    np.sqrt(
        female_p * (1 - female_p) / len(female_sorted)
    )
    * 100
)

# CREATE FIGURE 2

plt.figure(
    num="Figure 2",
    figsize=(10, 6)
)


# MALE CUMULATIVE DISTRIBUTION

plt.plot(
    male_sorted,
    male_cumulative,
    color="steelblue",
    linewidth=2.5,
    label="Male"
)

plt.fill_between(
    male_sorted,
    male_cumulative - male_uncertainty,
    male_cumulative + male_uncertainty,
    color="steelblue",
    alpha=0.18
)


# FEMALE CUMULATIVE DISTRIBUTION

plt.plot(
    female_sorted,
    female_cumulative,
    color="lightcoral",
    linewidth=2.5,
    label="Female"
)

plt.fill_between(
    female_sorted,
    female_cumulative - female_uncertainty,
    female_cumulative + female_uncertainty,
    color="lightcoral",
    alpha=0.20
)


# ADD MEDIAN LINES

plt.axvline(
    male_median,
    color="steelblue",
    linestyle="--",
    alpha=0.7,
    label=f"Male median = {male_median:.1f}"
)

plt.axvline(
    female_median,
    color="lightcoral",
    linestyle="--",
    alpha=0.7,
    label=f"Female median = {female_median:.1f}"
)


# FIGURE 2 LABELS

plt.title(
    "Cumulative Age Distribution of Male and Female Billionaires"
)

plt.xlabel(
    "Age (years)"
)

plt.ylabel(
    "Cumulative Percentage (%)"
)

plt.ylim(
    0,
    105
)

plt.grid(
    alpha=0.25
)

plt.legend()

plt.tight_layout()

plt.show()


# FIGURE 3:
# AVERAGE AGE BY COUNTRY AND GENDER

# Keep only rows with age, gender, and country information
location_data = billionaires[
    [
        "age",
        "gender",
        "countryOfCitizenship"
    ]
].dropna().copy()


# FIND TOP 5 COUNTRIES

top_countries = (
    location_data["countryOfCitizenship"]
    .value_counts()
    .head(5)
    .index
)

# Keep only those countries
location_data = location_data[
    location_data["countryOfCitizenship"].isin(
        top_countries
    )
]

# CALCULATE MEAN AGE BY COUNTRY AND GENDER

mean_age_country = (
    location_data
    .groupby(
        [
            "countryOfCitizenship",
            "gender"
        ]
    )["age"]
    .mean()
    .unstack()
)


# CALCULATE STATISTICAL UNCERTAINTY

# Standard deviation
std_age_country = (
    location_data
    .groupby(
        [
            "countryOfCitizenship",
            "gender"
        ]
    )["age"]
    .std()
    .unstack()
)

# Number of billionaires
n_country = (
    location_data
    .groupby(
        [
            "countryOfCitizenship",
            "gender"
        ]
    )["age"]
    .count()
    .unstack()
)

# Standard error
uncertainty_country = (
    std_age_country
    / np.sqrt(n_country)
)


# PREPARE GRAPH

countries = mean_age_country.index

x = np.arange(
    len(countries)
)

bar_width = 0.36

plt.figure(
    num="Figure 3",
    figsize=(10, 6)
)

# MALE

plt.bar(
    x - bar_width / 2,
    mean_age_country["M"],
    width=bar_width,
    yerr=uncertainty_country["M"],
    capsize=5,
    color="steelblue",
    edgecolor="black",
    label="Male"
)

# FEMALE

plt.bar(
    x + bar_width / 2,
    mean_age_country["F"],
    width=bar_width,
    yerr=uncertainty_country["F"],
    capsize=5,
    color="lightcoral",
    edgecolor="black",
    label="Female"
)


# FIGURE 3 LABELS

plt.title(
    "Average Age of Billionaires by Country and Gender"
)

plt.xlabel(
    "Country"
)

plt.ylabel(
    "Average Age (years)"
)

plt.xticks(
    x,
    countries,
    rotation=20
)

plt.legend()

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()

plt.show()