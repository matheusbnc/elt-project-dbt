with
    dim_data as (
        select
            *,
            FORMAT_DATE('%B', data_calendario) AS nome_mes
        from
            {{ ref('silver_data') }}
    )

select * from dim_data