with
    dim_produtos as (
        select
            *
        from
            {{ ref('silver_produtos') }}
    )

select * from dim_produtos
