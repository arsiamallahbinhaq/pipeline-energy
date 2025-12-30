with source as (

    select *
    from {{ source('raw', 'raw_energy') }}

),

cleaned as (

    select
        country,
        iso_code,
        year::int as year,

        -- Energy
        round(primary_energy_consumption::numeric, 2)
            as primary_energy_consumption,

        -- Population
        population::bigint as population,

        -- GDP
        gdp::numeric as gdp

    from source
    where primary_energy_consumption is not null
      and year >= 2000
      and country is not null

)

select * from cleaned
