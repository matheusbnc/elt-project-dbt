with
    dim_localidades as (
        select
            *
        from
            {{ ref('silver_localidades') }}
    )

select * from dim_localidades
