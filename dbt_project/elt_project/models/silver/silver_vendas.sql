with
    silver_vendas as (
        select
            data_id AS id_data,
            cliente_id AS id_cliente,
            localidade_id AS id_localidade,
            produto_id AS id_produto,
            quantidade AS quantidade_venda,
            total_venda AS valor_total_venda
        from
            {{ source('bronze', 'raw_vendas') }}
    )

select * from silver_vendas
