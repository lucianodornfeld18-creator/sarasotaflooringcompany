# Auditoria SEO / GEO / AEO — sarasotaflooringcompany.com

Data: 2026-09-18 · Método: o mesmo roteiro do prompt `08-PROMPT-KISSIMMEE-CONCRETE.md`, adaptado para flooring. Toda medida abaixo foi tirada por script (`src/audit_site.py`, `src/qa_content.py`, `src/kw_report.py`, validador de links do `src/build.py`) sobre o site antigo (commit `1bdc88e`) e sobre o site novo (`dist/`). Arquivos de evidência: `docs/audit-before.json`, `docs/audit-after.json`, `docs/keyword-coverage.md`, `docs/link-report.json`, `docs/content-qa.json`, `docs/research-keywords-and-serp.md`, `docs/research-questions.md`.

## 1. Resumo

```text
Domain:               sarasotaflooringcompany.com
Build date:           2026-09-18
Indexable URLs:       176  (antes: 122)
Palavras no site:     244.117  (antes: 218.515 — mas 82% delas eram texto repetido)
Texto único por página (média, sem template):  85%   (antes: 18%)
Links internos quebrados: 0 · páginas órfãs: 0 · titles/H1/descriptions duplicados: 0
Keywords pesquisadas presentes no site: 147 de 151 (as 4 restantes ficaram de fora de propósito)
Perguntas respondidas em post próprio: 73 posts cobrindo 79 perguntas (pedido: 50)
Raio coberto: 21 comunidades em 40 milhas (antes: 8)
Sobreposição de texto com bradentonflooring.com: 0%
Deployment status:    DEPLOYED (ver seção 9)
```

## 2. O que a auditoria encontrou no site antigo (por gravidade)

| # | Achado | Evidência | O que foi feito |
|---|---|---|---|
| 1 | **Formulário não entregava leads.** Os 2 formulários faziam `POST /thanks/` num site estático. | `curl -X POST …/thanks/` → HTTP 405; nenhum JS nem serviço de formulário no HTML. | Todos os formulários postam no Web3Forms, com honeypot, campo `page` (de qual página veio o lead) e redirect para `/thanks/`. Formulário em **todas** as páginas de conteúdo. Envio de teste real aceito pela API. |
| 2 | **Avaliações e nota inventadas.** 12 depoimentos placeholder (o README do projeto dizia isso) + `AggregateRating 5.0 / 12` em 117 páginas + link `g.page/sarasota-flooring-co` que não existe (cai numa busca do Google), repetido 187 vezes. | `_data.py` (`REVIEWS`, `rating`, `review_count`), `audit-before.json` → `external_domains`. | Removidos. Viola a política de review snippets do Google (risco de ação manual) e a regra da FTC de 2024. O componente continua pronto para avaliações reais (ver OWNER-INPUTS). |
| 3 | **Páginas-doorway.** As 48 páginas serviço×cidade eram o mesmo texto com o nome da cidade trocado: 3.800 pares de páginas com mais de 15% de texto idêntico, até **83,6%** entre duas cidades; em média só **18%** do texto de cada página era exclusivo dela. Os 48 posts "custo por cidade" tinham o mesmo problema. | `audit-before.json` → `internal_dup_top`, `uniq_share_mean`. | As 48 páginas foram reescritas "local primeiro" (bairros reais, época das casas, zona de inundação, regra de condomínio, jurisdição de permit), sem repetir a descrição genérica do serviço. Depois, descontado o template: **nenhum par serviço×cidade acima de 15%** (máx. 11%; mesmo serviço em duas cidades: 4,5% em média, contra 66% antes); unicidade média por página 85%. Os 48 posts de custo por cidade viraram 6 guias de custo com tabela por cidade (301 dos URLs antigos). |
| 4 | **Rede de links no rodapé.** 3 links "partner sites" (brazacleaning, ocoeeconcrete, thevillagesremodeling) em todas as 124 páginas = 372 links externos sitewide, footprint clássico de rede. | `audit-before.json` → `external_domains`. | Removidos. Links externos agora são só fontes citadas (NWFA, TCNA, FEMA, NOAA, Angi, HomeGuide…). |
| 5 | **Código-fonte público.** `_data.py`, `_gen.py`, `README.md` etc. respondiam 200 em produção, porque o Pages servia a raiz do repositório. | `curl https://sarasotaflooringcompany.com/_data.py` → 200. | Fontes em `src/`, site gerado em `dist/`; o Pages passa a servir só `dist/`. |
| 6 | **Build quebrado fora do sandbox original.** Caminho de saída fixo `/home/claude/sarasota-flooring` em 7 lugares — no Windows escrevia em `C:\home\claude\…`. Por isso ninguém regenerava o site desde maio. | `grep home/claude _*.py`. | Build único `python src/build.py`, caminhos relativos, reproduzível. |
| 7 | **Cobertura de busca com buracos.** "near me": 0 ocorrências. North Port, Englewood, Osprey, Nokomis, Ellenton, Port Charlotte: 0 menções. Sem páginas para refinishing, remoção de tile, waterproof, engineered hardwood, condomínios, nivelamento — todas com demanda comprovada na pesquisa. | `audit-before.json` → `keywords`; `research-keywords-and-serp.md` §1.1 e §5. | 13 cidades novas, 6 landings novas, 73 posts, hub de custos. "near me": 44 ocorrências naturais em 40 páginas. |
| 8 | On-page da home. Title com 102 caracteres; H1 renderizava "inSarasota" (sem espaço); description com 191. | `audit-before.json` → `title_too_long`, `desc_bad`. | Title 56 caracteres, H1 novo, description dentro do limite; home passou de 1.756 para 5.141 palavras. |
| 9 | Só **7 imagens** no site inteiro, JPG de 200–400 KB, sem responsivo. | `audit-before.json` → `images`. | Pipeline WebP em 480/960/1600 px com `srcset`, `width/height`, lazy-load fora do LCP. Continua sendo o ponto fraco: só há 8 fotos reais (ver OWNER-INPUTS). |
| 10 | Claims sem prova: "the longest warranty in the Sarasota market", microclima "5–8% mais úmido", endereço de escritório virtual no schema, licença = "Business Tax Receipt". | `_data.py`. | Superlativo removido; endereço reduzido a cidade/UF/ZIP; o site nunca diz "licensed" (a Flórida não licencia instalador de piso; licenciamento local preemptado em 01/07/2024 — explicado num post com fonte). |
| 11 | Overflow horizontal no celular (botão do header cortado). | Screenshot 390 px do site antigo. | Header novo; 63 combinações página×viewport testadas sem overflow. |
| 12 | Sem `llms.txt`, sem feed, robots sem política para bots de IA, sem analytics. | — | `llms.txt` (47 KB), `llms-full.txt` (298 KB, todas as respostas), `feed.xml`, robots liberando Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Applebot etc. Analytics depende do dono (OWNER-INPUTS §5). |

