## Aula 07: Mais exploração de dados com `pandas` e `seaborn`

Nesta aula vamos continuar explorando dados utilizando o módulo `pandas`. Também 
vamos fazer algumas operações com os dados e introduzir o módulo `seaborn` para 
análises gráficas.


## **1. ``Dataframe``** BRICS

Salvando ``dataframes`` em arquivos (`.csv` ou `.xlsx`)

```python
df.to_excel("tabela_brics.xlsx")
```

| codigo | pais          | capital    | area    | populacao |
| ------ | ------------- | ---------- | ------- | --------- |
| BR     | Brasil        | Brasília   | 8516.0  | 213.4     |
| RU     | Rússia        | Moscou     | 17100.0 | 143.5     |
| IN     | Índia         | Nova Dehli | 3286.0  | 1408.0    |
| CH     | China         | Beijing    | 9597.0  | 1412.0    |
| SA     | África do Sul | Pretoria   | 1221.0  | 59.3      |


## 1.1. Selecionando Dados

- `nome da coluna` e.g. "capital"
- `índice da coluna` e.g. 1
- `.loc()` e.g. `.loc["BR"]`
- `.iloc()` e.g. `.iloc[0]`


## 1.2. Operações Matemáticas

- `soma`
- `subtração`
- `multiplicação`
- `divisão`

## 1.3. Operações de aggregação:
  - `.count()`
  - `.min()`
  - `.max()`
  - `.sum()`

## **1.3.1. Operações Lógicas**
- Comparações & Verificações:
  - ``==`` e ``!=``
  - ``<`` e `>`
  - ``<=`` e `>=`
  - `.isin()`
- `pandas.query`

------------

## 2. **Banco Mundial do Desenvolvimento**

O Banco Mundial é o maior banco de desenvolvimento do mundo e possui 
o status de observador no Grupo de Desenvolvimento das Nações Unidas.

- [WDI - Data Bank](https://databank.worldbank.org/home)
- [WDI - Planilha](https://databank.worldbank.org/data/download/WDI_excel.zip)


```python
def download_wdi():
  url = (
    'https://databank.worldbank.org/data/download/WDI_excel.zip'
  )
  r = requests.get(url)

  zip = zipfile.ZipFile(BytesIO(r.content))
  zip.extractall("./")
  zip.close()
```

A planilha está possui mais de 380 mil registros para mais de 260 
países ou regiões e mais de 1400 indicadores desde 1960 até 2020. 
Nem todos os países publicam todos os indicadores ao longo de todos
os anos. Cada registro (linha) na planilha refere a um indicador e país 
específicos ao longo do tempo.

| Country Name  | Country Code | Indicator Code    | 1960       | 1961       | 1962       | 1963       | 1964       | ... | 2019        | 2020        | 2021        |
| ------------- | ------------ | ----------------- | ---------- | ---------- | ---------- | ---------- | ---------- | --- | ----------- | ----------- | ----------- |
| Brazil        | BRA          | SP.POP.TOTL.MA.IN | 36,658,093 | 37,763,189 | 38,880,853 | 40,022,356 | 41,178,982 | ... | 104,119,798 | 104,779,288 | 105,291,292 |
| Netherlands   | NLD          | SP.POP.TOTL.MA.IN | 5,722,531  | 5,799,701  | 5,884,270  | 5,965,492  | 6,047,391  | ... | 8,615,129   | 8,665,375   | 8,712,076   |
| New Caledonia | NCL          | SP.POP.TOTL.MA.IN | 41,916     | 43,092     | 44,260     | 45,461     | 46,673     | ... | 135,376     | 135,133     | 134,914     |
| New Zealand   | NZL          | SP.POP.TOTL.MA.IN | 1,191,787  | 1,215,886  | 1,246,966  | 1,271,025  | 1,297,055  | ... | 2,461,701   | 2,522,257   | 2,538,828   |

## 2.1. **Selecionando BRICS e Indicadores**

- **Países**:
  - Brasil
  - Rússia
  - Índia
  - China
  - África do Sul

- **Indicadores**:
  - Renda anual ajustada per capita `NY.ADJ.NNTY.PC.CD`
  - Percentual de área ocupada para agricultura `AG.LND.AGRI.ZS`
  - Taxa de natalidade a cada 1000 habitantes `SP.DYN.CBRT.IN`
  - Gasto público em educação em relação ao PIB `SE.XPD.TOTL.GD.ZS`

- [`pandas.melt`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html)

## 2.3. **Plotting com `seaborn` e `matplotlib`**

- [``seaborn.lineplot()``](https://seaborn.pydata.org/generated/seaborn.lineplot.html)
- [``seaborn.scatterplot()``](https://seaborn.pydata.org/generated/seaborn.scatterplot.html)

- [`pandas.melt`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html)