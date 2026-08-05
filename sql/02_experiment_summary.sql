-- Hillstrom email experiment: descriptive arm-level outcomes
-- Assumes a table named hillstrom_email_experiment.

WITH arm_summary AS (
    SELECT
        segment,
        COUNT(*) AS customers,
        SUM(visit) AS visits,
        AVG(visit::NUMERIC) AS visit_rate,
        SUM(conversion) AS conversions,
        AVG(conversion::NUMERIC) AS conversion_rate,
        SUM(spend) AS total_revenue,
        AVG(spend) AS revenue_per_customer,
        AVG(CASE WHEN conversion = 1 THEN spend END) AS average_order_value,
        AVG(CASE WHEN spend = 0 THEN 1.0 ELSE 0.0 END) AS zero_spend_share
    FROM hillstrom_email_experiment
    GROUP BY segment
)
SELECT *
FROM arm_summary
ORDER BY segment;

-- Absolute differences against control.
WITH arm_summary AS (
    SELECT
        segment,
        COUNT(*) AS customers,
        AVG(visit::NUMERIC) AS visit_rate,
        AVG(conversion::NUMERIC) AS conversion_rate,
        AVG(spend) AS revenue_per_customer
    FROM hillstrom_email_experiment
    GROUP BY segment
),
control AS (
    SELECT *
    FROM arm_summary
    WHERE segment = 'No E-Mail'
)
SELECT
    treatment.segment AS treatment,
    treatment.customers,
    treatment.visit_rate,
    control.visit_rate AS control_visit_rate,
    treatment.visit_rate - control.visit_rate AS visit_rate_difference,
    treatment.conversion_rate,
    control.conversion_rate AS control_conversion_rate,
    treatment.conversion_rate - control.conversion_rate
        AS conversion_rate_difference,
    treatment.revenue_per_customer,
    control.revenue_per_customer AS control_revenue_per_customer,
    treatment.revenue_per_customer - control.revenue_per_customer
        AS revenue_per_customer_difference
FROM arm_summary AS treatment
CROSS JOIN control
WHERE treatment.segment <> 'No E-Mail'
ORDER BY treatment.segment;

-- Segment-level descriptive effects. These are exploratory until supported by
-- uncertainty estimates and interaction tests in the statistical analysis.
WITH segment_summary AS (
    SELECT
        history_segment,
        segment,
        COUNT(*) AS customers,
        AVG(visit::NUMERIC) AS visit_rate,
        AVG(conversion::NUMERIC) AS conversion_rate,
        AVG(spend) AS revenue_per_customer
    FROM hillstrom_email_experiment
    GROUP BY history_segment, segment
),
control AS (
    SELECT
        history_segment,
        customers AS control_customers,
        visit_rate AS control_visit_rate,
        conversion_rate AS control_conversion_rate,
        revenue_per_customer AS control_revenue_per_customer
    FROM segment_summary
    WHERE segment = 'No E-Mail'
)
SELECT
    treatment.history_segment,
    treatment.segment AS treatment,
    treatment.customers,
    control.control_customers,
    treatment.visit_rate - control.control_visit_rate AS visit_rate_difference,
    treatment.conversion_rate - control.control_conversion_rate
        AS conversion_rate_difference,
    treatment.revenue_per_customer - control.control_revenue_per_customer
        AS revenue_per_customer_difference
FROM segment_summary AS treatment
JOIN control
    ON treatment.history_segment = control.history_segment
WHERE treatment.segment <> 'No E-Mail'
ORDER BY treatment.history_segment, treatment.segment;
