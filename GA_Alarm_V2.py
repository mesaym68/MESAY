import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_alarm = pd.read_excel("C:/Users/mm598h/Documents/Daily Alarms/GA_Alarm_04062022.xlsx")
df_alarm.rename(columns = {'NodeName':'NodeId'}, inplace = True)
df_disabled = pd.read_excel("C:/Users/mm598h/Documents/Daily Alarms/GA_DiasbledCells_04062022.xlsx")
df_geoOwner = pd.read_excel("C:/Users/mm598h/Documents/Daily Alarms/Geo_Owner.xlsx")
df_Nodeid_tac = df_disabled[['NodeId', 'tac']]
df_Nodeid_tac= df_Nodeid_tac.drop_duplicates(subset = ["NodeId"])
df_alarm = df_alarm.assign(result=df_alarm['NodeId'].isin(df_disabled['NodeId']).astype(int))
df_alarm.drop(df_alarm[df_alarm['result'] == 0].index, inplace = True)
df_alarm.pop("result")
df_alarm['tac'] = df_alarm['NodeId'].map(df_Nodeid_tac.set_index('NodeId')['tac'])
df_filtered_sp = df_alarm.loc[df_alarm['specificProblem'].isin(['General HW Error', 'Resource Allocation Failure', 'Resource Activation Timeout', 'Service Unavailable', 'Heartbeat Failure'])]
df_filtered_sp=df_filtered_sp.drop_duplicates()
output = df_filtered_sp.merge(df_geoOwner, on='tac', how='outer')
output = output.dropna(subset=['presentSeverity', 'NodeId'])
output = output.drop(["repeatCount","commentTime","visibility","fmxGenerated","processingType","eventPoId","additionalInformation","backupObjectInstance","backupStatus","trendIndication","proposedRepairAction","ceaseOperator","ackTime","ackOperator","problemDetail","commentText","RNC Name","RNCs","Secondary Engineer","Manager","Area","System View"], axis = 1)
output.to_excel(r'C:\Users\mm598h\Downloads\SpecificProblem_04062022.xlsx',index = False)
output['specificProblem'].value_counts().plot(kind='pie', figsize=(10,8), autopct='%1.0f%%')
plt.title('Percentage of Specific Problems Identified',loc='right',color='r', fontsize=20)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.04))