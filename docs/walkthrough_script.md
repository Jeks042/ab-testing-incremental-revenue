# Three-Minute Project Walkthrough

## Opening - 20 seconds

This project evaluates whether two email treatments created genuine incremental revenue and whether customer-level targeting could improve the decision. I used the 64,000-customer Hillstrom randomized experiment, with Men's E-Mail, Women's E-Mail and No E-Mail control groups.

## Experiment integrity - 25 seconds

Before estimating effects, I checked the schema, missing values, outcome consistency, treatment allocation and baseline balance. The sample-ratio test produced a p-value of 0.9037, and the largest absolute standardized mean difference was 0.0086, so I proceeded with all assigned customers in an intention-to-treat analysis.

## Average treatment effects - 45 seconds

Both treatments increased the primary commercial outcome, spend per eligible customer. Men's E-Mail increased spend by 0.770 versus control, with a 95% confidence interval from 0.484 to 1.052. Women's E-Mail increased spend by 0.424, with an interval from 0.152 to 0.686.

I then compared the two active treatments directly. Men's E-Mail produced an additional 0.345 spend units per customer versus Women's E-Mail. The confidence interval was 0.044 to 0.666, and the multiplicity-adjusted p-value was 0.0305. This supported Men's E-Mail as the stronger treatment.

## Commercial decision - 35 seconds

I translated the causal spend effects into contribution profit rather than treating all observed revenue as incremental. At a 40% contribution margin and a 0.10 contact cost, Men's E-Mail generated approximately 208 profit units per 1,000 eligible customers, compared with 70 for Women's E-Mail. Men's also had the wider break-even cost buffer.

## Segmentation and targeting - 40 seconds

The pre-specified segment interaction tests did not support a manual targeting rule after multiplicity adjustment. I then trained separate outcome models for each randomized arm and evaluated candidate policies on a 30% holdout.

The profit-aware model showed a point uplift of 18.3 per 1,000 customers versus Men's-send-to-all, but the 95% bootstrap interval ranged from -129.1 to +155.4. Because that interval included zero and meaningful losses, I rejected the model for deployment.

## Close - 15 seconds

The final recommendation is Men's E-Mail to eligible customers when campaign economics clear the threshold. The important project lesson is that a model can rank customers and still fail to demonstrate reliable incremental profit. I separated predictive performance, causal treatment effects and deployable policy value throughout the analysis.
