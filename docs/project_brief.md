# Project Brief

## Project title

A/B Testing and Incremental Revenue: Email Campaign Decision System

## Stakeholder

Marketing Director, supported by CRM, Finance and Customer Analytics teams.

## Decision to be made

The business must decide whether to continue using email campaigns, which treatment should be preferred and how to allocate limited campaign capacity without confusing observed revenue with revenue caused by treatment.

## Business context

A campaign can generate visits and purchases while still failing to create incremental profit. Some customers may have purchased without receiving an email, some segments may respond differently, and treatment cost can remove apparent gains.

This project therefore treats the experiment as a commercial decision problem rather than a dashboard exercise.

## Primary decision metric

The primary commercial metric is **incremental profit per eligible customer**.

It is derived from:

```text
Incremental revenue per customer
× contribution margin
− contact cost per treated customer
− any additional treatment-specific cost
```

The project will also report visit and conversion effects as supporting behavioural metrics.

## Primary comparisons

1. Men's email versus no-email control
2. Women's email versus no-email control
3. Men's email versus women's email, interpreted as a secondary comparison

## Primary outcomes

- Revenue per eligible customer
- Conversion rate
- Visit rate

## Guardrails

- No unexplained deterioration in average order value among converters
- No recommendation based only on relative percentage lift
- No targeting model trained on post-treatment outcomes as input features
- No subgroup recommendation without sufficient sample size and uncertainty reporting
- No claim that a predictive response model estimates incremental impact

## Commercial scenarios

The final recommendation will be tested under multiple assumptions for:

- contribution margin;
- contact cost;
- treatment-specific creative or fulfilment cost;
- campaign capacity; and
- minimum acceptable return.

## Deliverable standard

A recruiter or senior stakeholder should be able to understand the decision, evidence, uncertainty, assumptions and recommendation without opening the analysis notebook.

The final public pack will contain:

- executive dashboard;
- two-page decision memo;
- reproducible code and SQL;
- methodology and limitations;
- concise portfolio case study; and
- interview-ready explanation of the experiment.