O que já estava certo e foi mantido: canonical em todas as páginas, 1 H1 por página, zero links quebrados, JSON-LD válido, IndexNow com chave publicada, redirects de atalhos.

## 3. Antes × depois (medido)

| Métrica | Antes | Depois |
|---|---|---|
| Páginas HTML | 124 | 178 (176 indexáveis) |
| Texto único por página (média, 8-grams, sem template) | 18,1% | **85,2%** |
| Serviço×cidade, texto igual entre pares (8-grams, bruto, inclui blocos de template) | 1.128 de 1.128 pares >15% · média 51% · máx. 83,6% | média 16,8% · máx. 24,6% (o que sobra é o bloco fixo de formulário/CTA/lateral) |
| Serviço×cidade, texto igual **sem o template** | 288 pares >15% · mesmo serviço em cidades diferentes: média **66%**, máx. 72% | **0 pares >15%** · mesmo serviço: média **4,5%**, máx. 7,6% |
| Home (palavras) | 1.756 | 5.141 |
| Página de serviço (média) | 2.144 | 2.997 |
| Serviço×cidade (média) | 2.161 (83% repetido) | 1.075 (local) |
| Posts | 51 (48 clones por cidade) | 73 (uma pergunta por URL) |
| Cidades com página | 8 | 21 |
| Landings comerciais além dos 6 serviços | 0 | 6 |
| Ferramentas interativas | 0 | 3 |
| Titles > 65 caracteres | 5 | 0 |
| Descriptions fora de 110–165 | 7 | 0 (só 404 e thanks, noindex) |
| Titles / H1 / descriptions duplicados | 6 / 6 / 0 | 0 / 0 / 0 |
| Links internos quebrados / órfãs | 0 / 0 | 0 / 0 |
| Links externos sitewide para a rede | 372 | 0 |
| Schema `AggregateRating` sem avaliações reais | 117 páginas | 0 |
| JSON-LD | LocalBusiness, FAQ, Article, Breadcrumb | + WebSite, Service (59), WebApplication (3), FAQPage em 159 páginas |
| Imagens (tags `<img>`) | 7 | 414 (WebP responsivo) |
| Maior HTML | 76 KB | 111 KB (FAQ hub) — limite do roteiro: 150 KB |
| "near me" | 0 | 44 em 40 páginas |
| Sobreposição com bradentonflooring / triangle / bva | 0 / 0 / 0 | 0 / 0 / 0 |
| Sobreposição com napasflooring | 40 páginas >5% (média 7,7%) | 1 página (contato: lista de horários) |

## 4. Interlinks

