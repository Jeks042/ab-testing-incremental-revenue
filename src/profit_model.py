"""Commercial sensitivity model for email-treatment decisions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import pandas as pd


@dataclass(frozen=True)
class ProfitAssumptions:
    contribution_margin: float
    contact_cost_per_customer: float
    additional_variable_cost_per_customer: float = 0.0
    fixed_campaign_cost: float = 0.0

    def validate(self) -> None:
        if not 0 <= self.contribution_margin <= 1:
            raise ValueError("Contribution margin must be between 0 and 1.")
        for name, value in (
            ("contact_cost_per_customer", self.contact_cost_per_customer),
            (
                "additional_variable_cost_per_customer",
                self.additional_variable_cost_per_customer,
            ),
            ("fixed_campaign_cost", self.fixed_campaign_cost),
        ):
            if value < 0:
                raise ValueError(f"{name} cannot be negative.")


@dataclass(frozen=True)
class ProfitResult:
    recipients: int
    incremental_revenue_per_customer: float
    incremental_revenue: float
    incremental_contribution: float
    variable_campaign_cost: float
    fixed_campaign_cost: float
    incremental_profit: float
    incremental_profit_per_customer: float
    break_even_contact_cost: float


def evaluate_profit(
    recipients: int,
    incremental_revenue_per_customer: float,
    assumptions: ProfitAssumptions,
) -> ProfitResult:
    """Convert a treatment effect into a transparent profit estimate."""
    assumptions.validate()
    if recipients <= 0:
        raise ValueError("Recipients must be greater than zero.")

    incremental_revenue = recipients * incremental_revenue_per_customer
    incremental_contribution = (
        incremental_revenue * assumptions.contribution_margin
    )
    variable_campaign_cost = recipients * (
        assumptions.contact_cost_per_customer
        + assumptions.additional_variable_cost_per_customer
    )
    incremental_profit = (
        incremental_contribution
        - variable_campaign_cost
        - assumptions.fixed_campaign_cost
    )
    profit_per_customer = incremental_profit / recipients
    break_even_contact_cost = (
        incremental_revenue_per_customer * assumptions.contribution_margin
        - assumptions.additional_variable_cost_per_customer
        - assumptions.fixed_campaign_cost / recipients
    )

    return ProfitResult(
        recipients=recipients,
        incremental_revenue_per_customer=incremental_revenue_per_customer,
        incremental_revenue=incremental_revenue,
        incremental_contribution=incremental_contribution,
        variable_campaign_cost=variable_campaign_cost,
        fixed_campaign_cost=assumptions.fixed_campaign_cost,
        incremental_profit=incremental_profit,
        incremental_profit_per_customer=profit_per_customer,
        break_even_contact_cost=break_even_contact_cost,
    )


def sensitivity_table(
    recipients: int,
    incremental_revenue_per_customer: float,
    contribution_margins: Iterable[float],
    contact_costs: Iterable[float],
    additional_variable_cost_per_customer: float = 0.0,
    fixed_campaign_cost: float = 0.0,
) -> pd.DataFrame:
    """Evaluate profit across contribution-margin and contact-cost scenarios."""
    records: list[dict[str, float | int]] = []

    for margin in contribution_margins:
        for contact_cost in contact_costs:
            assumptions = ProfitAssumptions(
                contribution_margin=margin,
                contact_cost_per_customer=contact_cost,
                additional_variable_cost_per_customer=(
                    additional_variable_cost_per_customer
                ),
                fixed_campaign_cost=fixed_campaign_cost,
            )
            result = evaluate_profit(
                recipients=recipients,
                incremental_revenue_per_customer=incremental_revenue_per_customer,
                assumptions=assumptions,
            )
            records.append(
                {
                    "recipients": recipients,
                    "contribution_margin": margin,
                    "contact_cost_per_customer": contact_cost,
                    "incremental_revenue_per_customer": (
                        incremental_revenue_per_customer
                    ),
                    "incremental_profit": result.incremental_profit,
                    "incremental_profit_per_customer": (
                        result.incremental_profit_per_customer
                    ),
                    "break_even_contact_cost": result.break_even_contact_cost,
                }
            )

    return pd.DataFrame.from_records(records)
