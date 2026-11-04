# Pesquisa de compradores das NCMs da Sinhorelli (representante comercial de exportação)

A Sinhorelli representa fornecedores que vendem estes produtos (NCM / SH):

| NCM | Produto | Fornecedor representado |
|---|---|---|
| 4104.11 / 4104.19 | Couro bovino wet blue (flor e raspa) | JBS (Brasil, Argentina, Uruguai, EUA), Zendaleather |
| 4104.41 / 4104.49 | Couro bovino crust (seco) | JBS Argentina |
| 4107 | Couro bovino acabado | JBS |
| 3921.13 | Microfibra / sintético PU, espuma PU laminada (forros, cabedal) | Yantai Joye Microfiber (China) |
| 3921.12 | Sintético PVC | Yantai |
| 3921.90 | Contraforte/couraça termoadesiva (hotmelt) | Yantai |
| 5603.14 | Não-tecido (forro de gáspea, palmilha de montagem/strobel) | Yantai |
| 5602 | Feltro | Yantai |
| 5901.90 | Palmilha antiperfuro (anti punch) | Yantai |
| 6406.90 | Biqueira de aço / palmilhas / partes de calçado | Yantai |
| 6005.37 | Malha/mesh (air mesh, forro) | Yantai |
| 5609 | Cadarços (refletivos) | Yantai |
| 3907.99 | Poliol poliéster — sistema PU para solado (confirmado em contrato da Xuchuan: XC-6002C, XC-200, D-1010) | Xuchuan (China) |
| 3909.50 | Pré-polímero/isocianato do sistema PU para solado (Xuchuan, XC-8280) e TPU (Miracll) | Xuchuan, Miracll (China) |
| 3506.91 | Adesivos para calçado (PU, PVC, cola de contato) | BIQ (Brasil) |
| 3814.00 | Solventes | BIQ |
| 8480.71 | Moldes para solado (injeção/compressão) | Matrizaria Polako (Brasil) |
| 3926.90 | Fôrmas plásticas para calçado | Formello (Brasil), Polako |
| 6406.20 | Solados de borracha/plástico | Hiper Solados (Brasil) |

## Quem compra isso (perfil de cliente)
Fábricas de calçado (em especial botas de segurança, militares, PVC, couro), curtumes (wet blue/crust), fábricas de solados (PU/TPU/borracha), fábricas de solado PU e de calçado injetado em PU (compram sistema PU 3907.99 + 3909.50 — ex.: Segurindustria, Peru), fabricantes de couro sintético/tecido revestido, fabricantes de marroquinaria/estofados, e distribuidores de insumos para calçado.

## Tarefa
Para os PAÍSES indicados, encontrar empresas que COMPRAM/IMPORTAM essas NCMs, o mais atualizado (2024–2026) e o mais certo possível. Priorize evidência real: registros de importação (Veritrade, Volza, Panjiva, ImportGenius, Datasur, 52wmb, TradeAtlas — páginas gratuitas), notícias, sites oficiais, câmaras setoriais (ex.: CICEG/ANPIC no México, ACICAM na Colômbia, CALTU no Equador, CIC na Argentina), cadastros de empresas. Use a WebSearch e a WebFetch. Não invente empresas, CNPJ/RUC/NIT, sites ou contatos: se não tiver certeza, deixe null. Cada empresa precisa de pelo menos 1 fonte (URL) que a cite.

Já existem na base (NÃO repita estas; você pode reforçar uma delas só se achar evidência NOVA de importação 2024–2026 — nesse caso inclua com o mesmo nome e "atualiza_existente": true):
ver o arquivo a lista de empresas já existentes em prospeccao.json (campo "empresas", chaves "pais" e "empresa") (chaves = país em português maiúsculo).

Meta: 10 a 20 empresas NOVAS por país grande (México, Colômbia, Peru, Brasil, Argentina, Equador), 4 a 10 por país menor. Qualidade > quantidade.

## Fornecedores e período (importante)
Para cada empresa, procure DE QUEM ela compra (nome do exportador/fornecedor nos registros de importação) e preencha "fornecedores_conhecidos" e o campo "fornecedor" de cada evidência. Em toda evidência, preencha "periodo" com a data do registro (dd/mm/aaaa quando houver, ou o intervalo de anos, ex.: "2024-2026"). Registro sem data perde valor: prefira registros datados.

## Saída
Grave UM arquivo JSON (lista) no caminho indicado na sua tarefa, cada item exatamente com estas chaves:
{"empresa": str, "nome_fantasia": str|null, "pais": "MEXICO|COLOMBIA|EQUADOR|PERU|BOLIVIA|CHILE|ARGENTINA|PARAGUAI|URUGUAI|VENEZUELA|GUATEMALA|EL SALVADOR|HONDURAS|NICARAGUA|COSTA RICA|PANAMA|REP DOMINICANA|BRASIL", "cidade": str|null, "id_fiscal": str|null, "site": str|null, "contato": null, "segmento": "calçado de segurança|calçado geral|bota PVC/borracha|curtume|solados|couro sintético/tecido revestido|marroquinaria/estofados|distribuidor de insumos|adesivos/químicos", "produtos": str, "porte": "pequeno|médio|grande"|null, "ncms_provaveis": [códigos da tabela acima, formato "4104.11"], "evidencias": [{"descricao": str, "ncm": str, "origem": str, "fornecedor": str|null, "periodo": str, "valor": str|null, "unidade": str|null, "fonte": url}], "fornecedores_conhecidos": str|null, "por_que_e_prospect": str (1 frase, português), "confianca": "alta|média|baixa", "fontes": [urls], "atualiza_existente": bool}
Confiança: alta = registro de importação da NCM 2024–2026 ou fonte oficial clara; média = fabricante confirmado do segmento, sem registro de importação; baixa = citação fraca/antiga.
Também grave, se encontrar, um resumo de mercado por país no mesmo arquivo? NÃO — só a lista de empresas.
Responda no final só com: quantas empresas por país, e o caminho do arquivo.