Regra aplicada (mesma do roteiro de Kissimmee): home → serviços, landings, cidades por tier, ferramentas, custos, posts; serviço → suas 8 páginas serviço×cidade + guia de custo + posts relacionados; cidade → 6 serviços (serviço×cidade nas 8 cidades-núcleo) + cidades vizinhas + posts locais; serviço×cidade → serviço-pai + cidade + outras cidades do mesmo serviço + outros serviços da mesma cidade; post → próximo passo comercial + 3–5 posts relacionados + páginas locais; FAQ hub → todos os posts; `/areas/` → todas as cidades com distância e tempo.

- Validador no build: todo `href` interno precisa resolver para uma página gerada, um arquivo estático ou uma regra de redirect. Resultado: **0 quebrados, 0 órfãs** (`docs/link-report.json`, que também lista as 15 páginas com menos links de entrada).
- Perguntas fundidas (6 casos em que duas perguntas eram a mesma) têm o slug antigo mapeado para o post que absorveu a resposta (`src/content/merged_slugs.json`), então nenhum link cruzado quebrou.
- Âncoras: variadas e descritivas por regra do briefing; nenhuma âncora exata repetida em bloco.
- FAQ de página comercial que repete uma pergunta que tem post próprio: mantém a resposta curta e aponta para o post ("Read the full answer"), para que **uma pergunta tenha um único URL dono**.

## 5. Keywords

Pesquisa: 151 keywords com evidência (autocomplete em 136 sementes, composição da SERP, CPC publicado quando existe) — não existe volume público no nível de Sarasota; os rótulos HIGH/MEDIUM/LOW dizem qual foi a evidência (`docs/research-keywords-and-serp.md`). Cada keyword tem uma página dona.

Cobertura no site gerado (`docs/keyword-coverage.md`): **147 de 151 presentes**, 97 delas em 5 ou mais páginas. As 4 ausentes ficaram de fora de propósito: `flooring st petersburg fl` e `flooring punta gorda` (fora do raio de 40 milhas), `top rated flooring companies near me` e `licensed and insured flooring contractors` (seriam claims sem prova).

As que mais importam e onde moram: `flooring company sarasota` / `flooring installation sarasota` / `flooring contractors sarasota` → home; `vinyl plank flooring sarasota`, `hardwood flooring sarasota`, `tile installation sarasota`… → páginas de serviço; `hardwood floor refinishing sarasota`, `tile removal sarasota`, `waterproof flooring sarasota`, `engineered hardwood flooring sarasota`, `condo flooring sarasota`, `subfloor leveling` → 6 landings novas; `flooring <cidade> fl` → 21 páginas de cidade; consultas de custo com quantidade ("1000 sq ft", "per square foot", "labor cost") → hub `/cost/` + 6 guias com exemplos resolvidos; "best flooring for …" e "X vs Y" → posts com tabela e veredito na primeira frase.

Sem stuffing: máximo ~1 "near me" exato a cada 250 palavras, sempre em frase natural ("If you searched for flooring installers near me from Palmer Ranch…").

## 6. GEO / AEO (aparecer nas respostas de IA)

O que a evidência de 2026 mostra que funciona, e o que foi implementado:

1. **Cápsulas de resposta**: toda página abre com 40–70 palavras autossuficientes, com número, unidade, ano e escopo geográfico. É o trecho que AI Overviews, ChatGPT e Perplexity extraem. 176 páginas têm cápsula; posts e landings também usam H2 em forma de pergunta.
2. **Números explícitos**: a pesquisa mostrou que os resumos gerados por IA citavam literalmente as páginas que tinham faixas de preço. Todas as faixas do site vêm de uma tabela única (2026) e os exemplos resolvidos foram recalculados por script.
3. **Tabelas em HTML puro** (preço por m², comparações, tolerâncias) — sem abas nem conteúdo carregado por JS. As 3 primeiras respostas de cada FAQ ficam abertas por padrão.
4. **Fontes primárias linkadas**: NWFA, TCNA, ASTM F2170/F1869, FEMA TB 2, Florida Building Code, NOAA, páginas de condado, Angi/HomeGuide/This Old House com data. Onde a pesquisa não achou fonte, o número foi omitido (lista em `docs/research-questions.md`).
5. **Entidade consistente**: mesmo nome, telefone e área em todas as páginas, no schema e no `llms.txt`. `sameAs` se preenche sozinho quando os perfis reais existirem.
6. **`/llms.txt` e `/llms-full.txt`**: resumo da entidade + todas as respostas em texto plano.
7. **Bots de busca e de IA liberados** no robots.txt (conferir o "Block AI bots" do Cloudflare — OWNER-INPUTS §5).
8. **Bing primeiro**: IndexNow notificado com todas as URLs (ChatGPT Search e Copilot usam o índice do Bing).
9. **Frescor**: "Last reviewed" visível, `dateModified` real no schema, sitemap com `lastmod` real.
10. Autor: os artigos são assinados pela equipe editorial da empresa (Organization), com página pública de método (`/editorial-standards/`) que inclui a divulgação de uso de IA na redação. Não inventei pessoa, credencial nem foto.

