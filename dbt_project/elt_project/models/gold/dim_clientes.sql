with
    dim_clientes as (
        select
            *,
            case
                when idade_cliente is null then 'desconhecida'
                when idade_cliente < 18 then '0-17'
                when idade_cliente between 18 and 24 then '18-24'
                when idade_cliente between 25 and 34 then '25-34'
                when idade_cliente between 35 and 44 then '35-44'
                when idade_cliente between 45 and 54 then '45-54'
                when idade_cliente between 55 and 64 then '55-64'
                else '65+'
            end AS faixa_etaria
        from 
            {{ ref('silver_clientes') }}
    )

select * from dim_clientes
