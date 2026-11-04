"""Junta pesquisas novas (pesquisa/novos/*.json, mesmo formato do BRIEF.md) ao prospeccao.json.
Uso: python3 -I pesquisa/atualizar.py   (rodar na raiz do repositório)
- empresa nova (país + nome) entra com "novo": true (o "novo" da rodada anterior é limpo)
- empresa que já existe: soma evidências/fontes/NCMs, sobe confiança para "alta" se a nova for alta, preenche campos vazios
- descarta entradas sem fonte"""
import json, glob, re, os, datetime, collections
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
arq = os.path.join(RAIZ, 'prospeccao.json')
d = json.load(open(arq, encoding='utf-8'))
def norm(x): return re.sub(r'\s+',' ',re.sub(r'[^A-Z0-9 ]',' ',str(x or '').upper())).strip()
emp = d['empresas']
for e in emp: e.pop('novo', None); e.pop('atualizado', None)
idx = {(e['pais'], norm(e['empresa'])): i for i, e in enumerate(emp)}
novas = reforcadas = 0
for f in sorted(glob.glob(os.path.join(RAIZ, 'pesquisa', 'novos', '*.json'))):
    for e in json.load(open(f, encoding='utf-8')):
        fontes = e.get('fontes') or [v.get('fonte') for v in e.get('evidencias') or [] if v.get('fonte')]
        if not e.get('empresa') or not e.get('pais') or not fontes: continue
        e['pais'] = e['pais'].upper().strip(); e.pop('atualiza_existente', None)
        k = (e['pais'], norm(e['empresa']))
        if k in idx:
            a = emp[idx[k]]
            for campo in ('evidencias', 'fontes'):
                L = a.get(campo) or []
                for v in e.get(campo) or []:
                    if v not in L: L.append(v)
                a[campo] = L
            a['ncms_provaveis'] = sorted(set((a.get('ncms_provaveis') or []) + (e.get('ncms_provaveis') or [])))
            if e.get('confianca') == 'alta': a['confianca'] = 'alta'
            for c in ('cidade','id_fiscal','site','porte','produtos','por_que_e_prospect','fornecedores_conhecidos','nome_fantasia'):
                if not a.get(c) and e.get(c): a[c] = e[c]
            a['atualizado'] = True; reforcadas += 1
        else:
            e['novo'] = True; idx[k] = len(emp); emp.append(e); novas += 1
hoje = datetime.date.today()
d['atualizadoEm'] = hoje.isoformat()
d['coleta'] = hoje.strftime('%m/%Y')
json.dump(d, open(arq, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('novas', novas, 'reforçadas', reforcadas, 'total', len(emp))
print(collections.Counter(e['pais'] for e in emp).most_common())
