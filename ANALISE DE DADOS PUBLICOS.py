import pandas as pd
import matplotlib.pyplot as plt

arquivo_sjc=pd.read_excel("SP_Sao_Jose_dos_Campos_Geral.xls", sheet_name=8)
arquivo_cac=pd.read_excel("SP_Cacapava_Geral.xls", sheet_name=8)
arquivo_tau=pd.read_excel("SP_Taubate_Geral.xls", sheet_name=8)
valorapro_sjc={'01': '', '02': '', '03': '', '04': '', '05': '', '06': '', '07': '', '08': '','total': '' }
valorapro_cac={'01': '', '02': '', '03': '', '04': '', '05': '', '06': '', '07': '', '08': '','total': '' }
valorapro_tau={'01': '', '02': '', '03': '', '04': '', '05': '', '06': '', '07': '', '08': '','total': '' }
valorapres_sjc={'01': '', '02': '', '03': '', '04': '', '05': '', '06': '', '07': '', '08': '','total': '' }
valorapres_cac={'01': '', '02': '', '03': '', '04': '', '05': '', '06': '', '07': '', '08': '','total': '' }
valorapres_tau={'01': '', '02': '', '03': '', '04': '', '05': '', '06': '', '07': '', '08': '','total': '' }
#dados sjc aprovados
valorapro_sjc['01']=arquivo_sjc['Unnamed: 3'] [5]
valorapro_sjc['02']=arquivo_sjc['Unnamed: 3'] [8]
valorapro_sjc['03']=arquivo_sjc['Unnamed: 3'] [23]
valorapro_sjc['04']=arquivo_sjc['Unnamed: 3'] [34]
valorapro_sjc['05']=arquivo_sjc['Unnamed: 3'] [53]
valorapro_sjc['06']=arquivo_sjc['Unnamed: 3'] [60]
valorapro_sjc['07']=arquivo_sjc['Unnamed: 3'] [65]
valorapro_sjc['08']=arquivo_sjc['Unnamed: 3'] [68]
valorapro_sjc['total']=arquivo_sjc['Unnamed: 3'] [72]
#dados sjc apresentados
valorapres_sjc['01']=arquivo_sjc['Unnamed: 7'] [5]
valorapres_sjc['02']=arquivo_sjc['Unnamed: 7'] [8]
valorapres_sjc['03']=arquivo_sjc['Unnamed: 7'] [23]
valorapres_sjc['04']=arquivo_sjc['Unnamed: 7'] [34]
valorapres_sjc['05']=arquivo_sjc['Unnamed: 7'] [53]
valorapres_sjc['06']=arquivo_sjc['Unnamed: 7'] [60]
valorapres_sjc['07']=arquivo_sjc['Unnamed: 7'] [65]
valorapres_sjc['08']=arquivo_sjc['Unnamed: 7'] [68]
valorapres_sjc['total']=arquivo_sjc['Unnamed: 7'] [72]

#dados caçapava aprovados
valorapro_cac['01']=arquivo_cac['Unnamed: 3'] [5]
valorapro_cac['02']=arquivo_cac['Unnamed: 3'] [8]
valorapro_cac['03']=arquivo_cac['Unnamed: 3'] [23]
valorapro_cac['04']=arquivo_cac['Unnamed: 3'] [34]
valorapro_cac['05']=arquivo_cac['Unnamed: 3'] [53]
valorapro_cac['06']=arquivo_cac['Unnamed: 3'] [60]
valorapro_cac['07']=arquivo_cac['Unnamed: 3'] [65]
valorapro_cac['08']=arquivo_cac['Unnamed: 3'] [68]
valorapro_cac['total']=arquivo_cac['Unnamed: 3'] [72]
#dados caçapava apresentados
valorapres_cac['01']=arquivo_cac['Unnamed: 7'] [5]
valorapres_cac['02']=arquivo_cac['Unnamed: 7'] [8]
valorapres_cac['03']=arquivo_cac['Unnamed: 7'] [23]
valorapres_cac['04']=arquivo_cac['Unnamed: 7'] [34]
valorapres_cac['05']=arquivo_cac['Unnamed: 7'] [53]
valorapres_cac['06']=arquivo_cac['Unnamed: 7'] [60]
valorapres_cac['07']=arquivo_cac['Unnamed: 7'] [65]
valorapres_cac['08']=arquivo_cac['Unnamed: 7'] [68]
valorapres_cac['total']=arquivo_cac['Unnamed: 7'] [72]
#dados taubaté aprovados
valorapro_tau['01']=arquivo_tau['Unnamed: 3'] [5]
valorapro_tau['02']=arquivo_tau['Unnamed: 3'] [8]
valorapro_tau['03']=arquivo_tau['Unnamed: 3'] [23]
valorapro_tau['04']=arquivo_tau['Unnamed: 3'] [34]
valorapro_tau['05']=arquivo_tau['Unnamed: 3'] [53]
valorapro_tau['06']=arquivo_tau['Unnamed: 3'] [60]
valorapro_tau['07']=arquivo_tau['Unnamed: 3'] [65]
valorapro_tau['08']=arquivo_tau['Unnamed: 3'] [68]
valorapro_tau['total']=arquivo_tau['Unnamed: 3'] [72]

