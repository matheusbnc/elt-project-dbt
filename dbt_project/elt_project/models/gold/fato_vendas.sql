with
    fato_vendas as (
        select
            *
        from
            {{ ref('silver_vendas') }}
    )

select * from fato_vendas