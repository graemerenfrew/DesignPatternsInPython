from kpis import KPIs
from currentkpis import CurrentKPIs
from forecastkpis import ForecastKPIs

#report on the current KPIs
kpis = KPIs()
currentKPIs = CurrentKPIs(kpis)
forecastKPIs = ForecastKPIs(kpis)
kpis.set_kpis(25, 10, 5)
kpis.set_kpis(100, 50, 3)
kpis.set_kpis(50, 10, 20)

print("\n***Detaching current KPI observer***\n\n")
kpis.detach(currentKPIs)
kpis.set_kpis(150, 110, 120)