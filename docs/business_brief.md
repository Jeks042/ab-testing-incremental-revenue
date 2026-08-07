# Business Decision Brief

## Decision context

A retail marketing team needed to determine whether email activity created incremental commercial value, which of two campaign treatments should be preferred, and whether customer-level personalisation justified replacing a simpler fixed campaign policy.

The analysis was designed around the business decision rather than campaign reporting alone. The central question was not whether treated customers spent more in total, but whether the treatment caused additional spend and whether that incremental value remained attractive after contribution margin and contact cost were applied.

## Stakeholders

The decision is relevant to Marketing, CRM, Finance and Customer Analytics teams.

Marketing and CRM require a clear treatment recommendation. Finance requires the recommendation to remain viable under explicit margin and campaign-cost assumptions. Customer Analytics requires any segmentation or personalisation decision to be supported by evidence of genuine treatment heterogeneity or out-of-sample policy value.

## Decision metric

The primary commercial outcome is **spend per eligible customer** because it preserves the randomised intention-to-treat comparison across all assigned customers.

Commercial value is expressed as:

```text
incremental spend per eligible customer
× contribution margin
− contact cost per treated customer
− any additional treatment-specific cost
```

Visit rate and conversion rate are supporting behavioural outcomes rather than substitutes for the primary commercial measure.

## Decision hierarchy

The completed analysis addressed four linked decisions:

1. Did either email treatment create incremental value relative to No E-Mail?
2. Did Men's E-Mail outperform Women's E-Mail directly?
3. Did treatment effects vary enough across pre-treatment customer characteristics to justify a manual segment rule?
4. Did a personalised treatment policy improve profit reliably enough on held-out randomised data to replace the strongest fixed treatment?

## Final business decision

**Men's E-Mail is the recommended operating treatment when campaign economics clear the documented threshold. The current personalised targeting policy should not be deployed.**

Relative to No E-Mail, Men's E-Mail increased spend per eligible customer by approximately **£0.77**. It also outperformed Women's E-Mail directly by approximately **£0.35 per eligible customer**.

At the reference assumptions of **40% contribution margin** and **£0.10 contact cost per customer**, Men's E-Mail generated approximately **£208 incremental profit per 1,000 eligible customers**.

No pre-specified segment interaction remained significant after multiplicity adjustment, and the held-out personalised policies did not demonstrate sufficiently precise profit improvement over Men's-send-to-all.

## Decision boundaries

The recommendation is conditional on the stated campaign economics and the observed experiment context. It should be revisited if contribution margin, delivery cost, creative cost, customer mix or campaign design changes materially.

A future personalised policy should be approved only after prospective or otherwise adequately powered randomised evaluation demonstrates reliable incremental profit beyond the fixed Men's E-Mail benchmark.
