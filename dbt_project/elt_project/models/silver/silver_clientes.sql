with
    silver_clientes as (
        select
            cliente_id AS id_cliente,
            nome AS nome_cliente,
            idade AS idade_cliente,
            genero AS genero_cliente
        from
            {{ source('bronze', 'raw_clientes') }}

    )

select * from silver_clientes