#dados taubaté apresentados
valorapres_tau['01']=arquivo_tau['Unnamed: 7'] [5]
valorapres_tau['02']=arquivo_tau['Unnamed: 7'] [8]
valorapres_tau['03']=arquivo_tau['Unnamed: 7'] [23]
valorapres_tau['04']=arquivo_tau['Unnamed: 7'] [34]
valorapres_tau['05']=arquivo_tau['Unnamed: 7'] [53]
valorapres_tau['06']=arquivo_tau['Unnamed: 7'] [60]
valorapres_tau['07']=arquivo_tau['Unnamed: 7'] [65]
valorapres_tau['08']=arquivo_tau['Unnamed: 7'] [68]
valorapres_tau['total']=arquivo_tau['Unnamed: 7'] [72]



#Tabela Taubaté:
df_tau = pd.DataFrame({'pres': [valorapres_tau['01'],valorapres_tau['02'],valorapres_tau['03'],valorapres_tau['04'],valorapres_tau['05'],valorapres_tau['06'],valorapres_tau['07'],valorapres_tau['08']],
                   'pro': [valorapro_tau['01'],valorapro_tau['02'],valorapro_tau['03'],valorapro_tau['04'],valorapro_tau['05'],valorapro_tau['06'],valorapro_tau['07'],valorapro_tau['08']]},index = ['Ações de promoção e \nprevenção em saúde','Procedimentos com \nfinalidade diagnóstica','Procedimentos\n clínicos','Procedimentos \ncirúrgicos','Transplantes de orgãos,\n tecidos e células','Medicamentos','Órteses, próteses e\n materiais especiais','Ações complementares \nda atenção à saúde'])

fig = plt.figure()
ax = fig.add_subplot(111)
ax2 = ax.twinx()
width = 0.3
                      
df_tau.pres.plot(kind='bar', color='purple', ax=ax, width=width, position=1)
df_tau.pro.plot(kind='bar', color='black', ax=ax, width=width, position=0)

ax2.yaxis.set_major_locator(plt.NullLocator())
ax.tick_params(axis='x', rotation=90)


ax.set_ylabel('Valor Apresentado(em dezenas de milhões)')
ax2.set_ylabel('Valor Aprovado(em dezenas de milhões)')


#Tabela Caçapava:
df_cac = pd.DataFrame({'pres': [valorapres_cac['01'],valorapres_cac['02'],valorapres_cac['03'],valorapres_cac['04'],valorapres_cac['05'],valorapres_cac['06'],valorapres_cac['07'],valorapres_cac['08']],
                   'pro': [valorapro_cac['01'],valorapro_cac['02'],valorapro_cac['03'],valorapro_cac['04'],valorapro_cac['05'],valorapro_cac['06'],valorapro_cac['07'],valorapro_cac['08']]}, index = ['Ações de promoção e \nprevenção em saúde','Procedimentos com \nfinalidade diagnóstica','Procedimentos\n clínicos','Procedimentos \ncirúrgicos','Transplantes de orgãos,\n tecidos e células','Medicamentos','Órteses, próteses e\n materiais especiais','Ações complementares \nda atenção à saúde'])

fig = plt.figure()
ax = fig.add_subplot(111)
ax2 = ax.twinx()
width = 0.3
                      
df_cac.pres.plot(kind='bar', color='yellow', ax=ax, width=width, position=1)
df_cac.pro.plot(kind='bar', color='black', ax=ax, width=width, position=0)

