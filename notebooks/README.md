# Notebook Workflow

The notebooks will be developed in a fixed order so that conclusions are not produced before experiment integrity is established.

## Planned sequence

1. `01_data_validation.ipynb`
   - Load the source file
   - Reconcile row and column counts
   - Review missing values and duplicates
   - Test treatment allocation
   - Assess baseline balance
   - Document outcome inconsistencies

2. `02_experiment_analysis.ipynb`
   - Build arm-level descriptive summaries
   - Estimate visit, conversion and spend effects
   - Calculate confidence intervals
   - Review multiplicity, precision and practical significance

3. `03_segment_effects.ipynb`
   - Evaluate pre-specified segments
   - Estimate interaction effects
   - Separate exploratory patterns from supported differences

4. `04_profit_and_targeting.ipynb`
   - Apply commercial assumptions
   - Estimate break-even conditions
   - Compare send-to-all, rule-based and model-based policies
   - Evaluate uplift and profit under capacity constraints

## Reproducibility rule

Each notebook will call functions from `src/` rather than hiding important logic inside isolated notebook cells. Final tables used in the dashboard and decision memo will be exported from reproducible code.
