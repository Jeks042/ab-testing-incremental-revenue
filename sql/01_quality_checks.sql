-- Hillstrom email experiment: source-data and experiment-integrity checks
-- Assumes a table named hillstrom_email_experiment.

-- 1. Row count
SELECT COUNT(*) AS row_count
FROM hillstrom_email_experiment;

-- 2. Treatment allocation
SELECT
    segment,
    COUNT(*) AS customers,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS allocation_pct
FROM hillstrom_email_experiment
GROUP BY segment
ORDER BY segment;

-- 3. Missing values by field
SELECT
    SUM(CASE WHEN recency IS NULL THEN 1 ELSE 0 END) AS recency_missing,
    SUM(CASE WHEN history_segment IS NULL THEN 1 ELSE 0 END) AS history_segment_missing,
    SUM(CASE WHEN history IS NULL THEN 1 ELSE 0 END) AS history_missing,
    SUM(CASE WHEN mens IS NULL THEN 1 ELSE 0 END) AS mens_missing,
    SUM(CASE WHEN womens IS NULL THEN 1 ELSE 0 END) AS womens_missing,
    SUM(CASE WHEN zip_code IS NULL THEN 1 ELSE 0 END) AS zip_code_missing,
    SUM(CASE WHEN newbie IS NULL THEN 1 ELSE 0 END) AS newbie_missing,
    SUM(CASE WHEN channel IS NULL THEN 1 ELSE 0 END) AS channel_missing,
    SUM(CASE WHEN segment IS NULL THEN 1 ELSE 0 END) AS segment_missing,
    SUM(CASE WHEN visit IS NULL THEN 1 ELSE 0 END) AS visit_missing,
    SUM(CASE WHEN conversion IS NULL THEN 1 ELSE 0 END) AS conversion_missing,
    SUM(CASE WHEN spend IS NULL THEN 1 ELSE 0 END) AS spend_missing
FROM hillstrom_email_experiment;

-- 4. Invalid binary values
SELECT 'mens' AS field_name, mens::TEXT AS invalid_value, COUNT(*) AS rows
FROM hillstrom_email_experiment
WHERE mens NOT IN (0, 1) OR mens IS NULL
GROUP BY mens
UNION ALL
SELECT 'womens', womens::TEXT, COUNT(*)
FROM hillstrom_email_experiment
WHERE womens NOT IN (0, 1) OR womens IS NULL
GROUP BY womens
UNION ALL
SELECT 'newbie', newbie::TEXT, COUNT(*)
FROM hillstrom_email_experiment
WHERE newbie NOT IN (0, 1) OR newbie IS NULL
GROUP BY newbie
UNION ALL
SELECT 'visit', visit::TEXT, COUNT(*)
FROM hillstrom_email_experiment
WHERE visit NOT IN (0, 1) OR visit IS NULL
GROUP BY visit
UNION ALL
SELECT 'conversion', conversion::TEXT, COUNT(*)
FROM hillstrom_email_experiment
WHERE conversion NOT IN (0, 1) OR conversion IS NULL
GROUP BY conversion;

-- 5. Monetary consistency
SELECT
    SUM(CASE WHEN history < 0 THEN 1 ELSE 0 END) AS negative_history_rows,
    SUM(CASE WHEN spend < 0 THEN 1 ELSE 0 END) AS negative_spend_rows,
    SUM(CASE WHEN spend > 0 AND conversion <> 1 THEN 1 ELSE 0 END)
        AS positive_spend_without_conversion,
    SUM(CASE WHEN conversion = 1 AND spend <= 0 THEN 1 ELSE 0 END)
        AS conversion_without_positive_spend,
    SUM(CASE WHEN conversion = 1 AND visit <> 1 THEN 1 ELSE 0 END)
        AS conversion_without_visit
FROM hillstrom_email_experiment;

-- 6. Exact duplicate rows
SELECT
    recency,
    history_segment,
    history,
    mens,
    womens,
    zip_code,
    newbie,
    channel,
    segment,
    visit,
    conversion,
    spend,
    COUNT(*) AS duplicate_count
FROM hillstrom_email_experiment
GROUP BY
    recency,
    history_segment,
    history,
    mens,
    womens,
    zip_code,
    newbie,
    channel,
    segment,
    visit,
    conversion,
    spend
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;

-- 7. Baseline descriptive balance by treatment arm
SELECT
    segment,
    COUNT(*) AS customers,
    AVG(recency) AS avg_recency,
    AVG(history) AS avg_prior_year_spend,
    AVG(mens) AS prior_mens_share,
    AVG(womens) AS prior_womens_share,
    AVG(newbie) AS new_customer_share
FROM hillstrom_email_experiment
GROUP BY segment
ORDER BY segment;
