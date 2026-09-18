# OWNER-INPUTS — sarasotaflooringcompany.com

Atualizado em 2026-09-18. Tudo aqui depende de informação ou ação do proprietário. O site já está no ar sem estes itens; cada um deles aumenta ranking, citação por IA ou conversão.

## 1. Prioridade máxima — entidade e avaliações (é aqui que o topo da SERP é decidido)

A auditoria de concorrentes mostrou que o topo de "flooring sarasota" é fraco em on-page (um deles tem H1 "EXQUISITE" e nenhum schema) e é sustentado por **Google Business Profile, avaliações e citações**. On-page nós já ganhamos; falta isto:

| Item | Por quê | Ação |
|---|---|---|
| Google Business Profile real e verificado | Fonte nº 1 do Google AI Overviews/AI Mode e do Local Pack. O link `g.page/sarasota-flooring-co` que estava no site **não existia** (redirecionava para uma busca) e foi removido de 187 lugares. | Criar/verificar o perfil como *service-area business* (sem endereço público), categoria primária "Flooring contractor"; secundárias "Tile contractor", "Wood floor installation service" e "Wood floor refinishing service" (não usar "Flooring store": não há showroom). Depois colocar a URL em `src/data_core.py` → `BUSINESS["gbp"]`. |
| Yelp, Houzz, Angi, Thumbtack, BBB, HomeAdvisor, BestPickReports, Nextdoor, Bing Places, Apple Business Connect | "best flooring company sarasota" é 100% diretórios; o ChatGPT cita Yelp em ~80% das respostas locais. | Cadastrar com NAP idêntico: **Sarasota Flooring Company · (941) 241-3724 · Lakewood Ranch, FL 34212**. Colocar cada URL em `BUSINESS` (`yelp`, `houzz`, `angi`, `thumbtack`, `bbb`, `facebook`, `instagram`) — o schema `sameAs` e uma futura página `/directories/` se montam sozinhos. |
| Avaliações reais | As 12 avaliações que estavam no site eram **placeholders inventados** (o próprio README dizia isso) com `AggregateRating 5.0/12` em 117 páginas. Isso viola a política de review snippets do Google (risco de ação manual) e a regra da FTC de 2024 sobre reviews falsas. **Foram removidas.** | Quando houver avaliações reais no GBP: preencher `REVIEWS` em `data_core.py` com texto, nome, data e URL da fonte. O rating só volta ao schema se for do perfil da mesma entidade. |

## 2. Verdade legal

| Item | Situação no site | O que preciso |
|---|---|---|
| Entidade "Sarasota Flooring Company LLC" | Usada no rodapé e no schema `legalName`. | Confirmar que a LLC existe na Sunbiz (ou qual entidade fatura). Se não existir, registrar a LLC ou um nome fictício (DBA). |
| Licença | A Flórida não tem licença estadual para instalador de piso, e o licenciamento local foi preemptado em 01/07/2024. O site **não diz "licensed"** em lugar nenhum. | Nada a fazer, a não ser que exista alguma licença real para divulgar. |
| Seguro | O site só diz "ask us for our certificate of insurance". | Confirmar que há apólice de general liability ativa (seguradora + limites). Se não houver, me avise para eu tirar a frase. |
| Garantia de 2 anos por escrito | Prometida em todo o site e detalhada em `/warranty/`. | Confirmar que é isso mesmo que a empresa entrega e que existe o documento. |
| "Owner supervises every install, no subcontracted crews" | Prometido em todo o site. | Confirmar. Se houver subcontratação, eu ajusto o texto. |
| Endereço "8125 Lakewood Main Street, Suite 207" (virtual office) | **Tirei a rua** do site e do schema; ficou só "Lakewood Ranch, FL 34212 · by appointment". Escritório virtual viola as diretrizes do GBP. | Se o endereço for real e com atendimento, me diga e eu recoloco. |
| Tabela de preços | Mantive as faixas que já estavam no site (2026). Todas as calculadoras, guias de custo e posts usam exatamente essas faixas. | Revisar `SERVICES[...]["pricing_rows"]` em `data_core.py`. Se mudar lá, rodar o build e tudo se atualiza (exceto os exemplos resolvidos dentro dos textos dos guias de custo). |

