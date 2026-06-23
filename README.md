# FutureWise AI

FutureWise AI is an AI-powered financial feasibility and goal planning platform that helps users determine whether future goals, purchases, or trips are financially realistic based on their income, balances, spending patterns, and savings behavior.

## Overview

The platform analyzes user-provided financial information such as checking balance, savings balance, income, expenses, transaction history, and goal details. It then forecasts whether the goal is feasible within the desired timeline and uses an LLM-powered recommendation layer to explain the results in natural language.

Example use case:

> “Can I afford a $3,000 trip in 6 months?”

FutureWise AI evaluates the user’s current savings rate, projected balance, required monthly savings, and spending habits to provide a clear recommendation.

## Features

* Financial profile creation with checking balance, savings balance, income, and monthly expenses
* Goal-based feasibility analysis for trips, purchases, savings targets, and future plans
* Forecasting engine to calculate required monthly savings, projected savings, and remaining balance after goal completion
* Transaction analysis using Pandas for spending patterns and category-based insights
* LLM-powered explanations and personalized financial recommendations using the OpenAI API
* React dashboard for visualizing goals, spending trends, and savings projections
* Docker-based development and deployment setup

## Tech Stack

**Backend:** Python, FastAPI, SQLAlchemy
**Database:** PostgreSQL
**Frontend:** React, JavaScript
**AI/LLM:** OpenAI API
**Data Analysis:** Pandas
**DevOps:** Docker, Git, GitHub

## Planned MVP

The first version will allow users to manually enter:

* Checking balance
* Savings balance
* Monthly income
* Monthly expenses
* Goal name
* Goal cost
* Goal timeline

The system will return:

* Feasibility result
* Required monthly savings
* Current monthly savings rate
* Projected savings
* Remaining balance after reaching the goal
* AI-generated financial recommendation

## Future Enhancements

* CSV transaction upload
* Plaid Sandbox integration for simulated bank account data
* Spending category breakdowns
* Multiple financial goals
* Emergency fund analysis
* Personalized saving strategies
* Interactive charts and dashboards
* Authentication and user-specific financial history

## Project Status

This project is currently in development.
