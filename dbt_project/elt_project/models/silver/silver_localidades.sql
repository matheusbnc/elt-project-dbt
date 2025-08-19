with
    silver_localidades as (
        select
            localidade_id AS id_localidade,
            cidade AS cidade_localidade,
            estado AS estado_localidade,
            pais AS pais_localidade,
            cep AS cep_localidade
        from
            {{ source('bronze', 'raw_localidades') }}
    )

select * from silver_localidades