ax2.yaxis.set_major_locator(plt.NullLocator())
ax.tick_params(axis='x', rotation=90)

ax.set_ylabel('Valor Apresentado(em milhões)')
ax2.set_ylabel('Valor Aprovado(em milhões)')



#Tabela São José dos Campos:
df_sjc = pd.DataFrame({'pres': [valorapres_sjc['01'],valorapres_sjc['02'],valorapres_sjc['03'],valorapres_sjc['04'],valorapres_sjc['05'],valorapres_sjc['06'],valorapres_sjc['07'],valorapres_sjc['08']],
                  'pro': [valorapro_sjc['01'],valorapro_sjc['02'],valorapro_sjc['03'],valorapro_sjc['04'],valorapro_sjc['05'],valorapro_sjc['06'],valorapro_sjc['07'],valorapro_sjc['08']]}, index = ['Ações de promoção e \nprevenção em saúde','Procedimentos com \nfinalidade diagnóstica','Procedimentos\n clínicos','Procedimentos \ncirúrgicos','Transplantes de orgãos,\n tecidos e células','Medicamentos','Órteses, próteses e\n materiais especiais','Ações complementares \nda atenção à saúde'])

fig = plt.figure()
ax = fig.add_subplot(111)
ax2 = ax.twinx()
width = 0.3
                      
df_sjc.pres.plot(kind='bar', color='gray', ax=ax, width=width, position=1)
df_sjc.pro.plot(kind='bar', color='black', ax=ax, width=width, position=0)

ax2.yaxis.set_major_locator(plt.NullLocator())
ax.tick_params(axis='x', rotation=90)


ax.set_ylabel('Valor Apresentado(em dezenas de milhões)')
ax2.set_ylabel('Valor Aprovado(em dezenas de milhões)')

#Tabela de Comparação de valores apresentados:
fig = plt.figure()
ax = fig.add_subplot(111)
ax2 = ax.twinx()
width = 0.3
                      
df_tau.pres.plot(kind='bar', color='purple', ax=ax, width=width, position=1.5)
df_sjc.pres.plot(kind='bar', color='gray', ax=ax, width=width, position=-0.5)
df_cac.pres.plot(kind='bar', color='Yellow', ax=ax, width=width, position=0.5)

ax2.yaxis.set_major_locator(plt.NullLocator())
ax.tick_params(axis='x', rotation=90)

ax.set_ylabel('Valor Apresentado(em dezenas de milhões)')

#Tabela de Comparação de valores aprovados:
fig = plt.figure()
ax = fig.add_subplot(111)
ax2 = ax.twinx()
width = 0.3
                      
df_tau.pro.plot(kind='bar', color='purple', ax=ax, width=width, position=1.5)
df_sjc.pro.plot(kind='bar', color='gray', ax=ax, width=width, position=-0.5)
df_cac.pro.plot(kind='bar', color='Yellow', ax=ax, width=width, position=0.5)

ax2.yaxis.set_major_locator(plt.NullLocator())
ax.tick_params(axis='x', rotation=90)

ax.set_ylabel('Valor Aprovado(em dezenas de milhões)')

#Tabela total:
df_total = pd.DataFrame({'Taubaté': [valorapres_tau['total'],valorapro_tau['total']],
                   'Caçapava': [valorapres_cac['total'],valorapro_cac['total']],
                   'sjc': [valorapres_sjc['total'],valorapres_sjc['total']]}, index = ['Valor Apresentado','Valor Aprovado'])

fig = plt.figure()
ax = fig.add_subplot(111)
ax2 = ax.twinx()
width = 0.3
                      
df_total.sjc.plot(kind='bar', color='gray', ax=ax, width=width, position=-0.5)
df_total.Taubaté.plot(kind='bar', color='purple', ax=ax, width=width, position=1.5)
df_total.Caçapava.plot(kind='bar', color='yellow', ax=ax, width=width, position=0.5)

plt.gca().xaxis.set_major_locator(plt.NullLocator())
ax2.yaxis.set_major_locator(plt.NullLocator())
ax.tick_params(axis='x', rotation=90)

ax.set_ylabel('Valor Apresentado(em dezenas de milhões)')
ax2.set_ylabel('Valor Aprovado(em dezenas de milhões)')


plt.show()
