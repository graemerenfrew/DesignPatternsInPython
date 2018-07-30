from kpi_data import KPI_Data

#report on the current kpi values
for kpi in KPI_Data:
    if kpi.name == 'open':
        print('Current open tickets: %s ' % kpi.value)
    elif kpi.name == 'new':
        print("New tickets in last hr: %s " % kpi.value)
    elif kpi.name == "closed":
        print("Closed tix in last hr: %s " % kpi.value)