## 3. Leads: formulário, telefone, e-mail

- **Formulário**: todos os formulários do site postam no Web3Forms (chave `348354a8-…b255`) e redirecionam para `/thanks/`. Cada lead chega com o campo `page` dizendo de qual página veio. Teste real enviado em 2026-09-18 (assunto "TESTE … pode ignorar") — **confirme que chegou na caixa cadastrada no Web3Forms**.
- **opera-portal**: outra sessão (2026-09-18 10:06) tinha ligado os formulários no `opera-portal /api/lead` com `brand=sarasota-flooring`, mas a marca ainda não existe no portal (o endpoint recusaria os leads). Por instrução sua, ficou Web3Forms. O trabalho da outra sessão está guardado em `git stash` (`stash@{0}`). Se quiser os leads **também** no portal: criar a marca no portal primeiro; depois eu ligo um segundo envio (ou troco o destino) em 5 minutos.
- **E-mail**: `hello@sarasotaflooringcompany.com` e qualquer outro endereço do domínio (catch-all) encaminham para **opusdigitalmarketingflorida@gmail.com** via Cloudflare Email Routing (MX/SPF/DKIM publicados em 2026-09-18). Mande um e-mail de teste para hello@ para confirmar.
- **Telefone (941) 241-3724**: segundo a nota da outra sessão, hoje é só um twimlet forward para +1 689 242-7487. Reapontar para o portal (voice/status/sms) depende da marca existir lá.

## 4. Fotos e prova real

O site inteiro tem **8 fotos**. É a maior fraqueza de conteúdo que sobrou.
- 20–30 fotos reais de obras (antes/depois, slab preparado, medição de umidade, escadas, banheiros), de preferência com cidade e tipo de piso.
- 5–10 projetos documentados (cidade, m²/sq ft, material, desafio, prazo, faixa de preço) → viram a seção `/projects/`, que é o que diferencia de franquias com páginas clonadas.
- Vídeos curtos (teste de umidade, nivelamento, instalação) com transcrição.

## 5. Ferramentas de busca (15 minutos, só o dono consegue)

1. **Google Search Console**: o domínio já tem o TXT `google-site-verification` no DNS — entrar na propriedade e enviar `https://sarasotaflooringcompany.com/sitemap.xml`. Pedir indexação da home e das 6 landings novas.
2. **Bing Webmaster Tools**: importar do GSC, enviar sitemap. ChatGPT Search e Copilot usam o índice do Bing. IndexNow já está com chave publicada (`/8a350006d4c298f2bdc1c5260446e4fa.txt`) e eu já notifiquei as URLs.
3. **Cloudflare → Security → Bots**: conferir que "Block AI bots" está **desligado** para esta zona (o robots.txt libera OAI-SearchBot, PerplexityBot, ClaudeBot etc., mas o WAF do Cloudflare pode bloquear antes).
4. Google Analytics 4 / Cloudflare Web Analytics: o site não tem nenhum. Me passe o ID do GA4 (`G-…`) ou ative o Web Analytics no painel do Pages.

## 6. Rede de sites irmãos (canibalização)

- `triangle-floor.com` e `napasflooring.com` usam a mesma arquitetura de URLs e miram Sarasota, Venice e Lakewood Ranch; `bradentonflooring.com` mira Bradenton. Medi sobreposição de texto: **0% com bradentonflooring, triangleflooring e bvaflooring; ~8% com napasflooring em 40 páginas antigas** (todas reescritas nesta versão).
- Decisão aplicada neste site: nenhum link entre os sites da rede (tirei os 3 links de "partner sites" do rodapé — 372 links externos sitewide), nenhuma frase compartilhada, e estrutura de página diferente (cápsulas de resposta, guias de custo consolidados, páginas de condomínio/remoção/nivelamento que os irmãos não têm).
- Recomendação: para **Bradenton**, deixar `bradentonflooring.com` como dono da intenção "flooring bradenton" e manter aqui só a página de cidade + serviço×cidade com conteúdo local próprio (já é assim). Reavaliar em 90 dias com dados do Search Console.
