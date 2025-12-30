select
    country,
    year,

    -- Total energy consumption
    sum(primary_energy_consumption)
        as total_energy_consumption,

    -- Metrics
    max(population) as population,
    avg(gdp) as avg_gdp,

    -- Derived metric
    sum(primary_energy_consumption)
        / nullif(max(population), 0)
        as energy_per_capita

from {{ ref('stg_energy') }}
group by country, year
