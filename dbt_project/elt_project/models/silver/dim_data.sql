with
    dim_data as (
        select
            data_id AS id_data,
            data AS data_calendario,
            ano AS ano_calendario,
            mes AS mes_calendario,
            dia AS dia_calendario,
            dia_da_semana AS dia_semana,
            trimestre AS trimestre_calendario,
            fim_de_semana AS fim_de_semana_flag
        from
            {{ source('bronze', 'raw_data') }}
    )

select * from dim_data
