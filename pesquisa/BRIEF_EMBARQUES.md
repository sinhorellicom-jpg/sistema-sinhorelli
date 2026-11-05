# Coleta de EMBARQUES (registros de importação / BL) das NCMs da Sinhorelli

Objetivo: montar um banco de embarques reais na América Latina (importador, exportador/fornecedor, data, NCM, quantidade, unidade, valor) para saber QUEM compra, DE QUEM compra e A QUE PREÇO (o sistema divide valor ÷ quantidade sozinho).

## Onde procurar (páginas gratuitas, use WebSearch + WebFetch)
Veritrade (veritradecorp.com — perfis de empresa por país com amostras de embarques), Volza (volza.com — "import data" por HS e país, mostra linhas com data, importador, exportador, quantidade, valor), Panjiva, ImportGenius, Datasur, 52wmb, TradeAtlas, Seair/Infodriveindia/Zauba (lado exportador: China/Índia/Brasil → LatAm), Eximpedia, Tendata, ImportYeti, notícias. Pesquise por HS + país ("3909.50 import data Colombia", "wet blue 410411 Mexico importers shipment", "PU microfiber leather 392113 Peru import"), e por exportador ("JBS wet blue export Mexico shipment", "Yantai Joye Microfiber shipments", "Miracll TPU export Colombia", "Xuchuan PU system export Peru").

## Prioridade: para quem os NOSSOS fornecedores vendem
Toda rodada, procure também pelo lado do exportador: embarques de JBS (Brasil, Argentina/CSA-N, Uruguai, EUA), Zendaleather, Yantai Joye Microfiber, Miracll, Xuchuan, BIQ, Matrizaria Polako, Formello e Hiper Solados para importadores da América Latina (páginas de fornecedor no 52wmb, ImportGenius, Panjiva, Volza, TradeAtlas, Seair/Eximpedia). O campo "exportador" deve trazer o nome como aparece no registro.

## Regras
- Só registre embarque que a fonte mostra de verdade: data (ou mês/ano), importador e pelo menos quantidade OU valor. Nunca invente nem estime números; se um campo não aparece, null.
- Quantidade com a unidade exatamente como aparece (kg, ton, m2, sqft/pés², pcs, pares, rolos, unidades). Valor em USD, dizendo se é FOB, CIF ou "não informado".
- SÓ registros com data de 2026 em diante (data do embarque/BL/declaração). Registro sem data ou anterior a 2026 não entra.
- Importador na América Latina (inclui Brasil e México). Exportador: qualquer país.

## Saída
Grave UM arquivo JSON (lista) no caminho indicado, cada item com exatamente estas chaves:
{"data": "aaaa-mm-dd" ou "aaaa-mm" ou "aaaa", "importador": str, "pais": "MEXICO|COLOMBIA|EQUADOR|PERU|BOLIVIA|CHILE|ARGENTINA|PARAGUAI|URUGUAI|VENEZUELA|GUATEMALA|EL SALVADOR|HONDURAS|NICARAGUA|COSTA RICA|PANAMA|REP DOMINICANA|BRASIL", "exportador": str|null, "origem": str|null (país de origem), "ncm": str (ex.: "3909.50"), "produto": str (descrição curta como aparece), "quantidade": number|null, "unidade": str|null, "valor": number|null (USD), "tipo_valor": "FOB|CIF|não informado", "preco_unit_fonte": number|null (só se a fonte mostrar o preço unitário), "fonte": url}
Responda no final só com quantos embarques por NCM e o caminho do arquivo.
