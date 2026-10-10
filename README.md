# DevStudio — Orders Automation Dashboard

A portfolio demonstration of CSV-based order processing, a Python REST API, and a lightweight interactive dashboard.

**Live demo:** https://devstudio-orders-dashboard.vercel.app

## Features
- Read sample orders from CSV
- Calculate order totals from quantity and unit price
- Filter orders by payment status
- Show paid revenue and order counts
- Display results in a responsive web dashboard

## Technology
Python standard library, HTML, CSS, JavaScript, CSV, Vercel Serverless Functions.

## API
`GET /api/orders` — list all orders, count, and paid revenue.

`GET /api/orders?status=paid` — filter orders by status.

## Data
Sample records only; no real customer data. This is a demonstration, not a production order-management platform.

## Deployment
The production demo is hosted on Vercel. The original deployed source consists of `api/index.py`, `index.html`, `sample_orders.csv`, and `vercel.json`. These files will be restored to this repository from the deployment.

## Status
Source restoration in progress. README published first to initialize the repository.

## Author
DevStudio — business automation and practical web tools.