Inovações que os concorrentes auditados não têm: calculadora de custo com remoção, nivelamento e rodapé em linhas separadas; "Florida Flooring Finder" (7 perguntas sobre laje, inundação, casa fechada no verão, condomínio, pets, aluguel, orçamento → 2 pisos recomendados com o porquê); checklist de aprovação de piso em condomínio (13 itens, imprimível); página de condomínio com IIC/STC e passo a passo de aprovação; páginas de remoção de tile com controle de pó e de nivelamento de laje; guias de custo com aritmética visível.

## 7. Território — raio de 40 milhas (medido a partir do centro de Sarasota)

- **0–15 mi**: Sarasota, Siesta Key, Lakewood Ranch, Longboat Key, Osprey, Bradenton, Palmetto, Ellenton
- **15–30 mi**: Nokomis, Anna Maria Island, Venice, Parrish, Myakka City, Wellen Park, North Port, Ruskin, Englewood, Sun City Center
- **30–40 mi**: Apollo Beach, Port Charlotte, Riverview
- **Fora (não reivindicado)**: Punta Gorda (41), Arcadia (42), Tampa (43), St. Petersburg (31 em linha reta, mas do outro lado da baía).

Cada página de cidade tem ZIPs e bairros verificados por busca, fatos locais com fonte e texto que não sobrevive à troca do nome da cidade (ex.: Venice Island fora das zonas de inundação; Longboat Key com departamento de obras próprio; North Port e a enchente do Ian; terrazzo sob carpete em Gulf Gate). Serviço×cidade só nas 8 cidades-núcleo (URLs que já existiam); as outras 13 ganham página de cidade forte em vez de 78 páginas finas.

## 8. Rede de sites irmãos

Medido por 8-grams contra as pastas locais: bradentonflooring 0%, triangleflooring 0%, bvaflooring 0%, napasflooring 1 página (contato). Fingerprints evitados: sem "63-Point", sem "Why choose us", sem posts `<serviço>-cost-<cidade>`, sem links entre domínios, paleta/tipografia/estrutura próprias. `triangle-floor.com` e `napasflooring.com` disputam as mesmas SERPs de Sarasota/Venice/Lakewood Ranch — podem competir, mas nenhuma frase é compartilhada. Recomendação para Bradenton em OWNER-INPUTS §6.

## 9. Publicação

- Repositório: fontes em `src/`, estáticos em `static/`, site em `dist/`, documentação em `docs/`.
- Cloudflare Pages: diretório de saída alterado para `dist` (o código-fonte deixa de ser servido); deploy automático a cada push em `main`.
- Redirects 301: os 48 posts antigos de custo por cidade → guia de custo do serviço; 3 posts editoriais antigos → equivalentes novos; atalhos antigos mantidos. Todas as demais URLs antigas continuam existindo no mesmo endereço.
- E-mail: `hello@` e catch-all → opusdigitalmarketingflorida@gmail.com (Cloudflare Email Routing, MX/SPF/DKIM publicados).
- IndexNow: todas as URLs do sitemap enviadas.

## 10. Revisão da auditoria (segunda passada)

Depois da primeira rodada, reauditei o site gerado e corrigi o que sobrou: 8 deslizes de QA (4 titles acima de 60, 2 palavras da lista proibida, 2 cápsulas longas), 21 frases repetidas entre páginas de cidade e guias de custo (todas reescritas com o nome da cidade — resultado final: **0 frases compartilhadas entre arquivos de conteúdo**), tabela duplicada em posts (o redator mandou a mesma tabela em dois campos), FAQs do índice de custos que não renderizavam, 3 descriptions que estouraram o limite depois dos patches, e 16 keywords sem cobertura (cobertas com FAQs na página dona). Pendências reais que não dependem de mim estão em `OWNER-INPUTS.md`.

### Limites honestos desta auditoria
- Não há dado de Search Console nem de Ahrefs/Similarweb (conectores sem autorização nesta sessão): não medi posições, impressões nem backlinks. A pesquisa de SERP foi feita por busca real em 2026-09-18, sem Local Pack nem anúncios visíveis.
- Não rodei Lighthouse; performance foi tratada por construção (CSS inline, WebP responsivo, JS mínimo, HTML ≤ 111 KB).
- O conteúdo foi redigido com IA a partir de pesquisa com fontes e validado por script; um instalador de verdade deveria ler as 6 páginas de serviço e os guias de custo para confirmar que os preços e o processo batem com a operação real.
- Posição no Google e citação por IA não podem ser prometidas; o que está garantido é que cada controle sob nosso domínio foi executado e medido.
